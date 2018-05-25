#!/usr/bin/env python3

import argparse
import json
import logging
import requests

# == Log Config ==

logger = logging.getLogger('Bot Config')
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    '%(asctime)s :: %(name)s :: %(levelname)s :: %(message)s'
)

ch.setFormatter(formatter)

logger.addHandler(ch)

# == CLI ==

parser = argparse.ArgumentParser()

parser.add_argument(
    '--bot-name', '-bn', type=str, default='rouana',
    help='Bot username (default: rouana)'
)
parser.add_argument(
    '--bot-password', '-bp', type=str, default='rouana',
    help='Bot password (default: rouana)'
)
parser.add_argument(
    '--admin-name', '-an', type=str, default='admin',
    help='Admin username (default: admin)'
)
parser.add_argument(
    '--admin-password', '-ap', type=str, default='admin',
    help='Admin password (default: rouana)'
)
parser.add_argument(
    '--rocketchat-url', '-r', type=str, default='http://localhost:3000',
    help='Rocket chat URL (default: http://localhost:3000)'
)

args = parser.parse_args()


host = args.rocketchat_url
if host[-1] == '/':
    host = host[:-1]

path = '/api/v1/login'

bot_name = args.bot_name
bot_password = args.bot_password
admin_name = args.admin_name
admin_password = args.admin_password

bot_email = bot_name + '@email.com'
user_header = None


def get_authentication_token():
    login_data = {'username': admin_name, 'password': admin_password}
    response = requests.post(host + path, data=json.dumps(login_data))

    if response.json()['status'] == 'success':
        logger.info('Login suceeded')

        authToken = response.json()['data']['authToken']
        userId = response.json()['data']['userId']
        user_header = {
            'X-Auth-Token': authToken,
            'X-User-Id': userId,
            'Content-Type': 'application/json'
        }

        return user_header


def create_bot_user():
    user_info = {
        'name': bot_name,
        'email': bot_email,
        'password': bot_password,
        'username': bot_name,
        'requirePasswordChange': False,
        'sendWelcomeEmail': True, 'roles': ['bot']
    }

    create_user_response = requests.post(
        host + '/api/v1/users.create',
        data=json.dumps(user_info),
        headers=user_header
    )

    if create_user_response.json()['success'] is True:
        logger.info('User has been sucessfully created!')
    else:
        logger.error('Error while creating bot user!')


def create_livechat_agent():
    agent_info = {'username': bot_name}
    create_agent_response = requests.post(
        host + '/api/v1/livechat/users/agent',
        data=json.dumps(agent_info),
        headers=user_header
    )

    if create_agent_response.json()['success'] is True:
        logger.info('Bot agent has been sucessfully created!')
    else:
        logger.error('Error while creating bot agent!')

    return create_agent_response.json()['user']['_id']


def configure_livechat():
    # Enable Livechat
    requests.post(
        host + '/api/v1/settings/Livechat_enabled',
        data=json.dumps({'value': True}),
        headers=user_header
    )

    # Disable show pre-registration form
    requests.post(
        host + '/api/v1/settings/Livechat_registration_form',
        data=json.dumps({'value': False}),
        headers=user_header
    )


def create_department(bot_agent_id):
    department_info = {
        'department': {
            'enabled': True,
            'showOnRegistration': True,
            'name': 'department',
            'description': 'default department'
        },
        'agents': [{
            'agentId': bot_agent_id,
            'username': bot_name,
            'count': 0,
            'order': 0
        }]
    }
    create_department_response = requests.post(
        host + '/api/v1/livechat/department',
        data=json.dumps(department_info),
        headers=user_header
    )

    if create_department_response.json()['success'] is True:
        logger.info('Default department has been sucessfully created!')
    else:
        logger.error('Error while creating department!')


if __name__ == '__main__':
    logger.info('===== Automatic env configuration =====')

    user_header = get_authentication_token()

    if user_header:
        logger.info('>> Create user')
        create_bot_user()

        logger.info('>> Create livechat agent')
        bot_agent_id = create_livechat_agent()

        logger.info('>> Configure livechat')
        configure_livechat()

        logger.info('>> Create livechat department')
        create_department(bot_agent_id)

    else:
        logger.error('Login Failed')
