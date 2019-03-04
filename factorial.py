'''agsag
agsfga
agfag
'''
def facto(n):
    if n==0:
        return 1
    else: return n * facto(n-1)

def main0():
    ''' gsousgj
            skj dsogsd
            adfkja;
    '''
    print("0! = ",facto(0))
    print("4! = ",facto(4))
def sum1(n):
    s=0
    while n > 0:
        s += 1n -= 1
    return s
val = 0
def sum2():
    s=0
    while val > 0:
        s += 1
        val -= 1
    return s
def sum3():
    s=0
    for i in range(val, 0, -1):
        s += 1
    return s
def maina():
    global val
    val = 5
    print(sum1(input))
    print(sum2())
    print(sum3())
def main1():
    global val
    val = 5
    print(sum1(input))
    print(sum3())
    print(sum2())
def main2():
    global val
    val = 5
    print(sum2())
    print(sum1(input))
    print(sum3())
