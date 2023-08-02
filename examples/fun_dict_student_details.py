def student_details(name,*marks,**details):
    print "="*20
    print "     Student Details     "
    print "="*20
    print "Name:",name
    total=0
    for i in marks:
	total+=i
    print "type:",type(details)
    for k,v in details.items():
	print k,":",v
    print "Marks:",total
    print "="*20

student_details('Rama',35,45,56,age=20,add="BTM",contact=999888)
