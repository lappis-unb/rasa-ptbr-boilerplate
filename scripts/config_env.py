#!/usr/bin/env python

import json
import logging
import requests
import argparse
from time import sleep

# == Log Config ==
logging.basicConfig(format='%(levelname)s : %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# == CLI ==
parser = argparse.ArgumentParser()

parser.add_argument(
    '--admin-name', '-an', type=str, default='boss',
    help='Admin username (default: boss)'
)
parser.add_argument(
    '--admin-password', '-ap', type=str, default='boss',
    help='Admin password (default: boss)'
)

parser.add_argument(
    '--bot-name', '-bn', type=str, default='rasa_bot',
    help='Bot username (default: rasa_bot)'
)
parser.add_argument(
    '--bot-password', '-bp', type=str, default='rasa_bot',
    help='Bot password (default: rasa_bot)'
)

args = parser.parse_args()

# == Admin Info == 
admin_name = args.admin_name 
admin_password = args.admin_password

# == Bot Info == 
bot_name = args.bot_name
bot_password = args.bot_password 
bot_email = bot_name + '@email.com'

# == Host Info ==
#host = http://rocketchat:3000/ # Rocketchat - Docker
host = "http://localhost:3000/" # Rockechat - Local
path = "/api/v1/login"
user_header = None


def get_authentication_token(user):
    login_data = {"username": user, "password": user}
    response = requests.post(host + path, data=login_data)

    if response.json()["status"] == "success":
        logger.info(f"Login succeed | Header = {user}")

        authToken = response.json()["data"]["authToken"]
        userId = response.json()["data"]["userId"]
        user_header = {
            "X-Auth-Token": authToken,
            "X-User-Id": userId,
            "Content-Type": "application/json"
        }

        return user_header
    else:
        logger.error(f"Login failed | {response}") 

def create_bot_user():
    user_info = {
        "name": bot_name,
        "email": bot_email,
        "password": bot_password,
        "username": bot_name,
        "requirePasswordChange": False,
        "sendWelcomeEmail": True, 
        "roles": ["bot", "livechat-agent"],
    }

    user_header = get_authentication_token(admin_name)

    create_user_response = requests.post(
        host + '/api/v1/users.create',
        data=json.dumps(user_info),
        headers=user_header
    )

    if create_user_response.json()["success"] == True:
        logger.info(f"Bot created | Bot = {bot_name}")
    else:
        logger.error(f"Unable to create bot  | {create_user_response}")

    
def set_avatar(user):
    avatar_config = {
        "username": user,
        "avatarUrl": "https://www.rasa.com/assets/img/sara/sara-open-source-2.0.png",
    }

    user_header = get_authentication_token(user)

    set_avatar_response = requests.post(
        host + "api/v1/users.setAvatar",
        data=json.dumps(avatar_config),
        headers=user_header
    )

    if set_avatar_response.json()["success"] == True:
        logger.info(f"Avatar updated | User = {user}")
    else:
        logger.error(f"Unable to create avatar | {set_avatar_response}")

def set_status_active(user):
    user_status = {
        "message": "My status update", 
        "status": "online" 
    }

    user_header = get_authentication_token(user)

    set_user_status_response = requests.post(
        host + "/api/v1/users.setStatus",
        data=json.dumps(user_status),
        headers=user_header
    )

    if set_user_status_response.json()["success"] == True:
        logger.info(f"Status ON | User = {user}")
    else:
        logger.error(f"Status OFF | {set_user_status_response}")
    
def config_bot():
    create_bot_user()
    set_avatar(bot_name)
    set_status_active(bot_name)

def config_livechat():
    user_header = get_authentication_token(admin_name)

    # Enable Livechat
    livechat_response = requests.post(
        host + '/api/v1/settings/Livechat_enabled',
        data=json.dumps({'value': True}),
        headers=user_header
    )

    if livechat_response.json()["success"] == True:
        logger.info("Livechat ON")
    else:
        logger.error(f"Livechat OFF | {livechat_response}")
    
    # Disable show pre-registration form
    registration_form_response = requests.post(
        host + '/api/v1/settings/Livechat_registration_form',
        data=json.dumps({'value': False}),
        headers=user_header
    )

    if registration_form_response.json()["success"] == True:
        logger.info(f"Registration form disabled!") 
    else:
        logger.error(f"Registration still enabled... {registration_form_response}")

def config_department():
    bot_id = get_authentication_token(bot_name)["X-User-Id"]
    admin_header = get_authentication_token(admin_name)

    department_info = {
        'department': {
            'enabled': True,
            'showOnRegistration': True,
            'showOnOfflineForm': True,
            'email': bot_email,
            'name': 'department',
            'description': 'default department'
        },
        'agents': [{
            'agentId': bot_id,
            'username': bot_name,
            'count': 0,
            'order': 0
        }]
    }

    create_department_response = requests.post(
        host + '/api/v1/livechat/department',
        data=json.dumps(department_info),
        headers=admin_header
    )

    if create_department_response.json()['success'] is True:
        logger.info('Default Department ON')
    else:
        logger.error(f'Error while creating department! | {create_department_response.text}')

if __name__ == '__main__':
    logger.info("===== Sara Mascot S2 =====")

    #rasa_url = "http://bot:5005/"      # Rasa - Docker
    rasa_url = "http://localhost:5005/" # Rasa - Local


    response = False

    # O script verifica se o servidor Rasa subiu antes de executar #
    while(not response):
        try:
            response = requests.get(rasa_url)
            response = True
            logger.info("Rasa Server UP!")

            logger.info(">> Configure Bot")
            config_bot()

            logger.info(">> Configure Livechat")
            config_livechat()

            logger.info(">> Cofigure Department")
            config_department()

        except:
            logger.info("Rasa Server DOWN...") 
        finally:
            sleep(3)

    logger.info("===== END =====")
