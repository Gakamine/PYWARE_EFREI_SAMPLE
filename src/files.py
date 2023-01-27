import os.path
import base64
import hashlib
import pathlib

def exfiltrate_file(filepath):
    if os.path.isfile(filepath):
        opnfile=open(filepath,"rb")
        encoded_file = base64.b64encode(opnfile.read()).decode()
        md5=hashlib.md5(encoded_file.encode("utf-8")).hexdigest()
        filetype=pathlib.Path(filepath).suffix.upper().replace('.', '')
        return md5,encoded_file,filetype
    else:
        return (None,None,None)
