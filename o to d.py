a=int(input('enter a octal no.:'))
r=0
x=-1
s=0
while a!=0:
    x+=1
    r=a%10
    s+=(8**x)*r
    a=a//10
print(s)