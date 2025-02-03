p=int(input("Enter the priciple amount: "))
r=int(input("enter the rate of interest: "))
t=int(input("enter the time period: "))
#compound interest = p(1+r/100)**t - p
d=(p*(1+(r/100))**t)-p
print(d)
