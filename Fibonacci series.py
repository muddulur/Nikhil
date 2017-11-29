def fib_series(x):

    if x<=1:

        return x;

    else:

        return (fib_series(x-1)+fib_series(x-2));

no_of_steps=int(input("enter the no of steps you want to see the fib series: "));

for i in range(no_of_steps):

    print(fib_series(i));