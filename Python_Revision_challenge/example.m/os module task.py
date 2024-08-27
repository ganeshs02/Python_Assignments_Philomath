'''write a program to clear the clutter inside a folder on your computer you should use os module 
to rename all the png images form i.png - n.png files in that folder do the same for other file
formats'''

'''
eg - 
stdf.png - 1.png
fjdflkjdas.txt - 2.png
fjsdafasdf.pdf - 3.png '''

import os
import shutil as s

class Cleartheclutter:

    def create(self): #to creat the directory if not exists. 
        if (not os.path.exists("osmod")):
            os.mkdir("osmod")
            for i in range(0,5):
                os.mkdir(f"osmod/file{i+1}")
    
    def rename(self): #to rename the existing files in the directory.
        for i in range (0,5):
            os.rename(f"osmod/file{i+1}",f"osmod/{i+1}.png{i+1}")

    def delete(self): #to remove the directory if exists
        if(os.path.exists("osmod")):
            s.rmtree("osmod")
        


obj = Cleartheclutter()
obj.create() 
obj.rename()
obj.delete()





