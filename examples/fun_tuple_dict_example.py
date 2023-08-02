def fun(name,*marks,**details):
    total=0
    for i in marks: # 34,45,65
        total+=i
    print "="*20
    print "     Student Details     "
    print "="*20
    print "Name:",name
    for k,v in details.items():
        print k,":",v
    print "Total:",total
    print "="*20

fun('Rama',45,56,67,age=20,add="BTM",contact=999888)