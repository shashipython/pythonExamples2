import re
line="Cats are smarter the dogs"
#line="     smarter the Cats"
# Example Match
matchobj=re.match(r'.+(are)\s+(smart).*',line,re.M|re.I)
print "====",matchobj
if matchobj:
    print "Found",matchobj.group(0),matchobj.group(2)   
else:
    print "Not Found"
    
#Example for search
matchobj1=re.search(r'dogs',line,re.M|re.I)
if matchobj1:
    print "Found Search",matchobj1.group()
else:
    print "Not found"
    
#Example for compile
reg=re.compile(r'(\w+).*$',re.I|re.M)
print "reg :",reg
matchobj2=reg.search(line)
print "===",matchobj2
if matchobj2:
    print "MAtch found:",matchobj2.group(1)
else:
    print "Not match found"
    
