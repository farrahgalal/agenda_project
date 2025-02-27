#lookup_agenda.py
#This program finds agenda sessions in the data you imported.

#To complete this task, you will need to:
#1. Parse command line arguments to retrieve lookup conditions
#2. Get the table records which match the lookup conditions provided
##3. Print the resulting records onto the screen

#We should be able to run your program as follows:\
#`$> ./lookup_agenda.py column value`

import sys
from db_table import db_table

def lookup_agenda(column, value):
    return 0

if __name__ == "__main__":
    column = sys.argv[1]
    value = sys.argv[2]
    lookup_agenda(column, value)
