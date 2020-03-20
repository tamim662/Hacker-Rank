# My Approach
'''s=input("Enter a string:")

if(len(s)>0 and len(s)<1000):
    new_s=s.split(" ")



for i in range (len(new_s)):
    print(new_s[i].capitalize(),end=" ")'''

#!/bin/python3
#hacker Rank

import math
import os
import random
import re
import sys

# Complete the solve function below.

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
#from __future__ import print_function
def solve(s):
    result=''
    if(len(s)>0 and len(s)<1000):
        new_s=s.split(" ")
    for i in range (len(new_s)):
         result+=new_s[i].capitalize()+" "
        
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

