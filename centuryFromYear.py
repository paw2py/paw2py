find the centur of a given year
 year 1 to 100 is centur 1
 year  101 to 200 is centur 2

from math import trunc
def solution(year):
    if year < 100:
        return 1
    if year % 100 == 0:
        return round(year/100)
    else:
        return trunc(year/100) + 1    

