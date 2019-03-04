from math import sqrt
from time import clock
x1,y1=eval(input("type the coordinates (x1,y1):   "))
start=clock()
x2,y2=eval(input("type the coordinate (x2,y2):  "))
r=sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))
time=clock()-start
print(r)
print("it took you ",time, "s to type all the coordinates")
