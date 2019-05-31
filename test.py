import os 
from os import path
from os import path
 

dir_path = os.path.dirname(os.path.realpath(__file__))

folder = dir_path
for the_file in os.listdir(folder):
    file_path = os.path.join(folder, the_file)
    try:
        if os.path.isfile(file_path) and the_file != 'test.py' :
            os.unlink(file_path)
         
    except Exception as e:
        print(e)


input()