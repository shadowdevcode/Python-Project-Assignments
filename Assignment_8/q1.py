import datetime

d = datetime.date(2012, 12, 19)
d.timetuple()
print(d.timetuple())
print(tuple(d.timetuple()))