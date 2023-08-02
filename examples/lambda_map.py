'''
map
 map() applies the function func to all the elements of the sequence seq. It returns a new list with the elements changed by func

'''


def fahrenheit(T):
    return ((float(9)/5)*T + 32)
def celsius(T):
    return (float(5)/9)*(T-32)
temp = (36.5, 37, 37.5,39)

F = map(fahrenheit, temp)
C = map(celsius, F)

print "Celsius:",C


