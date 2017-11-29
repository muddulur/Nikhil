def fact(x):

    if x<=1:

        return x

    else:

        return x*fact(x-1)

entered=int(input("enter the num : "))

print("the factorial of given num is: ",fact(entered))
