from random import randrange, seed
from time import clock
                    #PRINTING RANDOM NUMBERS
##seed(200)
##count=0
##for i in range(0,100):
##    print(randrange(1,1000), end='   ')
##    count+=1
##print()
##print(count)
#print(randrange(0,100))
                        #GAME
x=randrange(1,100)
guess=eval(input("guess the number : "))
start=clock()
count,i=0,0
while guess!=x:
    if guess<x:
        i+=1
        print(10-i, "tries left")
        print("go up!")
        guess=eval(input("guess the number : "))
        count+=1
    if guess>x:
        i+=1
        print(10-i, "tries left")
        print("go down!")
        guess=eval(input("guess the number : "))
        count+=1
    if i==9:
        print("you lost!\t", x, " is the right number")
        print(clock()-start, "secondes")
        break
print()
if guess==x:
    print("you got it!!!   ",x," is the right number")
    print(count, "tries")
    sec=clock()-start
    print(sec, "secondes")
    
