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
from db_table import db_table
import xlrd  # library for .xls files

def import_agenda(filename):
    wb = xlrd.open_workbook(filename)
    sheet = wb.sheet_by_index(0)  

    # database table schema 
    agenda_table = db_table("agenda", {
        "date": "TEXT NOT NULL",
        "time_start": "TEXT NOT NULL",
        "time_end": "TEXT",
        #"type": "TEXT",
        "title": "TEXT NOT NULL",
        "location": "TEXT",
        "description": "TEXT",
        "speakers": "TEXT",
        #"parent_id": "INTEGER"
    })

    parent_id = None

    for row_idx in range(14, sheet.nrows):
        row = sheet.row_values(row_idx)  
        # if session is sub or main session
            # if sub, check if previous has a parent_id and assign that parent id to it
                # if doesnt have parent_id, meaning that prev row is a main session, assign id
        session_type = row[3] if row[3] else None  

        if session_type == "Sub":
            if parent_id is not None:
                data["parent_id"] = parent_id
            else:
                continue
        else:
            parent_id = None

        data = {
            "date": row[0] if row[0] else None,
            "time_start": row[1] if row[1] else None,
            "time_end": row[2] if row[2] else None,
            #"type": row[3].replace("'", "''") if isinstance(row[3], str) else None, 
            "title": row[4].replace("'", "''") if isinstance(row[4], str) else None, 
            "location": row[5].replace("'", "''") if isinstance(row[5], str) else None,
            "description": row[6].replace("'", "''") if isinstance(row[6], str) else None,
            "speakers": row[7].replace("'", "''") if isinstance(row[7], str) else None,
            "parent_id": parent_id
        }


        # date, time_start, title all must not be NULL
        if not data["date"] or not data["time_start"] or not data["title"]:
            continue  

        # check to see if row exists
        existing_rows = agenda_table.select(
            where={
                "title": data["title"],
                "date": data["date"],
                "time_start": data["time_start"]
            }
        )

        # if it does not exist -> insert (avoid repeats)
        if not existing_rows:
            agenda_table.insert(data)

    records = agenda_table.select()  # Fetch all records
    #------testing purposes---------#
    #if records:
        #print("\nAgenda Table:")
        #for record in records:
            #print(record)
    #--------------------------------#

    agenda_table.close()
    print("Agenda import successful")

if __name__ == "__main__":
    import_agenda(sys.argv[1])
