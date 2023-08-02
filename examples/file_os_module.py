import os

print "Current Directory:",os.getcwd()
scriptPath=os.getcwd()

print "Make Directory:",os.mkdir("newdir")
print "Remove File:",os.remove("inPut.txt")
print "Remove directory:",os.rmdir("newdir")
print "Chnage The directory:",os.chdir("E:\python_software")
print "Now where we are path :",os.getcwd()
print "Comming Back to Scripts:",os.chdir(scriptPath)
print "Script Path we are :",os.getcwd()