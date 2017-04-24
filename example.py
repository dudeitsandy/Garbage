import datetime
r"""
this script creates an empty file
"""


filename=datetime.datetime.now()

#create empty file

def create_file():
        """this function creates an empty file"""
        with open(filename.strftime("%Y-%m-%d-%H-%M")+".txt",'w') as file:
            file.write("")#writing empty string

create_file()
