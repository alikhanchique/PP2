import datetime
a = datetime.datetime.now()
b = datetime.timedelta(days=5)
c = a-b
print(c.strftime("%x"))