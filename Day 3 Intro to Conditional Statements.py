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

n=int(input())

if n>=1 and n<=100:
    if n%2!=0:
        print("Weird")
    else:
        if n<=5:
            print("Not Weird")
        else:
            if n<=20:
                print("Weird")
            else:
                print("Not Weird")