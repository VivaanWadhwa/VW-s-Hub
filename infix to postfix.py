def push(l,x):
    l.append(x)
def pop(l):
    z=len(l)
    return l.pop(z-1)
    l.pop(z-1)
def display(l):
    return l
infix="a+b-(a/b*d)"
l=[]
operators={'(':4,')':4,'^':3,'*':2,'/':2,'%':2,'+':1,'-':1}
exp=[]
z=len(infix)
for ch in range (z):
    if infix[ch] in ['(',')','^','/','*','%','+','-']:        
        if len(l)>=1:
            if operators[l[len(l)-1]]==operators[infix[ch]]:
                temp=pop(l)
                exp.append(temp)  
            elif infix[ch]==")":
                for x in range(len(l)):
                    if l[x]=="(":
                        n=x
                for x in range (n+1,len(l)):
                    temp=pop(l)
                    exp.append(temp)
                    l.pop(n)
        push(l,infix[ch])   
    else:
        exp.append(infix[ch])
for x in range (len(l)):
    if l[x]==')':
        l.pop(x)                
        continue
    else:
        exp.append(l[x])