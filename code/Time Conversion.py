#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    if(s[8:] == 'AM'):
        thour = int(s[0:2])%12
        if(not thour):
            t = '00'+ s[2:8]
        elif(thour < 10):
            t = '0' + str(thour) + s[2:8]
        else:
            t = str(thour) + s[2:8]
    else:
        thour = 12 + int(s[0:2])%12
        t = str(thour) + s[2:8]
    return t
if __name__ == '__main__':
    # f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)
    print(result)
    # f.write(result + '\n')
    #
    # f.close()