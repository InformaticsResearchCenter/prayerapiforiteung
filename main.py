import datetime

now=datetime.datetime.now()

#this api requested using LATITUDE and LONGITUDE
long="107.5785163"
lati="-6.8758087"

"""
"method" (number) -
A prayer times calculation method. Methods identify various schools of thought about how to compute the timings. This parameter accepts values from 0-12 and 99, as specified below:
0 - Shia Ithna-Ansari
1 - University of Islamic Sciences, Karachi
2 - Islamic Society of North America
3 - Muslim World League
4 - Umm Al-Qura University, Makkah
5 - Egyptian General Authority of Survey
7 - Institute of Geophysics, University of Tehran
8 - Gulf Region
9 - Kuwait
10 - Qatar
11 - Majlis Ugama Islam Singapura, Singapore
12 - Union Organization islamic de France
13 - Diyanet İşleri Başkanlığı, Turkey
14 - Spiritual Administration of Muslims of Russia
99 - Custom. See https://aladhan.com/calculation-methods
"""
method='5'

api='http://api.aladhan.com/v1/calendar?latitude={lati}&longitude={long}&method={method}&month={months}&year={years}'.format(lati=lati, long=long, method=method, months=now.month, years=now.year)

import requests

req=requests.get(api)
apidata=req.json()['data'][now.day-1]
fajr=apidata['timings']['Fajr']
sunrise=apidata['timings']['Sunrise']
dhuhr=apidata['timings']['Dhuhr']
asr=apidata['timings']['Asr']
sunset=apidata['timings']['Sunset']
maghrib=apidata['timings']['Maghrib']
isha=apidata['timings']['Isha']
imsak=apidata['timings']['Imsak']
midnight=apidata['timings']['Midnight']

print('Berdasarkan dari Lokasi yang kamu kirim berikut Jadwal Ibadah yang diminta...\n\n*JADWAL PUASA*\n\n*Tanggal: _{now}_*\n\nFajr: {fajr}\nSunrise: {sunrise}\nDhuhr: {dhuhr}\nAsr: {asr}\nSunset: {sunset}\nMaghrib: {maghrib}\nIsha: {isha}\nImsak: {imsak}\nMidnight: {midnight}'.format(fajr=fajr, sunrise=sunrise, dhuhr=dhuhr, asr=asr, sunset=sunset, maghrib=maghrib, isha=isha, imsak=imsak, midnight=midnight, now=now.strftime('%d-%m-%Y')))