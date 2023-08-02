fd=open("test2.txt",'r')
p=fd.readlines()
print "fd.readlines():",p
for line in p:
    print "line:>",line
fd.close()