def ver1(x):
    if x == {"a","b","c","d","e"}:
        print("Correct!")
        return
    else:
        print("Incorrect")
        return
def hint1():
    print("Are you writing each letter as a string? Strings can be written with ''.")
    return
def ver2(A,B,C,D):
    if A == {2,3,4,5} and B == {3,4,5,6,7,8,9} and C == {2,3,4,5,6,7,8,9} and D == {3,4,5}:
        print("Correct!")
        return
    else:
        print("Incorrect")
        return
def hint2():
    print("Make sure you are calling methods on these sets. This means you need to call the method A.union(B), rather than union(A,B).")
    return
def ver3(x,y):
    if x == [1,2,3,4,5] and y == 4:
        print("Correct")
        return
    else:
        print("Incorrect")
        return
def hint3():
    print("Make sure you are calling the number at the third index. This should be the integer 4.")
    return
def ver4(fruit):
    if fruit == ['banana','blackberry','grapefruit','pineapple','strawberry','guava']:
        print("Correct")
        return
    else:
        print("Incorrect")
        return
def hint4():
    print("Make sure you are performing the actions in the same order as the exercise.")
    return
def ver5(lst1,lst2,lst3):
    x1 = ["Boston", "Kansas City", "Paris", "Manhattan"]
    x2 = ["Paris", "Manhattan", "Tokyo"]
    x3 = ["London", "Springfield", "Boston", "Kansas City", "Paris"]
    if (lst1, lst2, lst3) == (x1, x2, x3):
        print("Correct")
        return
    else:
        print("Incorrect")
        return
def hint5():
    print("Remember lists start at 0.")
    print("Remember that the entry on the left side of : is included but the one on the right is not inluded.")
    return
def ver6(x):
    y = [12,9,6]
    if x == y:
        print("Correct")
        return
    else:
        print("Incorrect")
        return
def hint6():
    print("Remember that the first entry of the slice will be included, the second entry will not. Make sure you start with a number divisible by 3.")
    print("In the third entry of the slice method, we want a -3 to descend and increment by 3.")
    return
def ver7(x,y,sum,tup):
    x1 = 3
    y1 = 4
    sum1 = 7
    tup1 = (x,y,sum)
    if x1 == x and y1 == y and sum1 == sum and tup1 == tup:
        print("Correct")
        return
    else:
        print("Incorrect")
        return
def hint7():
    print("Make sure you are defining x and y appropriately. It should look something like \n\nx,y = pair")
    return
def ver8(dictionary, keys):
    dictionary1 = {2:7,3:4,4:5,5:0}
    keys1 = dictionary1.keys()
    if dictionary == dictionary1 and keys == keys1:
        print("Correct")
        return
    else:
        print("Incorrect")
        return
def hint8():
    print("Use the pop method to remove a key. Use the same syntax for updating or adding a new entry to the list.")
    return
def ver9(length):
    length1 = 23
    if length1 == length:
        print("Correct")
        return
    else:
        print("Incorrect")
        return
def hint9():
    print("Use the len function on the set.")
    return