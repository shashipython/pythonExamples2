#!/usr/bin/python

import MySQLdb
def emp_update_details(name,lname,age,sex,income):
	# Open database connection
	db = MySQLdb.connect("localhost","root","moon01","test" )
	
	# prepare a cursor object using cursor() method
	cursor = db.cursor()
	# Prepare SQL query to INSERT a record into the database.
	sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
       LAST_NAME, AGE, SEX, INCOME) \
       VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
       (name,lname,age,sex,income)
	try:
	#	 Execute the SQL command
		cursor.execute(sql)
	# Commit your changes in the database
		db.commit()
	except:
	# Rollback in case there is any error
		db.rollback()

	# disconnect from server
	db.close()
	
#if __name__ == '__main__':
#name,lname,age,sex,income
fd=open('emp.txt','r')
#print ">>",fd.readlines()
for line in fd.readlines():
    l=line.split('|')
#	l=['Krisha',"Prasad",30,'M',2000]
    emp_update_details(l[0],l[1],int(l[2]),l[3],int(l[4]))
fd.close()