l=[5,3,1,0,2]
m=len(l)
for x in range(1,m):
   t=l[x]
   j=x-1
   if l[x]<l[j] and j>=0:
       l[x]=l[j]
       l[j]=l[x-2]
       l[x-2]=t
print(l)