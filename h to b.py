st=input("enter a hexadecimal no.:")
s=0
y=-1
for x in range(len(st)-1,-1,-1):
    y+=1
    if ord(st[y])>=48 and ord(st[y])<=57:
        s+=(16**x)*(ord(st[y])-48)
    elif ord(st[y])>=65 and ord(st[y])<=70:
        r=10+ord(st[y])-65
        s+=(16**x)*r
l=[]
while s!=0:
    r=s%2
    l.append(r)
    s=s//2
f=[]
for x in range(len(l)-1,-1,-1):
    f.append(l[x])
print(f)