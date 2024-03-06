from datetime import datetime, timedelta
a, b = datetime.now(), timedelta(days=1)
p = a -b
td = a
tm =a+b
print(p.strftime("%x"), td.strftime("%x"), tm.strftime("%x"))