def printme(name,age=20):
    '''
    Thi is the function to print
    '''
    print "@ print me function"
    print "Hi i am in side function"
    print "Name :",name
    print "age :",age
    return

def test():
    print "@ test function "
    printme('Shiva',50)
    printme('Rama')
    
    
test()