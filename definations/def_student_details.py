def std_details(reg,name,*marks,**std_dict):
    total=0
    for i in marks:
        if i > 35:
            result="P"
        else:
            result="F"
        total=total+i
        std_total_dict[reg]={'Name':name,"Marks":total,'result':result}
        for k,v in std_dict.items():
            std_total_dict[reg].update({k:v})
    
def std_report():
    print "="*40
    print "This is program to sum :"
    print "="*40 
    print "| Reg |  Name  |  age  |  address  | \
    contact  |  result  |  Marks  |"
    print "="*40
    for k,v in std_total_dict.items():
        print "| ",k," |  ",v['Name'],"  |  ",v['age'], \
        "  |  ",v['address'],"  |  ",v['contact'],"  |  ", \
        v['result'],"  |  ",v['Marks'],""
    
    print "="*40
          
    
def sudent_detail_collection(n):
    i=1
    while i<n:
        print i
        reg=i
        name=raw_input("Enter the name of student:")
        age1=raw_input("Enter the age of student:")
        contact1=raw_input("Enter the contact of student:")
        address1=raw_input("Enter the Address of student:")
        print "Enter the Marks details:"
        maths=input("Enter the Maths Marks:")
        social=input("Enter the Social Marks:")
        english=input("Enter the English Marks:")
        std_details(reg,name,maths,social,english,age=age1,contact=contact1, \
                    address=address1)
        i=i+1
        
        



global std_total_dict
std_total_dict ={}

print "Student Details:"
sudent_detail_collection(3)
print "Student afer: ",std_total_dict

std_report()