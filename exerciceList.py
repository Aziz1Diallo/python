def cop (a):
    copy=[]
    q=0
    for q in a:
        copy+=[q]
    return copy


def invers(a):
    inv=[]
    r=0
    for r in a:
        inv[r]=-a[r]
    return inv


def main():
    lstori=[2, 4, 6, 8, 10]
    target1= lstori[:] +  [10,12,14,16,18,20]
    print('[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]     ')
    for i in range(len(target1)):
        print( target1[i],end=' ')
    print()
    copy= cop(lstori)
    copyInv=invers(lstori)
 #   target2 = copy[::-1] + lstori
    print('[-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10]   ')
    for j in range(len(copy)):
       print( copy[j], end="  ")
    print()
    target3 = (lstori[0:1] + [3]) + (lstori[1:2] +[ 5]) + (lstori[2:3] + [7]) + lstori[3:4]
    print('[2, 3, 4, 5, 6, 7, 8, 10]    ')
    for k in range(len(target3)):
        print(target3[k], end="  ")
    print()
    target4= (lstori[0:2] + ['a', 'b','c']) + (lstori[1:2] + [5]) + lstori[3:4]
    print('[2, 4, 6, ’a’, ’b’, ’c’, 8, 10]     ')
    for l in range(len(target4)):
        print(target4[l], end="  ")
    print()
##    target5=lstori[0:0]
##    view(target5)
##    target6=lstori[-1:0]
##    view(target6)
##    target7=lstori[0:2]
##    view(target7)
##    target8=lstori[2:4]
##    view(target8)
##    target9 = lstori[0] + lstori[4]
##    view(target9)
##    target10= lstori[1:3]
##    view(target10)
main()
    
