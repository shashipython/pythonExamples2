'''
   10 * (1/0)
Traceback (innermost last):
File "<stdin>", line 1
ZeroDivisionError: integer division or modulo
'''
try:
    #p=10 *(1/0)
    #p=1+"hh"
    print "Value of p:",p
except TypeError:
    print "Yes i am in Type Error Block"
except NameError:
    print "Yes i am in Name Error Block"
except ZeroDivisionError:
    p=10*(1/2.0)
    print "Got an exceptrion "
    print "Value is",p
    
    
    
    
    