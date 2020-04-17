l=[5,3,0,1,2]
flag=0
z=len(l)
while flag==0:
    flag=1
    for x in range (z-1):
        
        if l[x]>l[x+1]:
           flag=0
           t=l[x]
           l[x]=l[x+1]
           l[x+1]=t
print (l)        