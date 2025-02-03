l1=[10,20,30]
l2=[10,20,30]
print("Original Lists are: ")
print(l1)
print(l2)
result=map(lambda x,y:x+y,l1,l2)
print(result)
print(list(result))