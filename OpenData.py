import requests
from datetime import datetime
import pytz



def sendEmail(tdelta):
    if(tdelta>3):
        print("send")
        return 1
    else:
        print("not send")
        return 0
        




def main():
    print("start")
    headers = {'UAuthorization': '5d0c4f23de394e0001045b5d390898efeea7423fb4090bb765d0d1ed'}
    url="https://uapi.ust.hk/sensor-data/_search?sort=@timestamp:desc&size=1"
    response = requests.get(url,headers=headers)

    jsontext=response.json()


    dt=response.json()['hits']['hits'][0]['_source']['@timestamp']
    print(response.status_code)

    date_time_obj = datetime.strptime(dt, '%Y-%m-%dT%H:%M:%S.%fZ')



    dt1 = date_time_obj.replace(tzinfo=pytz.utc)
    # print(dt1)

    dt2 = datetime.now(tz=pytz.UTC)
    # print(dt2)
    tdelta = dt2 - dt1 
    print(tdelta.seconds/60 ,"minute")
    sendEmail(tdelta.seconds/60)

if __name__ == "__main__":
    main()