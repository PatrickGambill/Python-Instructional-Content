def gen1():
    return [12,4,76,25,6767,43,9,122,4,2,32323,232,4353,2]
def ver1(prod):
    if prod == 15218438984975286510796800:
        print("Correct!")
        return
    else:
        print("Incorrect")
        return
def hint1():
    print("You will need to use a for loop over an iterable inside of this function. If you are stuck, reference the previous lesson.")
    return
def ver2(sum):
    if sum == 7626:
        print("Correct!")
        return
    else:
        print("Incorrect")
        return
def hint2():
    print("Make sure you have a base case. If you are stuck look at the syntax for the factorial function. This is very similar.")
    return
def ver3(lst):
    if lst == [3, 6, 9, 15, 18, 21, 27, 30, 33, 39, 42, 45, 51, 54, 57, 63, 66, 69, 75, 78, 81, 87, 90, 93, 99, 102, 105, 111, 114, 117, 123, 126, 129, 135, 138, 141, 147, 150, 153, 159, 162, 165, 171, 174, 177, 183, 186, 189, 195, 198, 201, 207, 210, 213, 219, 222, 225, 231, 234, 237, 243, 246, 249, 255, 258, 261, 267, 270, 273, 279, 282, 285, 291, 294, 297]:
        print("Correct!")
        return
    else:
        print("Incorrect")
        return
def hint3():
    print("To test divisibility, we can use the modulo operator, %. If a number x is divisible by 12, then x % 12 will be 0.")
    return
def ver4(lst):
    if lst == [9, 36, 81, 144, 225, 324, 441, 576, 729, 900, 1089, 1296, 1521, 1764, 2025, 2304, 2601, 2916, 3249, 3600, 3969, 4356, 4761, 5184, 5625, 6084, 6561, 7056, 7569, 8100, 8649, 9216, 9801]:
        print("Correct!")
        return
    else:
        print("Incorrect")
        return
def hint4():
    print("The order matters. Filter first, then map. It will probably be easier to create a list for the filter and a list for the map. Also make sure you are wrapping the filter and the map in a list function.")
    return