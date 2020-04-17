l=[]
a=int(input('enter a number:'))
while a!=0:
    r=a%16
    if r>=10:
        ch='A'
        x=ord(ch)+r-10
        l.append(chr(x))
    elif r<10:
        l.append(r)
    a=a//16
f=[]
for x in range(len(l)-1,-1,-1):
    f.append(l[x])
print(f) 