a=int(input("enter a number: "))
c=0
for i in range(1,a+1):
    if a%i==0:
        c=c+1
print(c)
if(c==2):
    print("prime number")
else:
    print("Not prime number")