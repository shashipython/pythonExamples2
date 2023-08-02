try:
	fd=open('test.txt','w')
	fd.write('Hi its me')
except IOError:
    print "Error: cont find the file"
else:
	print "Writen done"
	fd.close()	