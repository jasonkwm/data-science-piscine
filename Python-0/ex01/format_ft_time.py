import datetime as dt
import time as t
x = dt.datetime.now()
time_now = t.time()
print("Seconds since January 1, 1970: {:,.4f}, {:.2e} in scientific notation".format(time_now, time_now))
print(x.strftime("%b %d %Y"))
