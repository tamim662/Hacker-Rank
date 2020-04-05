#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    
    arr=s.split(":")
    arr[0]=int(arr[0])
    ar=arr[-1]
    for i in range(len(ar)):
        if (arr[0]!=12 and ar[i]=="P"):
            arr[0]+=12
        elif(arr[0]==12 and ar[i]=="P"):
            pass
        elif (arr[0]==12 and ar[i]=="A"):
            arr[0]-=12
            
       
    arr[0]='{:02}'.format(arr[0])
        
    arr[0]=str(arr[0]) 

 
    string=":".join(arr)
    for i in range(len(string)):
        # if (string[i]=="A" or string[i]=="P" or string[i]=="M"):
        string=string.replace("A","")
        string=string.replace("P","")
        string=string.replace("M","")

    return string








if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
