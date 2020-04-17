l=[]
l1=[]
for x in range (1,101):
    l.append(x)
a=int(input("enter number to be found"))
v=len(l)
j=0
while v>1:
  z=len(l)  
  if z%2>0:
    b=z/2
    if l[b]>a:
        x=l[b]
        l1=[]
        for i in range (x):
            l1.append(l[i])
            l=[]
            l.append(l1)

print (l)
            