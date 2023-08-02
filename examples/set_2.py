'''

Frozensets
Though sets can't contain mutable objects, sets are mutable:

cities = set(["Frankfurt", "Basel","Freiburg"])
>>> cities.add("Strasbourg")
>>> cities
set(['Freiburg', 'Basel', 'Frankfurt', 'Strasbourg'])

Frozensets are like sets except that they cannot be changed, i.e. they are immutable:


>>> cities = frozenset(["Frankfurt", "Basel","Freiburg"])
>>> cities.add("Strasbourg")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'frozenset' object has no attribute 'add'
>>>

'''

cities = frozenset(["Frankfurt", "Basel","Freiburg"])
cities.add("Strasbourg")
print "Cities :",cities
# Its gives the error not allow to add


adjectives = {"cheap","expensive","inexpensive","economical"}

print "Adjectives:",adjectives