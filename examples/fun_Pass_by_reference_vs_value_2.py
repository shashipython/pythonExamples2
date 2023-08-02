#!/usr/bin/python

# Function definition is here
def changeme( mylist1 ):
   "This changes a passed list into this function"
   mylist1=[1,2,3,4]; # This would assig new reference in mylist
   print "Values inside the function: ", mylist1
   return

# Now you can call changeme function
mylist = [10,20,30];
changeme( mylist );
print "Values outside the function: ", mylist