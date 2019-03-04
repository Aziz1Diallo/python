##def gcd(num1,num2):
##    min=num1 if num1<num2 else num2
##    i=2
##    while i<min+1:
##        if num1 % i ==0 and num2%i==0:
##            factor=i
##            break
##            i+=1
##    print(i)
##    return factor
##def inser():
##    return int(input("enter the numbers : "))
def main():
    val1=int(input("enter 1: "))
    val2=int(input("enter 2: "))
    min=val2 if val2<val1 else val1
    print(5%2)
    i=1
    while i < min+1:
        if val2 % i == 0 :
            if val1 % i == 0:
                if i==1: i+=1
                print("the comon factor of ",val1," and ", val2," is : ",i)
        i+=1
 #   print("the greatest common divisor of the two is : ", val1 , "*",g," or ", val2,"*",g,"  which is ", val1*gcd(val1,val2))

main()
