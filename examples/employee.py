class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary
	  
'''
Creating instance objects:

To create instances of a class, you call the class using class name and pass in whatever arguments its __init__ method accepts.
'''


"This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)

'''
Accessing attributes:

You access the object's attributes using the dot operator with object
'''


emp1.displayEmployee()
emp2.displayEmployee()
print "Total Employee %d" % Employee.empCount