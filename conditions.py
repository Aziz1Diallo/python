name=input("what's your name? ")
age=eval(input("how old are you"))
like=input("choose one of the following: \nvideo games' -- 'beach' -- 'hunting'")
if age>0 and age <=10: # this is for kids
        if like=="video games": # that's the perfect choice
                print("cool! that right homie. We are going to have some fun! haha!")
        else : #in case he is an old man still playing games, he must be told to come down to reality.
                print("no no")
if age >10 and age <= 25: # teenagers
        if like=="beach" or like=="hunting":
                print("oh! pal! let's get the party started")
        else: print("What? get rid of that now")
if age>=26:
        if like =="hunting":
                print("hah! ")
        if like=="beach":
                print("not for you")
        else: print("no")
