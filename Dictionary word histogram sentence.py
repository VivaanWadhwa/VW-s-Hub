s="hello how are you"
s1=""
z=len(s)
d={}
for x in range (z):
    if ord(s[x])==32 and len(s1) not in d:
        a=len(s1)
        s1=""
        d[a]=1
    elif ord(s[x])!=32:
        s1+=s[x]
    elif ord(s[x])==32 and len(s1) in d:
        a=len(s1)
        s1=""
        d[a]+=1
d[len(s1)]+=1        
print (d)        
            
        