st=input("enter a string\n")

l=[0 for x in range(26)]
for x in range(len(st)):
    l[ord(st[x])-97]+=1

for x in range(26):
    if l[x]!=0:
        print(chr(x+97),"=",l[x])