def ver1(x):
    if x == 16:
        print("Correct!")
        return
    else:
        print("Incorrect")
        return
def hint1():
    print("Make sure you don't have any typos in your variable name. Your variable should be called number and it should be equal to 16.")
    return
def ver2(x1,x2,x3,x4,x5):
    y = [x1,x2,x3,x4,x5]
    if y == [True,False,True,False,True]:
        print("Correct!")
        return
    else:
        print("Incorrect")
        return
def hint2():
    print("Make sure you are capitalizing True and False.")
    return
def ver3(x):
    y = 3**20 - (6*3)/(7+3.2)
    if x == y:
        print("Correct!")
        return
    else:
        print("Incorrect")
        return
def hint3():
    print("Remember a^b is represented as a**b and remember to put your denominator in parentheses before dividing.")
def ver4(x):
    if x == "African or European swallow?":
        print("Correct!")
        return
    else:
        print("Incorrect")
        return
def hint4():
    print('Your string needs to be "African or European swallow?"')
    return
def var():
    return [1,2,3]
def ver6(x):
    if x == type([1,2,3]):
        print("Correct!")
        return
    else:
        print("Incorrect")
        return
def hint6():
    print("Make sure you are setting y = type(var). This will store the type of var as y.")
    return