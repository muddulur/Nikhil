def sum(n):

    if n<=1:

        return n

    else:

        return n+sum(n-1)

num=int(input("enter the number:"))

if num<=0:

    print("enter the positive number:")

else:

    print("the sum of natural numbers is: ",sum(num))
