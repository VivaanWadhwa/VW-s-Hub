s=input("Enter Sentence \n")
s1=""
l=[]
z=len(s)
d={}
for x in range (z):
    if ord(s[x])==32 and len(s1) not in d:
        a=len(s1)
        l.append(s1)
        s1=''
        d[a]=l
        l=[]
    elif ord(s[x])!=32:
        s1+=s[x]
    elif ord(s[x])==32 and len(s1) in d:
        a=len(s1)
        l.append(s1)
        s1=''
        d[a]+=l
        l=[]
l.append(s1)
if len(s1) in d:
     d[len(s1)]+=l
else:
     d[len(s1)]=l          
print (d)        
            
        