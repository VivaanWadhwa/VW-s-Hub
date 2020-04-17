list1=[2,13,-1,-5,8,5]
z=len(list1)
if list1[0]>0:
        for c in range (z):
            if list1[c]<0:
                for y in range (c,-1,-1):
                                     t=list1[y]
                                     list1[y]=list1[y-1]
                                     list1[y-1]=t
                                     break
for x in range (z-1):
       if list1[x]>0:
              if list1[x+1]>0:
                       continue
              else:
                 t=list1[x]
                 list1[x]=list1[x+1]
                 list1[x+1]=t
       elif list1[x]<0:
            if list1[x+1]<0:
                 continue
            else:
                 t=list1[x]
                 list1[x]=list1[x+1]
                 list1[x+1]=t
print (list1)                              