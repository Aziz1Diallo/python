class Employee:
    def __init__(self, name, matri, pay):
        self.name=name
        self.id= matri
        self.salary = pay

def open_database(dataFile, db):
    lines = open(dataFile.dat)
    for line in lines:
        name, matri, pay = eval(line)
        db.append(Employee(name, id, salary))
    lines.close()
    return True

def print_database(db):
    for rec in db:
        print(str.format(" { : > 5 }:  { :<10}  { :>6.2f}", \
                         rec.id, rec.name, rec.salary))


def less_than_byName(e1, e2):
     return e1.name < e2.name

def less_than_byID(e1, e2):
    return e1.id < e2.id

def less_than_bySalary(e1, e2):
    return e1.salary < e2.salary

def sort(db, comp):
    n = len(db)
    for i in range (n -1):
        small= i;
        for j in range(i +1, n):
            if comp(db[j], db[small] ):
                small = j
        if small != i :
            db[i], db[small] = db[small], db[i]

def main():
    database = []

    if open_database ("dataFile.dat", database):
        print("-----Unsorted : ")
        print_database(database)

        #SORT BY NAME
        sort(database, less_than_byName)
        print("------Ordered by Name : ")
        print_database(database)

        #SORT BY ID
        sort(database, less_than_byID)
        print("------Ordered by ID : ")
        print_database(database)

        #SORTED BY SALARY
        sort(database, less_than_bySalary)
        print("------Ordered by Salary : ")
        print_database(database)
    else:
        print("could not open database file")
main()
