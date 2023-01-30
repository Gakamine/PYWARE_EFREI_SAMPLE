import requests

def upload_data(BASE_URL,HOSTNAME,IP,DATATYPE,DATA,MD5=None):
    if MD5:
        file_parts=[DATA[i: i + 3500] for i in range(0, len(DATA), 3500)]
        for file_part in file_parts:
            url="{}/f/{}/{}/{}/{}/{}".format(BASE_URL,HOSTNAME,IP,DATATYPE,MD5,file_part)
            requests.get(url)
    else:
        url="{}/{}/{}/{}/{}".format(BASE_URL,HOSTNAME,IP,DATATYPE,DATA)
        requests.get(url)
