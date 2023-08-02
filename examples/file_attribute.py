'''
File attributes
'''
print "File operation"
fd=open('anilTest.py','w')
print "Name of file:",fd.name
print "Mode of File:",fd.mode
print "Before :",fd.closed
if not fd.closed:
     fd.close()
print "file is closed or not:",fd.closed
