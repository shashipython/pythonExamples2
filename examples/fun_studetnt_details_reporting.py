def student_details():
	print "="*20
	print "     Student Details     "
	print "="*20
	for i in l:
		student_details_report(i)
	print "="*20
	
def student_details_report(details):    
	print 'Name:',details['name']
	print 'Age:',details['age']
	print 'Address:',details['add']
	print 'Contact:',details['contact']
		
def std_details_update():
	global l
	l=[]
	ent=True
	while ent:
	
		#std=raw_input("Enter Name,age,add,contact by giving one black space")
		#print ">>>std",std
		std_name=raw_input("Enter Name")
		std_age=raw_input("Enter Age")
		std_add=raw_input("Enter Addtree")
		std_contact=raw_input("Enter Contact")
		#std_name,std_age,std_add,std_contact=std.split('')
		l.append({'name':std_name,'age':std_age,'add':std_add,'contact':std_contact})
		ent=raw_input("Do you wnat to enter std details--Yes/no")
		if ent in ['Yes','Y',"yes","y"]:
		    ent=True
		else:
		    break
std_details_update()
student_details()
