def std_details(name,*marks,**std_dict):
    print "Student Name :",name
    for k,v in std_dict.items():
        print k,":",v
        
    total=0    
    for i in marks:
        total=total+i
    print "Total Marks: ",total
        

std_details("Shiva",30,40,45,age=10, \
            clas=2, \
            address="BTM" )