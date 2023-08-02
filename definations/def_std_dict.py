def std_details(name,**std_dict):
    print "Student Name :",name
    for k,v in std_dict.items():
        print k,":",v
        

std_details("Shiva",age=10, \
            clas=2, \
            address="BTM" )