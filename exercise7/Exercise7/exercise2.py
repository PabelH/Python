import time

hour = time.strftime('%H')
minutes = time.strftime('%M')

if int(hour) >= 19:
    print("It's time to go home!!!")
else:
    print("Only {} hours and {} minutes left to go home".format(18-int(hour), 59-int(minutes)))
