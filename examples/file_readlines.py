'''
File Readlines operation
'''

fd=open('test2.txt','r')
for line in fd.readlines():
	print "line:",line
fd.close()
