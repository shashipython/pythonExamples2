#!/usr/bin/python
import re
phone = "2004-959-595 shi #This is Phone Number"

# Delete Python-style comments
num = re.sub(r'#.*$', "", phone)
print "Phone Num : ", num

# Remove anything other than digits
num = re.sub(r'\D', " ", phone)
print "Phone Num : ", num