num=input("Enter the numbers separated with comma: ")
num_list=num.split(',')
l=[]
#print(num_list)
for i in num_list:
    h=int(i)
    l.append(h)
print(l)
#print(max(l))
max=l[0]
for j in l:
    if j>max:
        max=j
print("Maximum number is: ",max)

