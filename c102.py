import os 
import shutil

source = "C:/Users/DELL/Downloads/C102"
destination = "C:/Users/DELL/Documents/python/C102"
lists = os.listdir(source)

#print(lists)

for fileName in lists :
    name,ext = os.path.splitext(fileName)
   
    if ext == "" :
        continue
    if ext in [".gif" , ".png" , ".jpg" , ".jfif"] :
        path1 = source + "/" + fileName
        path2 = destination + "/" + "ImageFiles"
        path3 = destination + "/" + "ImageFiles/" + fileName 
        print(path1)
        print(path3)

        if os.path.exists(path2) :
            print("You are moving a file." + fileName)
            shutil.move(path1 , path3)

        else :
            os.makedirs(path2)
            print("You have moved this file." + fileName)
            shutil.move(path1 , path3)




    
