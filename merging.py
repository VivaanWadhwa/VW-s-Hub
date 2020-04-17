l1=[1,2,3,4,50]
l2=[9,10,11,12,13,14,15]
l3=[]
x,b=len(l1),len(l2)
y=0
z=0
while y<b and z<x:
    if l1[z]>l2[y]:
        l3.append(l2[y])
        y+=1
    elif l1[z]<l2[y]:
        l3.append(l1[z])
        z+=1
while y<b:
  l3.append(l2[y])
  y+=1
while z<x:
    l3.append(l1[z])
    z+=1
print (l3)        
    
    
    