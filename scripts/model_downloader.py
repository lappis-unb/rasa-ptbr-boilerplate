import requests
import os
import wget
import hashlib


MODEL_FOLDER = "/models" 
MODEL_FILENAME = "models.tar.gz"
MODEL_HOST = os.getenv('COACH_URL', 'coach')
VERSION_URL = "http://" + MODEL_HOST + "/version"
FILE_URL = 'http://' + MODEL_HOST + '/' + MODEL_FILENAME

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest() + "  " + fname + "\n"

def uncompress_models(filename):
    os.system("tar -xzvf " + filename)
    os.system("mv src_models " + MODEL_FOLDER)


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