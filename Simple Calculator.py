def add(a,b):

    c=a+b

    return c

def sub(a,b):

    c=a-b

    return c

def mul(a,b):

    c=a*b

    return c

def div(a,b):

    c=a/b

    return c

option_entered=int(input("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n"))

num1=int(input("enter the first number: ")


num2=int(input("enter the second number: ")

if option_entered == 1:

    print("the addition of two numbers is:",add(num1,num2))

elif option_entered == 2:

      print("the subtraction of two numbers is:",sub(num1,num2))

elif option_entered == 3:

    print("the multiplication of two numbers is:",mul(num1,num2))

elif option_entered == 4:

    print("the division of two numbers is:",div(num1,num2))

else:
    print("Invalid Option")
