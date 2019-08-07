import requests
import os
import wget
import hashlib

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest() + "  " + fname + "\n"

file_url = 'http://localhost/models.tar.gz'
version_url = "http://localhost/version"


if os.path.isfile('models.tar.gz') == True:
    r = requests.get(url = version_url)
    file_hash = md5("models.tar.gz")
    if r.text != file_hash:
        os.system("rm -r models.tar.gz")
        wget.download(file_url)
    else:
        pass
else:
    wget.download(file_url)

