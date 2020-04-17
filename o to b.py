a=int(input('enter a octal no.:'))
r=0
x=-1
s=0
while a!=0:
    x+=1
    r=a%10
    s+=(8**x)*r
    a=a//10
l=[]
while s!=0:
    r=s%2
    l.append(r)
    s=s//2
f=[]
for x in range(len(l)-1,-1,-1):
    f.append(l[x])
print(f)