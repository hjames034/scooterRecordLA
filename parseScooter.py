import urllib.request, json
import pytz
from datetime import datetime
dateTimeStr=datetime.utcnow().replace(tzinfo=pytz.utc)
def jsonReaderScooter(urlToOpen):
    with urllib.request.urlopen(urlToOpen) as url:
        data = json.loads(url.read().decode())
    retStr='lat,lon,isdisabled,time\n'
    try:
        with open('outputDataUpdated.csv','r') as reader:
            if retStr in reader:
                retStr=''
    except:
        pass
    for item in data["data"]["bikes"]:
        retStr+=str(item['lat'])+','+str(item['lon'])+','+str(item['is_disabled'])+','+str(dateTimeStr)+'\n'
    with open('outputDataUpdated.csv', 'a+') as writer:
        writer.writelines(retStr)
    return True
url = ["https://mds.bird.co/gbfs/los-angeles/free_bikes","https://s3.amazonaws.com/lyft-lastmile-production-iad/lbs/lax/free_bike_status.json","https://la-gbfs.getwheelsapp.com/free_bike_status.json"]
for i in url:
    jsonReaderScooter(i)
