c=1
l=[]
p="="*30
n=raw_input("Enter number how many std ")
while c<int(n):
    name=raw_input("Enter Name")
    age=raw_input("Enter Age")
    l.append({'Name':name,"Age":age})
    c=c+1
    
print p
print "        Std Details      "
print p
for i in l:
    print i['Name']
    print i['Age']
    