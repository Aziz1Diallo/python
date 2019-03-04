def keybord ():
    value=int(input("type value "))
    return value
def operatorCheck():
    op=input("type 'add' for addition or 'sub' for substraction    ")
    return op
def calc(a,b,operator):
    if operator=="add":
        res=a+b
        sign="+"
        return res,sign
    if operator=="sub":
        res=a-b
        sign="-"
        return res,sign
def Main():
    val1=keybord()
    val2=keybord()
    opera=operatorCheck()
    print(opera)
    result,sig=calc(val1,val2,opera)
    print(val1," ",sig," ",val2, " = ",result)
Main()
