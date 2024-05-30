import time as t
time_now = t.localtime()
print("Transaction complete at", str(time_now.tm_hour)+ "h" + str(time_now.tm_min) + "m")
t.sleep(5)
time_stamp = t.time() + (86400 * 7)
print (t.localtime(time_stamp))
