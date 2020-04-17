l=[]
a=int(input('enter a number:'))
while a!=0:
    r=a%8
    l.append(r)
    a=a//8
f=[]
for x in range(len(l)-1,-1,-1):
    f.append(l[x])
print(f)