def hello():
    print("hi")


def bye():
    print("bye")
    
def total():
    numbers = [1,2,3,4,5,1,4,5]
    Sum = sum(numbers)
    average= Sum/len(numbers)
    print (average)


print(hello())
print(total())
