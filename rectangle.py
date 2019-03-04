value=eval(input('type the height of the triangle : '))
row=0
while row<value:
    count=0
    while count<row:
        print(end="")
        count+=1
    count=0
    while count<value:
        print(end="*")
        count+=1
    print()
    row+=1
