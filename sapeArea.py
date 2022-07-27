Below we will define an n-interesting polygon. Your task is to find the area of a polygon for a given n.

A 1-interesting polygon is just a square with a side of length 1. An n-interesting polygon is obtained by taking the 
n - 1-interesting polygon and appending 
1-interesting polygons to its rim, side by side. You can see the 1-, 2-, 3- and 4-interesting polygons in the picture below.

def solution(n):
    if n <= 0:
        return 0
    noarea = 0
    i = n
    while i > 0:
        noarea += i -1
        i -= 1
    print(noarea)
    temp = (n+(n-1)) * (n+(n-1))
    print(temp)
    return temp - (noarea * 4)
   
