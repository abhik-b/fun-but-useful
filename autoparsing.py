
import os


currentloc=input("enter currentloc")
destination=input("enter destination")

os.chdir(currentloc)
source=input("enter the file name ")
destination = "{}/{}".format(destination,source)

os.rename(source,destination)
        # print(files)



#D:\pythonprojects\django projects\boilerplate