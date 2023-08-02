'''
Sets
A set contains an unordered collection of unique and immutable objects.
The set data type is, as the name implies, a Python implementation of the sets as they are known from mathematics.
This explains, why sets unlike lists or tuples can't have multiple occurrences of the same element.

Creating Sets

x = set("A Python Tutorial")

'''

x = set("A Python Tutorial")
#set(['A', ' ', 'i', 'h', 'l', 'o', 'n', 'P', 'r', 'u', 't', 'a', 'y', 'T']) 

#to find the type

print "Type:",type(x)


x = set(["Perl", "Python", "Java"])
#set(['Python', 'Java', 'Perl'])

# If we uses the tuple in the set
cities = set(("Paris", "Lyon", "London","Berlin","Paris","Birmingham"))

#duplicate elements that will remove and make a set
#set(['Paris', 'Birmingham', 'Lyon', 'London', 'Berlin'])


#----------------------------------------------------------------------------------------
'''
Immutable Sets
Sets are implemented in a way, which doesn't allow mutable objects.

ities = set((("Python","Perl"), ("Paris", "Berlin", "London")))
>>> cities = set((["Python","Perl"], ["Paris", "Berlin", "London"]))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'

'''
cities = set((("Python","Perl"), ("Paris", "Berlin", "London")))
print "cities:",cities
cities = set((["Python","Perl"], ["Paris", "Berlin", "London"]))

