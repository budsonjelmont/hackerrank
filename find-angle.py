#https://www.hackerrank.com/challenges/find-angle/problem?isFullScreen=true
import math

if __name__ == '__main__':
    # 1. Use pythag theorem to get length of third side
    # a**2 + b**2 = c**2
    lenab = int(input())
    lenbc = int(input())
    lenac = math.sqrt(math.pow(lenab,2) + math.pow(lenbc,2))
    midlenac = lenac / 2
    print(midlenac)
    # 2. Use law of sines to get angle A
    angCAB = math.asin((lenab * math.sin(90)) / lenac)
    print(angCAB)
    # 3. Use law of cosines to get length of missing side (c2 = a2 + b2 − 2ab cos(C))
    lenmb = math.sqrt(math.pow(lenbc,2) + math.pow(midlenac,2) - (2 * lenbc * midlenac * math.cos(angCAB)))
    print(lenmb)
    # 4. Use it again to get the angle we're looking for (cos(C) =  (a2 + b2 − c2)/2ab)
    angMBC =  math.acos((math.pow(lenmb,2) + math.pow(lenbc,2) - math.pow(midlenac,2))/(2 * lenmb * lenbc))
    print(angMBC)