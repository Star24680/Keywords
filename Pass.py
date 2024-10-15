for X in range(10):
    if X%20==0:
        print(X)
        print("Twist")
    elif X%15==0:
        print(X)
        pass
    elif X%5==0:
        print(X)
        print("Fizz")
    elif X%3==0:
        print(X)
        print("Buzz")
    else:
        print (X)