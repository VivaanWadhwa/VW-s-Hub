l1=[1,2,3,4,50]
l2=[51,45,34,22,11,10]
l3=[]
x,b=len(l1),len(l2)
y=len(l2)-1
z=0
while y<b and z<x:
    if l1[z]>l2[y]:
        l3.append(l2[y])
        y-=1    
    else:
        l3.append(l1[z])
        z+=1
while y<b and y>-1:
  l3.append(l2[y])
  y-=1
while z<x:
    l3.append(l1[z])
    z+=1
print (l3)        
    
    
    