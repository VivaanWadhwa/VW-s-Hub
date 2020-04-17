'''
WAP  to count the number of lines in a text file STORY.TXT
which are starting with an alphabet ‘A’.
'''
f=open("STORY.txt","w")
f.writelines(["Akfmfkmfr\n","afefrfrfr\n","A\n","Awswddwd\n","AAA"])
f.close()
f=open("STORY.txt","r")
a,counter=0,0
l=f.readlines()
f.close()
f=open("STORY.txt","r")
for n in range (len(l)):
    sentence=f.readline()
    if sentence[0]=="A":
        a+=1
    else:
        continue
print ("No of lines starting with A:%s" %a)
