n=int(input("enter the number:"))
fact=1
if(n<0):
    print("factorial does not exixt for negative numbers")
elif(n==0):
    print("the factorial of 0 is 1")
else:
    for i in range(1,n+1):
        fact=fact*i
    print(fact)
