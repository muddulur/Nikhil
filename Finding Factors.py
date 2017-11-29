input_num=int(input("Enter the number to which factors are needed: "));

for i in range(1,input_num):

    factor=input_num%i;

    if factor == 0:

        print (i,"\t");

    else:

        continue;
