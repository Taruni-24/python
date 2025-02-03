size=input("Enter the size of the pizza(S/M/L)?")
bill=0
if size=='s' or size=="S":
    bill+=100
    print("The cost of small pizza is 100")
elif size=="m" or size=="M":
    bill+=200
    print("The cost of medium pizza is 200")
elif size=="l" or size=="L":
    bill+=300
    print("The cost of large pizza is 300")

addpepper=input("Do you want to add peppor(Y/N)?")
if addpepper=="y" or addpepper=="Y":
    if size=="s" or size=="S":
        bill+=30
    else:
        bill+=50
extracheese=input("Do you want extra cheese(Y/N)?")
if extracheese=="y" or extracheese=="Y":
    bill+=20
print(f"Your bill is {bill}")
