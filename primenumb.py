attempt=0
n=0
while n<1 or n>10:
    n=eval(input('type a value from 1 to 10    '))
    attempt+=1
tries="try" if attempt==1 else "tries"
print(attempt," ",tries)
