import re 
str1="Name:Shiva Raghav Enni Age: 23 DOB: 12/01/1990"
r=re.compile('^Name:([\w\s]+)\s*Age\s*:\s*(\d+)\s*DOB\s*:\s*(\d{1,2}\/\d{1,2}\/\d{2,4})$')
t=r.search(str1)
if t:
	print "pattern Match"
	print "Group:",t.group(0)
	print "Name:",t.group(1)
	print "Age:",t.group(2)
	print "DOB:",t.group(3)
else:
    print "Match Not Found"


