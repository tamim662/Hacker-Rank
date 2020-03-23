import calendar
#calendar.setfirstweekday(5)

#print(calendar.TextCalendar(firstweekday=5).formatyear(2015))

m,d,y=input().split()

m,d,y=[int(m),int(d),int(y)]

#print(calendar.weekday(y,m,d))
if (y>2000 and y < 3000):
    day=calendar.weekday(y,m,d)


    result=calendar.day_name[day]
    print(result.upper())