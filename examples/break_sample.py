str1='python'
try:
    for i in str1:
        if i == 'o':
           print "I am breaking"
           break
        else:
           print i
except:
    pass   
print "Below the break"
for j in range(3):
    print j