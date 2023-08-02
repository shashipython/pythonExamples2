
def fib_gen(n):
#fib 0,1,1,2,3,5...
    l=[0,1]
    for i in range(2,n):
        fib=l[i-1]+l[i-2]
        l.append(fib)
    return l

n=input("Enter Number")
l=fib_gen(n)
print "Fib List:",l