import sys
import sqlite3
import pandas as pd
import datetime

con = sqlite3.connect("todo.db")
cur = con.cursor()

print("input 'initialize' or 'create' or 'read' or 'update' or 'delete'")
crud = input()

if crud == "initialize":
    try:
        cur.execute("CREATE TABLE todo(is_done, date_created, contents)")# TODO: add ID column
    except Exception as e: # NOTE: If the table is already exists, It raises error.
        print(e)
elif crud == "create":
    print("input todo contents: ")
    contents = input()

    current_date_as_date = datetime.date.today()
    current_date_as_str = current_date_as_date.strftime('%Y-%m-%d')
    # TODO: add ID column
    insert_sql = f"""
        INSERT INTO todo VALUES
            ('0', '{current_date_as_str}', '{contents}')
    """
    cur.execute(insert_sql)
    con.commit()
elif crud == "read":
    pass# NOTE: pass and just execute select and write markdown file later.
elif crud == "update":
    print("input contents")
    # TODO: select row with ID but not contents
    contents = input()
    update_sql = f"UPDATE todo SET is_done = '1' where contents = '{contents}'"
    cur.execute(update_sql)
    con.commit()
elif crud == "delete":
    pass# TODO: do something
else :
    print("crud is wrong")
    sys.exit()

select_sql = "SELECT * FROM todo where is_done = '0'"
df = pd.read_sql_query(sql = select_sql, con = con)
# print(df.head())
todo_table = df.to_markdown()
print(todo_table)
with open("todo.md", "w") as file:
    file.write(todo_table)
