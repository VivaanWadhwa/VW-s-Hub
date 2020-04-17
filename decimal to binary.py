a=int(input("enter decimal digit"))
num=a
st=""
while num>0:
    st+=str(num%2)
    num=num//2
print (st)    

    
    
    