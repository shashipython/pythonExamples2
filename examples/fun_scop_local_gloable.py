#!/usr/bin/python
 # This is global variable.
# Function definition is here
def sum1( arg1, arg2 ):
   global total
   #total = 0;   
   # Add both the parameters and return them."
   total = arg1 + arg2; # Here total is local variable.
   print "Inside the function local total : ", total
   #return total;


# Now you can call sum function
sum1( 10, 20 )
print "Outside the function global total : ", total 