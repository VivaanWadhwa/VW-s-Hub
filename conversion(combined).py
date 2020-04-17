choice='y'
print('Which type of conversion do you want:-\n1.binary to decimal\n2.binary to hexadecimal\n3.binary to octal\n4.decimal to binary\n5.decimal to hexadecimal\n6.decimal to octal\n7.hexadecimal to binary\n8.hexadecimal to decimal\n9.hexadecimal to octal\n10.octal to binary\n11.octal to decimal\n12.octal to hexadecimal')
while choice=='y' or choice=='Y':
    c=int(input('choice:'))
    if c==1:
        a=int(input('binary to decimal\nenter a binary no.:'))
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
    elif c==2:
        a=int(input('binary to hexadecimal\nenter a binary no.:'))
        r=0
        x=-1
        s=0
        while a!=0:
            x+=1
            r=a%10
            if r==1:
                s+=2**x
            a=a//10
        l=[]
        while s!=0:
            r=s%16
            if r>=10:
                ch='A'
                x=ord(ch)+r-10
                l.append(chr(x))
            elif r<10:
                l.append(r)
            s=s//16
        f=[]
        for x in range(len(l)-1,-1,-1):
            f.append(l[x])
        print(f)
    elif c==3:
        a=int(input('binar to octal\nenter a binary no.:'))
        r=0
        x=-1
        s=0
        while a!=0:
            x+=1
            r=a%10
            if r==1:
                s+=2**x
            a=a//10
        l=[]
        while s!=0:
            r=s%8
            l.append(r)
            s=s//8
        f=[]
        for x in range(len(l)-1,-1,-1):
            f.append(l[x])
        print(f)
    elif c==4:
        l=[]
        a=int(input('decimal to binary\nenter a number:'))
        while a!=0:
            r=a%2
            l.append(r)
            a=a//2
        f=[]
        for x in range(len(l)-1,-1,-1):
            f.append(l[x])
        print(f)
    elif c==5:
        l=[]
        a=int(input('decimal to hexadecimal\nenter a number:'))
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
    elif c==6:
        l=[]
        a=int(input('decimal to octal\nenter a number:'))
        while a!=0:
            r=a%8
            l.append(r)
            a=a//8
        f=[]
        for x in range(len(l)-1,-1,-1):
            f.append(l[x])
        print(f)
    elif c==7:
        st=input("hexadecimal to binary\nenter a hexadecimal no.:")
        s=0
        y=-1
        for x in range(len(st)-1,-1,-1):
            y+=1
            if ord(st[y])>=48 and ord(st[y])<=57:
                s+=(16**x)*(ord(st[y])-48)
            elif ord(st[y])>=65 and ord(st[y])<=70:
                r=10+ord(st[y])-65
                s+=(16**x)*r
        l=[]
        while s!=0:
            r=s%2
            l.append(r)
            s=s//2
        f=[]
        for x in range(len(l)-1,-1,-1):
            f.append(l[x])
        print(f)
    elif c==8:
        st=input("hexadecimal to decimal\nenter a hexadecimal no.:")
        s=0
        y=-1
        for x in range(len(st)-1,-1,-1):
            y+=1
            if ord(st[y])>=48 and ord(st[y])<=57:
                s+=(16**x)*(ord(st[y])-48)
            elif ord(st[y])>=65 and ord(st[y])<=70:
                r=10+ord(st[y])-65
                s+=(16**x)*r
        print(s)
    elif c==9:
        st=input("hexadecimal to octal\nenter a hexadecimal no.:")
        s=0
        y=-1
        for x in range(len(st)-1,-1,-1):
            y+=1
            if ord(st[y])>=48 and ord(st[y])<=57:
                s+=(16**x)*(ord(st[y])-48)
            elif ord(st[y])>=65 and ord(st[y])<=70:
                r=10+ord(st[y])-65
                s+=(16**x)*r
        l=[]
        while s!=0:
            r=s%8
            l.append(r)
            s=s//8
        f=[]
        for x in range(len(l)-1,-1,-1):
            f.append(l[x])
        print(f)
    elif c==10:
        a=int(input('octal to binary\nenter a octal no.:'))
        r=0
        x=-1
        s=0
        while a!=0:
            x+=1
            r=a%10
            s+=(8**x)*r
            a=a//10
        l=[]
        while s!=0:
            r=s%2
            l.append(r)
            s=s//2
        f=[]
        for x in range(len(l)-1,-1,-1):
            f.append(l[x])
        print(f)
    elif c==11:
        a=int(input('octal to decimal\nenter a octal no.:'))
        r=0
        x=-1
        s=0
        while a!=0:
            x+=1
            r=a%10
            s+=(8**x)*r
            a=a//10
        print(s)
    elif c==12:
        a=int(input('octal to hexadecimal\nenter a octal no.:'))
        r=0
        x=-1
        s=0
        while a!=0:
            x+=1
            r=a%10
            s+=(8**x)*r
            a=a//10
        l=[]
        while s!=0:
            r=s%16
            if r>=10:
                ch='A'
                x=ord(ch)+r-10
                l.append(chr(x))
            elif r<10:
                l.append(r)
            s=s//16
        f=[]
        for x in range(len(l)-1,-1,-1):
            f.append(l[x])
        print(f)
    else:
        print('invalid input')
    choice=input('do you want to continue converting:')
    
