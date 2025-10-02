#CC 7th time notes????

import time 
import datetime 

epoch = time.time()
reasonable_time = time.ctime(epoch)

print(f"The time scince Jan 1, 1970: {epoch}")
print(f"The time is: {reasonable_time}")

now = datetime.datetime.now()
hour = now.hour
print(f"the time is {now}")
print(f"The hour is {hour}")