import sys
import os
import re
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def main():
    yc = [6,4,2,0,6,4,2,0,6,4,2,0,6,4,2,0,6,4,2,0,6,4,2,0,6,4,2,0,6,4,2,0,6,4,2,0]
    mc = [1,4,4,0,2,5,0,3,6,1,4,6]
    dc = [0,1,2,3,4,5,6]
    date = input("Enter a date in the format YYYYMMDD: ")
    year = int(date[0:4])
    month = int(date[4:6])
    day = int(date[6:8])
    yf= int(date[0:2])
    yl=int(date[2:4])
    #convert to int
    year = int(year)
    print (year) 
    y = yc[int(yf)]
    m = mc[int(month)-1]
    a=day+m+y+yl+math.floor(yl/4)
    f=a%7
    print (f)
    if f == 0:
        print ("Saturday")
    elif f == 1:
        print ("Sunday")
    elif f == 2:
        print ("Monday")
    elif f == 3:
        print ("Tuesday")
    elif f == 4:
        print ("Wednesday")
    elif f == 5:
        print ("Thursday")
    elif f == 6:
        print ("Friday")
    else:
        print ("Error")


    pass

if __name__ == "__main__":
    main()


