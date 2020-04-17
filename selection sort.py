l=[5,3,0,1,2,8]
z=len(l)
for x in range (z):
    sm,pos=l[x],x
    for y in range (x,z):
        if l[y]<sm:
            sm=l[y]
            pos=y
    s=l[x]
    l[x]=l[pos]
    l[pos]=s
print (l)        