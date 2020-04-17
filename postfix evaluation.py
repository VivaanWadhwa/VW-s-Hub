def push(l,x):
    l.append(x)
def pop(l):
    z=len(l)
    return l.pop(z-1)
    l.pop(z-1)
def display(l):
    return l
l_exp=[5,6,9,'+',80,5,'*','-','/']
l=[]
for ch in range (len(l_exp)):
    if l_exp[ch] in ['(',')','^','/','*','%','+','-']:
        temp1=pop(l)
        temp2=pop(l)
        if l_exp[ch]=='+':
            push(l,temp2+temp1)
        elif l_exp[ch]=='-':
            push(l,temp2-temp1)
        elif l_exp[ch]=="*":
            push(l,temp2*temp1)
        elif l_exp[ch]=='/':
            push(l,temp2/temp1)
    else:
        push(l,l_exp[ch])
        
            
            
    