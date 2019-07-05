#!/bin/python3

import math
import os
import random
import re
import sys
def solve(s):
    # 1st method
    #Str=s.split(" ")
    #print(Str)
    #Lisr2=[i.capitalize() for i in Str]
    #print(Lisr2)
    #return ' '.join(Lisr2)

    #2nd method
    #Str = s.split(' ')
    #print(Str)
    #return ' '.join(word.capitalize() for word in Str)
    #3rd method

    for x in s[:].split():
        s=s.replace(x,x.capitalize())

    return s.capitalize()

if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)
    print(result)

 #   fptr.write(result + '\n')

#    fptr.close()
