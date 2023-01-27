import requests

def upload_data(BASE_URL,HOSTNAME,IP,DATATYPE,DATA,MD5=None):
    if MD5:
        file_parts=[DATA[i: i + 50] for i in range(0, len(DATA), 50)]
        for file_part in file_parts:
            url=BASE_URL+"f/"+HOSTNAME+"/"+IP+"/"+DATATYPE+"/"+MD5+"/"+file_part
            requests.get(url)
    else:
        url=BASE_URL+HOSTNAME+"/"+IP+"/"+DATATYPE+"/"+DATA
        requests.get(url)
