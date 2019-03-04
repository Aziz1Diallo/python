def main():
    data=[19, 20, 34, 56, 189]
    print(data[-1])
    print(data[0])
    print(data[-len(data)])
    print(data[-3])
    print('...................')
    for i in range(-1, -len(data) -1, -1):
        print(data[i], end='  ')
    print()

    print('..........................')
    for i in range(len(data)):
        print(data[i], end='  ')
    print()
    print('..........................')
    for i in range(len(data)-1,-1,-1):
        print(data[i], end='   ')
    print()
    segment=data[2:4]
    print(segment)

    
def triangle():
    tri=['*']*10
    for i in range(len(tri)):
        print(tri[0:i], sep='  ')
    #print()
    for i in range(len(tri)):
        print(tri[i:len(tri)],sep='  ')
main()

