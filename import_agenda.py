# import_agenda.py
# This program imports the schedule of an event into a local SQLite database.

#To complete this task, you will need to:
#1. Open an Agenda excel file
#2. Design SQLite Database table schema(s) to store agenda information
#3. Parse the content of the excel file and store the content in the table(s) you designed

#We should be able to run your program as follows:\
#`$> ./import_agenda.py agenda.xls`

import sqlite3
import sys
import pandas as pd
from db_table import db_table

def import_agenda(filename):
    # reads excel file, filename -> path to excel file
    df = pd.read_excel(filename)

    agenda_table = db_table("agenda", {
        "agenda_id": "INTEGER PRIMARY KEY AUTOINCREMENT",
		"date": "TEXT NOT NULL",
		"time_start": "TEXT",
		"time_end": "TEXT",
        "type": "TEXT", #session or subsessions
		"title": "TEXT",
		"location": "TEXT",
		"description": "TEXT",
		"speaker": "TEXT"
    })

    for index, row in df.iterrows():
        if index >= 16:
            data = {
                "date": row.iloc[0],
                "time_start": row.iloc[1],
                "time_end": row.iloc[2],
                "type": row.iloc[3],
                "title" : row.iloc[4],
                "location" : row.iloc[5] if row.iloc[5] else None,
                "description" : row.iloc[6] if row.iloc[6] else None,
                "speaker" : row.iloc[7] if row.iloc[7] else None
            }
  
            agenda_table.insert(data)    
            print(agenda_table.all())

    agenda_table.close()
    print("success")

if __name__ == "__main__":
    import_agenda(sys.argv[1]) # only argument in the command line is the filename 