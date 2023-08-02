
def std_report(name,*marks,**details):
	st="="*20 # ======================
	fd=open('aaa.txt','w')
	total=0
	for i in marks:
		total+=i
	fd.write(st+'\n')
	fd.write("     Student Details     \n")
	fd.write(st+'\n')
	fd.write("Name:%s\n"%name)
	for k,v in details.items():
		fd.write("%s :  %s\n"%(k,str(v)))
	fd.write("Total:%s\n"%total)
	fd.write(st)
	fd.close()

std_report('Rama2',45,56,67,age=20,add="BTM",contact=999888)
'''
while c==True:
	str_opt="""
	1.Add Student Details
	2.Add Student Marks and sem details
	3.Sudent Report
	4.Complete Sutunedts report
	5.Delete a record
	""""
	print str_opt
	opt=input("Enter tthe opt")
	if opt==1:
		std_add_fun()
	elif opt==2:
		std_marks_fun()
	elif opt==3:
		std_report()

Regular expression 
os,random,math,time,cal,sys
'''