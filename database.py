print("This is the database module and python calls it {}".format(__name__))
# __name__ gives you the module python thinks it is running
# The first module you run is called the __main__. All other files are the name of the filename.

#import interface
# Imports run the entire file that is being imported, including if it has any commands in the main

#from interface import check_HDL, check_LDL
import interface as bc
from interface import *

HDL_value = 55

classification = check_HDL(HDL_value)
print("55 is {}".format(classification))