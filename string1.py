#finding the number of girls in a company using endswith() method
emp=["rajesh","varuna","santhi","sruthi","megha"]
result=[]
for i in emp:
    if i.endswith("i") or i.endswith("a"):
        result.append(i)
print(result)
print(len(result))