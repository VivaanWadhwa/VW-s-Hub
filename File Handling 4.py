'''
WAP that copies all lines that start with uppercase letter from the first file
into the second file
'''
f=open("Stdin.txt","w")
f.writelines(["Akfmfkmfr\n","afefrfrfr\n","A\n","Awswddwd\n","AAA"])
f.close()
f=open("Stdin.txt","r")
l=f.readlines()
f.close()
f=open("Stdout.txt","w")
for x in range (len(l)):
    if ord(l[x][0])>64 and ord(l[x][0])<97:
        f.writeline(l[x])
    else:
        continue
f.close()
f=open("Stdout.txt","r")
print (f.read())
