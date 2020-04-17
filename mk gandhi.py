st=input("enter name\n")
spaces=0
st2=""
j=0
for k in st:
 if ord(k)==32:
       j+=1
for x in st:
 st2+=x
 z=ord(st2[0])
 z-=32
 if x==" ":
    spaces+=1
    print(chr(z),end="")
    if spaces<=j:
       print(".",end=" ")
       st2=""

print (st2,end="")
        
        