#!/usr/bin/env python3
# coding: utf-8

import requests
import json
import os

host = "http://rocketchat:3000"
path = "/api/v1/login"

bot_name = 'ROCKETCHAT_USER'
bot_password = 'ROCKETCHAT_PASSWORD'
bot_email = botname + '@email.com'
admin_name = 'ADMIN_USERNAME'
admin_password = 'ADMIN_PASS'

def get_authentication_token():
    login_data = {"username": admin_name, "password": admin_password}
    response = requests.post(host+path, data=json.dumps(login_data))
    if response.json()['status'] == 'success':
        print("login suceeded\n")

        authToken = response.json()['data']['authToken']
        userId = response.json()['data']['userId']
        user_header = {
            "X-Auth-Token": authToken,
            "X-User-Id": userId,
            "Content-Type": "application/json"
        }

        return user_header


user_header = get_authentication_token()


def create_user():
    user_info = {
        "name": bot_name,
        "email": bot_email,
        "password": bot_password,
        "username": bot_name,
        "requirePasswordChange": False,
        "sendWelcomeEmail": True, "roles": ['bot']
    }

    create_user_response = requests.post(
        host + "/api/v1/users.create",
        data=json.dumps(user_info),
        headers=user_header
    )

    if create_user_response.json()['success'] is True:
        print("User has been sucessfully created!")
    else:
        print("Error while creating bot user!")


def create_agent():
    agent_info = {"username": bot_name}
    create_agent_response = requests.post(
        host + "/api/v1/livechat/users/agent",
        data=json.dumps(agent_info),
        headers=user_header
    )

    if create_agent_response.json()['success'] is True:
        print("Bot agent has been sucessfully created!")
    else:
        print("Error while creating bot agent!")

    return create_agent_response


def configure_livechat():
    # Enable Livechat
    requests.post(
        host + "/api/v1/settings/Livechat_enabled",
        data=json.dumps({"value": True}),
        headers=user_header
    )

    # Disable show pre-registration form
    requests.post(
        host + "/api/v1/settings/Livechat_registration_form",
        data=json.dumps({"value": False}),
        headers=user_header
    )


def create_department(bot_agent_id):
    department_info = {
        "department": {
            "enabled": True,
            "showOnRegistration": True,
            "name": "department",
            "description": "default department"
        },
        "agents": [{
            "agentId": bot_agent_id,
            "username": bot_name,
            "count": 0,
            "order": 0
        }]
    }
    create_department_response = requests.post(
        host + "/api/v1/livechat/department",
        data=json.dumps(department_info),
        headers=user_header
    )

    if create_department_response.json()['success'] is True:
        print("Default department has been sucessfully created!")
    else:
        print("Error while creating department!")


if user_header:
    create_user()

    create_agent_response = create_agent()
    bot_agent_id = create_agent_response.json()['user']['_id']

    configure_livechat()

    create_department(bot_agent_id)

else:
    print("login failed")
