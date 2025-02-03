a=int(input("enter a number: "))
sum=0
for i in range(1,a+1):
    if a%i==0:
        sum=sum+i
if(a==sum):
    print("perfect number")
else:
    print("Not perfect number")