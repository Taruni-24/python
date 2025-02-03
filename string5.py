s="python is the good programming language"
f=s.split()
print(f)
n=[]
for i in f:
    if i=="is": 
        i="are"
    n.append(i)
f=" ".join(n)
print(f)
