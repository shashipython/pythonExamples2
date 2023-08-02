def printme(name,*marks):
    sum1=0
    for i in marks[0]:
        sum1=sum1+i
    return sum1

def test():
    name=raw_input("Enter the number a:")
    mlist=[];i=0
    while(i<5):
        marks=input("Enter the number a:")
        mlist.append(marks)
        i=i+1
        
    sum1=printme(name,mlist)
    print "Name : %s Marks : %d" %(name,sum1)
    
    
test()