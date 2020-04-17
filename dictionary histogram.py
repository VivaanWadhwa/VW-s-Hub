s="abracadabra"
d={}
z=len(s)
for x in range (z):
    d[s[x]]=0
for x in range (z):
    d[s[x]]+=1    
print (d)    
    
    