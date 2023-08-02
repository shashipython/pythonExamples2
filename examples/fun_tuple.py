def fun(name,*marks):
    print "type:",type(marks)
    total=0
    for i in marks:
        total+=i
    print "="*20
    print "     Student Details     "
    print "="*20
    print "Name:",name
    print "Total:",total
    print "="*20

fun('Rama',45,56,67,100)