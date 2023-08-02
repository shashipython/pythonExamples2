fd=open('std.txt','r+')
print "Name of File:",fd.name
str1="This is the 6th Line\n"


fd.seek(0,2)
line=fd.write(str1)
fd.seek(0,0)
'''
for i in range(10):
    line = fd.next()
    print "%d --> %s"%(i,line.upper())
'''




try:
    for i in range(100):
	line = fd.next()
	print "%d --> %s"%(i,line.upper())
except:
    pass

fd.close()