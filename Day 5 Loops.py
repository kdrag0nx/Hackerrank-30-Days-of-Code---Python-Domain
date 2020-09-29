'''
Author Name: Amit Kumar
Python version: Python 3.5 7 above

''
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    if n>=2 and n<=20:
        x=1
        a=n

        for i in range(1,11):
                multiple=n*x
                print(a,'x',x,'=',multiple,"\n",end="")#if you give simply \n then it will add lines and space too so if you want to remove space in between the lines then give end = "" symbol,now slash n will change the line as well and end symbol will delete the spacing in between two
                x +=1
