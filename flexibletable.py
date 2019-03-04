max = 18
print(end=" ")
for column in range(1, max+1):
    print(end=" %2i " % column)
print()
print(end="     +")
for column in range(1, max+1):
    print(end="----")
print()
for row in range(1, max+1):
    print(end="%2i  |  " % row)
    for column in range(1, max+1):
        product=row*column;
        print (end="%3i  " % product)
    print()
