''' Exercício referente ao vídeo 17 
 André de Oliveira Águila Favoto - 11811EAU013''' 

import datetime

import pytz

# tday = datetime.date.today()
# # print(tday.weekday())
# # print(tday.isoweekday())

# tdelta = datetime.timedelta(days=7)
# print(tday - tdelta)

# bday = datetime.date(2016, 9, 24)

# till_bday = bday -tday
# print(till_bday.total_seconds())


# """ t = datetime.time(9, 30, 45, 100000)
# print(t.hour) """

# dt = datetime.datetime(2016, 7, 26, 12, 30, 45, 100000)

# tdelta = datetime.tdelta(hours=12)
# print(dt + tdelta)

print(datetime.datetime.today(), datetime.datetime.now(), datetime.datetime.utcnow())

dt = datetime.datetime(2016, 7, 27, 12, 30, 45, tzinfo=pytz.UTC)

dt_now = datetime.datetime.now(tz = pytz.UTC)
print(dt_now)
dt_utcnow =  datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print(dt_now)

for tz in pytz.all_timezones:
    print(tz)