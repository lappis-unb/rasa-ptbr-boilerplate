#!/usr/bin/env python3

import json
import logging
import requests
import os

# == Log Config ==

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s :: %(name)s :: %(levelname)s :: %(message)s")

ch.setFormatter(formatter)

logger.addHandler(ch)


host = os.getenv("ROCKETCHAT_URL", "http://rocketchat:3000")
if host[-1] == "/":
    host = host[:-1]

if not host.startswith("http://"):
    host = "http://" + host

path = "/api/v1/login"

bot = {
    "name": os.getenv("ROCKETCHAT_BOT_NAME", "Bot"),
    "username": os.getenv("ROCKETCHAT_BOT_USERNAME", "bot"),
    "password": os.getenv("ROCKETCHAT_BOT_PASSWORD", "bot"),
    "avatar": os.getenv(
        "ROCKETCHAT_BOT_AVATAR_URL",
        "https://raw.githubusercontent.com/"
        "lappis-unb/rouana/master/images/rouana_avatar.jpeg",
    ),
    "email": os.getenv("ROCKETCHAT_BOT_USERNAME", "bot") + "@email.com",
}

admin_name = os.getenv("ROCKETCHAT_ADMIN_USERNAME", "admin")
admin_password = os.getenv("ROCKETCHAT_ADMIN_PASSWORD", "admin")

rasa_url = os.getenv("RASA_URL", "http://bot-rocket:5005/webhooks/rocketchat/webhook")
user_header = None


def api(endpoint, values=None, is_post=True):
    requests.adapters.DEFAULT_RETRIES = 5

    if endpoint[0] == "/":
        endpoint = endpoint[1:]

    url = host + "/api/v1/" + endpoint

    data = None
    if values:
        data = json.dumps(values)
    if is_post:
        response = requests.post(url, data=data, headers=user_header)
    else:
        response = requests.get(url, data=data, headers=user_header)

    if response.json()["success"] is True:
        logger.info("Success {} :: {}".format(url, response.json()))
    else:
        logger.error("ERROR {} :: {}".format(url, response.json()))
        raise EnvironmentError

    return response.json()


def api_post(endpoint, values=None):
    return api(endpoint, values)


def api_get(endpoint, values=None):
    return api(endpoint, values, False)


def get_authentication_token():
    login_data = {"username": admin_name, "password": admin_password}
    response = requests.post(host + path, data=json.dumps(login_data))

    if response.json()["status"] == "success":
        logger.info("Login suceeded")

        authToken = response.json()["data"]["authToken"]
        userId = response.json()["data"]["userId"]
        user_header = {
            "X-Auth-Token": authToken,
            "X-User-Id": userId,
            "Content-Type": "application/json",
        }

        return user_header


def create_bot_user():
    try:
        api_post(
            "users.create",
            {
                "name": bot["name"],
                "email": bot["email"],
                "password": bot["password"],
                "username": bot["username"],
                "requirePasswordChange": False,
                "sendWelcomeEmail": True,
                "roles": ["bot"],
            },
        )
    except Exception:
        print("User already created.")

    api_post(
        "users.setAvatar",
        {"avatarUrl": bot["avatar"], "username": bot["username"]},
    )


def configure_webhooks():
    webooks = api_get("integrations.list")

    name = "Rasa Webhook"

    for integration in webooks["integrations"]:
        if integration.get("name") == name:
            logger.info("Intergration {} already exists!".format(name))
            return

    api_post(
        "integrations.create",
        {
            "name": name,
            "type": "webhook-outgoing",
            "enabled": True,
            "scriptEnabled": False,
            "event": "sendMessage",
            "urls": [rasa_url],
            "username": bot["username"],
            "channel": "@" + bot["username"],
        },
    )


def configure_rocketchat():
    api_post("settings/Language", {"value": "pt_BR"})

    api_post("settings/Accounts_RegistrationForm", {"value": "Disable"})

    api_post("settings/Iframe_Integration_send_enable", {"value": True})

    api_post("settings/Iframe_Integration_receive_enable", {"value": True})

    api_post("settings/API_Enable_CORS", {"value": True})


if __name__ == "__main__":
    logger.info("===== Automatic env configuration =====")

    rocket_available = False

    while not rocket_available:
        try:
            user_header = get_authentication_token()
            rocket_available = True
        except Exception:
            import time

            logger.info("\n\n --------- Rocket Chat Unavailable! --------\n\n")
            logger.info(">> Waiting for 3 seconds...")
            time.sleep(3)

    logger.info(">> Connected to Rocket Instance")

    if user_header:
        try:
            logger.info(">> Create user")
            create_bot_user()

            logger.info(">> Configure Rocketchat")
            configure_rocketchat()

            logger.info(">> Configure Webhooks")
            configure_webhooks()
        except Exception as e:
            logger.error(f"Problem while trying to configure bot in Rocketchat: {e}")

    else:
        logger.error(">> Login Failed")
