from random import randrange

def randomList():
    liste=[]
    lenght = randrange(5, 15)
    for i in range(lenght):
        liste += [randrange(-10, 60)]
    return liste
def selectionSort(lst):
    for i in range(len(lst)):
        small = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[small]:
                small=j
        if i != small:
            lst[i], lst[small] = lst[small], lst[i]
def main():
    for n in range(5):
        col = randomList()
        print(col)
        selectionSort(col)
        print(col)
        print("==================================")
main()
