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
    '--bot-name', '-bn', type=str, default='Bot',
    help='Bot username at RocketChat(default: Bot)'
)
parser.add_argument(
    '--bot-username', '-bu', type=str, default='bot',
    help='Bot username at RocketChat(default: bot)'
)
parser.add_argument(
    '--bot-password', '-bp', type=str, default='bot',
    help='Bot password at RocketChat(default: bot)'
)
parser.add_argument(
    '--bot-avatar', '-ba', type=str, default='https://raw.githubusercontent.com/lappis-unb/rouana/master/images/rouana_avatar.jpeg',
    help='Bot avatar photo link (default: bot\'s github avatar)'
)
parser.add_argument(
    '--admin-name', '-an', type=str, default='admin',
    help='Admin username at RocketChat(default: admin)'
)
parser.add_argument(
    '--admin-password', '-ap', type=str, default='admin',
    help='Admin password at RocketChat(default: admin)'
)
parser.add_argument(
    '--rocketchat-url', '-r', type=str, default='http://rocketchat:3000',
    help='Rocket chat URL (default: http://rocketchat:3000)'
)
parser.add_argument(
    '--rasa-url', '-rasa', type=str, default='http://bot:5005/webhooks/rocketchat/webhook',
    help='Rasa URL (default: http://bot:5005/webhooks/rocketchat/webhook)'
)

args = parser.parse_args()


host = args.rocketchat_url
if host[-1] == '/':
    host = host[:-1]

if not host.startswith('http://'):
    host = 'http://' + host

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

def api(endpoint, values=None, is_post=True):
    if endpoint[0] == '/':
        endpoint = endpoint[1:]

    url = host + '/api/v1/' + endpoint

    data = None
    if values:
        data = json.dumps(values)

    if is_post:
        response = requests.post(url, data=data, headers=user_header)
    else:
        response = requests.get(url, data=data, headers=user_header)

    if response.json()['success'] is True:
        logger.info('Success {} :: {}'.format(url, response.json()))
    else:
        logger.error('ERROR {} :: {}'.format(url, response.json()))

    return response.json()

def api_post(endpoint, values=None):
    return api(endpoint, values)

def api_get(endpoint, values=None):
    return api(endpoint, values, False)


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
    api_post('users.create', {
        'name': bot['name'],
        'email': bot['email'],
        'password': bot['password'],
        'username': bot['username'],
        'requirePasswordChange': False,
        'sendWelcomeEmail': True, 'roles': ['bot']
    })

    api_post('users.setAvatar', {
        'avatarUrl': bot['avatar'],
        'username': bot['username']
    })


def create_livechat_agent():
    response = api_post('livechat/users/agent', {'username': bot['username']})
    return response['user']['_id']


def configure_livechat():
    # Enable Livechat
    api_post('settings/Livechat_enabled', {'value': True})

    # Disable show pre-registration form
    api_post('settings/Livechat_registration_form', {'value': False})

    # Change Livechat Color
    api_post('settings/Livechat_title_color', {
        'value': "#039046",
        'editor': 'color'
    })

    # Change Livechat Title
    api_post('settings/Livechat_title', {'value': bot['name']})

    # Disable Livechat Email display
    api_post('settings/Livechat_show_agent_email', {'value': False})

    # Disable file upload
    api_post('settings/Livechat_fileupload_enabled', {'value': False})

    # Change Livechat Webhook URL
    api_post('settings/Livechat_webhookUrl', {'value': rasa_url})

    # Activate Livechat Webhook Send Request on Visitor Message
    api_post('settings/Livechat_webhook_on_visitor_message', {'value': True})

    # Activate Livechat Webhook Send Request on Agent Messages
    api_post('settings/Livechat_webhook_on_agent_message', {'value': True})


def configure_webhooks():
    webooks = api_get('integrations.list')

    name = 'Rasa Webhook'

    for integration in webooks['integrations']:
        if integration.get('name') == name:
            logger.info('Intergration {} already exists!'.format(name))
            return

    api_post('integrations.create',
        {
            'name': name,
            'type': 'webhook-outgoing',
            'enabled': True,
            'scriptEnabled': False,
            'event': 'sendMessage',
            'urls': [rasa_url],
            'username': bot['username'],
            'channel': '@' + bot['username'],
        }
    )


def configure_rocketchat():
    api_post('settings/Language', {'value': 'pt_BR'})

    api_post('settings/Accounts_RegistrationForm', {'value': 'Disable'})

    api_post('settings/Iframe_Integration_send_enable', {'value': True})

    api_post('settings/Iframe_Integration_receive_enable', {'value': True})

    api_post('settings/API_Enable_CORS', {'value': True})


def create_department(bot_agent_id):
    get_departments_url = host + '/api/v1/livechat/department'

    get_departments_response = requests.get(
        get_departments_url,
        headers=user_header
    )

    number_of_departments = len(get_departments_response.json()['departments'])

    if number_of_departments == 0:
        api_post('livechat/department', {
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
        })

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

        logger.info('>> Configure Rocketchat')
        configure_rocketchat()

        logger.info('>> Configure Webhooks')
        configure_webhooks()

        logger.info('>> Create livechat department')
        create_department(bot_agent_id)

    else:
        logger.error('Login Failed')
