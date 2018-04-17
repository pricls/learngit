from datetime import datetime
now = datetime.now() 
print ('获取现在时间:',now)

print('获取计算机时间:',now.timestamp()) 

ts = now.timestamp()
print('timesatmp>>>datetime:',datetime.fromtimestamp(ts)) 

print('UTC标准时区:',datetime.utcfromtimestamp(ts)) 

cd = datetime.strptime('2018-1-1 22:54:43','%Y-%m-%d %H:%M:%S')
print ('字符串格式转化:',cd) 

print('现在时间的字符串形式:',now.strftime('%a,%b %d %H:%M:%S')) \

#时间运算
from datetime import timedelta 
af10h = now + timedelta(hours=10) 
print('10小时后:',af10h)
if1d = now - timedelta(days=1) 
print('1天前:',if1d)
af2d8h = now + timedelta(days=2, hours=8) 
print('2天8小时后:',af2d8h)

#UTC时间
from datetime import timezone
tz_utc_8 = timezone(timedelta(hours=8))
#创建时区UTC+8:00
dt = now.replace(tzinfo=tz_utc_8)
print('UTC时间:',dt)

#时区转化
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc) 
print('UTC+0:00:', utc_dt) #拿到UTC时间强制转化为UTC+0:00
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print('北京时间:', bj_dt) #北京时间
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print('东京时间:', tokyo_dt) #东京时间
tokys_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
print('北京时间>>>东京时间:',tokys_dt2)