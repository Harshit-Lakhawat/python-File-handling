import datetime

date = datetime.date(2025, 1,11)
today = datetime.date.today()

time = datetime.time(12, 30, 25)
now = datetime.datetime.now()

now =  now.strftime("%H:%M:%S  %d-%m-%y")

print(date)
print(time)
print(today)
print(now)




# target_datetime VS current_datetime
import datetime

date = datetime.date(2025, 1,11)
today = datetime.date.today()

time = datetime.time(12, 30, 25)
now = datetime.datetime.now()

now =  now.strftime("%H:%M:%S  %d-%m-%y")

target_datetime = datetime.datetime(200,12,11,4,8,56)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("target date has passed ")
else:
    print("yet to happen!")


print(date)
print(time)
print(today)
print(now)
