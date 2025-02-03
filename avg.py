height=input("Enter the heights of persons separated by comma: ")
hlist=height.split(',')
#print(hlist)
heights=[]
count1=0
count2=0
for i in hlist:
    h=int(i)
    heights.append(h)
print("The heights of persons are:",heights)
for j in heights:
    count1=count1+j
print("The sum of the heights are:",count1)
for k in heights:
    count2=count2+1
print("The number of heights are:",count2)
print("The average is:",round(count1/count2))

