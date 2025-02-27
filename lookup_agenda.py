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
    agenda_table = db_table("agenda", {
    "date": "TEXT NOT NULL",
    "time_start": "TEXT NOT NULL",
    "time_end": "TEXT",
    "title": "TEXT NOT NULL",
    "location": "TEXT",
    "description": "TEXT",
    "speakers": "TEXT"
    })

    records = agenda_table.select()  # Fetch all records
    #------testing purposes---------#
    #if records:
        #print("\nAgenda Table:")
        #for record in records:
            #print(record)
    #--------------------------------#

    # based on the column and the value, perform the lookup in the table
    if column == "speaker":
        # there can be multiple speakers so search within the list of speakers
        rows = agenda_table.select(where={"speakers": "%{}%".format(value)})
    else:
        # for all columns except speaker, we can do an exact match
        rows = agenda_table.select(where={column: value})

    #check for sub sessions related to those sessions
    sub_sessions_lst = []
    #for i in rows, iterate over rows
        #sub_sessions = agenda_table.select(where={parent_id: "{}.format(row["id"])"})
        #sub_sessions_lst.extend(sub_sessions)
    

    print(rows)

if __name__ == "__main__":
    column = sys.argv[1]
    value = sys.argv[2]
    lookup_agenda(column, value)
