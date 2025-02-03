a=[1,2,3,4,5,1,4]
b=a.copy()
a.append(9)
print(a)
print(b)
print(id(a))
print(id(b))