# year=int(input())
# day=0

# if (( year%400 == 0)or (( year%4 == 0 ) and ( year%100 != 0))):
#     day=12
# else:
#     day=13
# month='{:02}'.format(9)

# list=map(str,[day,month,year])
# string=':'.join(list)
# print(string)


def dayOfProgrammer(year):
    day=0
    if(1700<=year<=1917):

        if (year%4==0):
    
            day=12
    if(1919<=year<=2700):

        if (( year%400 == 0)or (( year%4 == 0 ) and ( year%100 != 0))):

            day=12
    
        else:
            day=13
    month='{:02}'.format(9)

    list=map(str,[day,month,year])
    string='.'.join(list)
    return string

year=int(input())
result=dayOfProgrammer(year)
print(result)