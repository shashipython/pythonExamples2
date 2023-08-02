'''Override class __str__ function'''

class MyMeta:
    def __str__(cls): 
       return "Beautiful class "

x = MyMeta()

print x