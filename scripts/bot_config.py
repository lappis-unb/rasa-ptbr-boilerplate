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
    '--bot-name', '-bn', type=str, default='Tais',
    help='Bot username (default: rouana)'
)
parser.add_argument(
    '--bot-username', '-bu', type=str, default='rouana',
    help='Bot username (default: rouana)'
)
parser.add_argument(
    '--bot-password', '-bp', type=str, default='rouana',
    help='Bot password (default: rouana)'
)
parser.add_argument(
    '--bot-avatar', '-ba', type=str, default='https://raw.githubusercontent.com/lappis-unb/rouana/master/images/rouana_avatar.jpeg',
    help='Bot avatar photo link (default: rouana\'s github avatar)'
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
parser.add_argument(
    '--rasa-url', '-rasa', type=str, default='http://rouana:5005/webhook',
    help='Rasa URL (default: http://rouana:5005/webhook)'
)

args = parser.parse_args()


host = args.rocketchat_url
if host[-1] == '/':
    host = host[:-1]

path = '/api/v1/login'

bot = {
    'name': args.bot_name,
    'username': args.bot_username,
    'password': args.bot_password,
    'avatar': args.bot_avatar,
    'email': args.bot_name + '@email.com',
}

admin_name = args.admin_name
admin_password = args.admin_password

rasa_url = args.rasa_url

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
        'name': bot['name'],
        'email': bot['email'],
        'password': bot['password'],
        'username': bot['username'],
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

    requests.post(
        host + '/api/v1/users.setAvatar',
        data=json.dumps({
            'avatarUrl': bot['avatar'],
            'username': bot['username']
        }),
        headers=user_header
    )


def create_livechat_agent():
    agent_info = {'username': bot['username']}
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

    # Change Livechat Color
    requests.post(
        host + '/api/v1/settings/Livechat_title_color',
        data=json.dumps({'value': "#039046", 'editor': 'color'}),
        headers=user_header
    )

    # Change Livechat Title
    requests.post(
        host + '/api/v1/settings/Livechat_title',
        data=json.dumps({'value': bot['name']}),
        headers=user_header
    )

    # Disable Livechat Email display
    requests.post(
        host + '/api/v1/settings/Livechat_show_agent_email',
        data=json.dumps({'value': False}),
        headers=user_header
    )

    # Change Livechat Webhook URL
    requests.post(
        host + '/api/v1/settings/Livechat_webhookUrl',
        data=json.dumps({'value': rasa_url}),
        headers=user_header
    )

    # Activate Livechat Webhook Send Request on Visitor Message
    requests.post(
        host + '/api/v1/settings/Livechat_webhook_on_visitor_message',
        data=json.dumps({'value': True}),
        headers=user_header
    )

    # Activate Livechat Webhook Send Request on Agent Messages
    requests.post(
        host + '/api/v1/settings/Livechat_webhook_on_agent_message',
        data=json.dumps({'value': True}),
        headers=user_header
    )


def configure_webhooks():
    webooks = requests.get(
        host + '/api/v1/integrations.list',
        headers=user_header
    ).json()

    name = 'Rasa Webhook'

    for integration in webooks['integrations']:
        if 'name' in integration and integration['name'] == name:
            logger.info('Intergration {} already exists!'.format(name))
            return

    requests.post(
        host + '/api/v1/integrations.create',
        data=json.dumps({
            'name': name,
            'type': 'webhook-outgoing',
            'enabled': True,
            'scriptEnabled': False,
            'event': 'sendMessage',
            'urls': [rasa_url],
            'username': bot['username'],
            'channel': '@' + bot['username'],
        }),
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
            'username': bot['username'],
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

        logger.info('>> Configure webhooks')
        configure_webhooks()

        logger.info('>> Create livechat department')
        create_department(bot_agent_id)

    else:
        logger.error('Login Failed')
