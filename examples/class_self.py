'''Methods uses method attributes of the self argument'''
class Bag:
    def __init__(self):
        self.data = []
    def add(self, x):
        self.data.append(x)
    def addtwice(self, x):
        self.add(x)
        self.add(x)
    def printdata(self):
        print "List having:",self.data

a = Bag()

a.add(4)
a.addtwice(10)

a.printdata()