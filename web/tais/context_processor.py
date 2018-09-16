import os

def env_vars(request):
    return {
        'ROCKETCHAT_URL': os.getenv('ROCKETCHAT_URL'),
    }
