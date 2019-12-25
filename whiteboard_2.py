
import datetime

mine = datetime.datetime.now()
mine2 = mine.timetz()



print(datetime.tzinfo.tzname(datetime.datetime.now().tzinfo()))