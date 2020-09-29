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
    ar=" "
    n = int(input())

    arr = list(map(str,input().rstrip().split()))
    arr.reverse()
    listToStr = ' '.join([str(elem) for elem in arr]) 

    print(listToStr)
    