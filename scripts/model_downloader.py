import requests
import os
import wget
import hashlib
import time


MODEL_FOLDER = "/models" 
MODEL_FILENAME = "models.tar.gz"
MODEL_HOST = os.getenv('COACH_URL', 'coach')
VERSION_URL = "http://" + MODEL_HOST + "/version"
FILE_URL = 'http://' + MODEL_HOST + '/' + MODEL_FILENAME


def try_connect_coach():
    for _ in range(100):
        if get_version():
            print("Coach is available. Continuing config...")
            return
        print('Coach is unavailable. Retrying in 1 second')
        time.sleep(1)

    print('Maximum number of attempts connecting to coach')
    raise RuntimeError('could not connect to coach')


def get_version():
    try:
        r = requests.get(url=VERSION_URL)
        return True
    except:
        return False


def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest() + "  " + fname + "\n"


def uncompress_models(filename):
    os.system("tar -xzvf " + filename)
    os.system("mv src_models " + MODEL_FOLDER)


if __name__ == '__main__':

    try_connect_coach()
    
    if os.path.isfile(MODEL_FILENAME) == True:
        print("file already exist")
        r = requests.get(url = VERSION_URL)
        file_hash = md5(MODEL_FILENAME)
        if r.text != file_hash:
            print("new version model file")
            os.system("rm -r " + MODEL_FILENAME)
            os.system("rm -rf " + MODEL_FOLDER)
            wget.download(FILE_URL)
            uncompress_models(MODEL_FILENAME)
        else:
            print("same model")
            uncompress_models(MODEL_FILENAME)
    else:
        print("model not found")
        wget.download(FILE_URL)
        uncompress_models(MODEL_FILENAME)
