import urllib.request, json
import pytz
from datetime import datetime
dateTimeStr=datetime.utcnow().replace(tzinfo=pytz.utc)
with urllib.request.urlopen("https://mds.bird.co/gbfs/los-angeles/free_bikes") as url:
    data = json.loads(url.read().decode())
retStr='lat,lon,isdisabled,time\n'
for item in data["data"]["bikes"]:
    retStr+=str(item['lat'])+','+str(item['lon'])+','+str(item['is_disabled'])+','+str(dateTimeStr)+'\n'
with open('outputData.csv', 'a+') as writer:
    writer.writelines(retStr)

