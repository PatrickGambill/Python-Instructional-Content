def ver1(sum):
    if sum == 1501500:
        print("Correct!")
        return
    else:
        print("Incorrect")
        return
def hint1():
    print("Remember to increment the loop in 3s. Also make sure that the last element is 3001, as it will not be included.")
    return
def ver2(product):
    if product == 43049123460000:
        print("Correct!")
        return
    else:
        print("Incorrect")
        return
def hint2():
    print("Make sure that you are multiplying the old product by each number in the set. You need to update product with each iteration.")
    return
def ver3(fact):
    if fact == 40320:
        print("Correct!")
        return
    else:
        print("Incorrect")
        return
def hint3():
    print("To compute n! (n factorial), you need to take the product of all positive integers less than or equal to n. For example, 3! = 1*2*3.")
    print("If your value goes above 10,000 inside of the while loop, it will not break until after the iteration. Make sure you are not returning the first factorial larger than 10,000.")
    return