'''st=input('enter a binary no.:')
s=0
y=-1
for x in range(len(st)-1,-1,-1):
    y+=1
    if ord(st[y])==49:
        s+=2**x
    else:
        s+=0
print(s)'''
a=int(input('enter a binary no.:'))
r=0
x=-1
s=0
while a!=0:
    x+=1
    r=a%10
    if r==1:
        s+=2**x
    a=a//10
print(s)