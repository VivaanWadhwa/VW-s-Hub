a=int(input('enter a binary no.:'))
r=0
x=-1
s=0
while a!=0:
    x+=1
    r=a%10
    if r==1:
        s+=2**x
    a=a//10
l=[]
while s!=0:
    r=s%8
    l.append(r)
    s=s//8
f=[]
for x in range(len(l)-1,-1,-1):
    f.append(l[x])
print(f)