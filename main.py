import time

import pandas as pd
import mysql.connector
import datetime

# Define your MySQL database connection parameters
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "flemingohr"  # Change to your database name
}

# Connect to the MySQL database
try:
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    print("connected : ",conn)
except Exception as e:
    print("eror bro ;",e )


# Read the Excel file into a pandas DataFrame
excel_file = "Employee list.xlsx"  # Replace with your Excel file name
df = pd.read_excel(excel_file)

# Iterate through the rows of the DataFrame and insert data into the MySQL table
for index, row in df.iterrows():


    ids=row["ids"]
    epf=row["epf"]
    title=row["title"]
    name=row["name"]
    designation=row["designation"]
    department=row["department"]
    grade=row["grade"]
    location=row["location"]
    doj=row["doj"]
    mngr=row["mngr"]

    mngremail=row["mngremail"]
    # admin=row["admin"]
    # avatar=row["avatar"]
    # isapplied=row["isapplied"]
    # promoted=row["promoted"]

    print("data : ",ids, epf, title, name, designation, department, grade, location, doj, mngr, mngremail)



    # , id, epf, title, name, designation, department, grade, location, doj, mngr, mngrepf, mngremail, admin, avatar, isapplied, promoted,

    # SQL query to insert data into the table


    # insert_query = f"INSERT INTO employee (id, epf, title, name, designation, department, grade, location, doj, mngr,mngremail) VALUES ({ids},{epf},{title},{name},{designation},{department},{grade},{location},{doj},{mngr},{mngremail})"
    insert_query = f"INSERT INTO employee (id, epf, title, name, designation, department, grade, location, doj, mngr, mngremail) VALUES ({ids}, '{epf}', '{title}', '{name}', '{designation}', '{department}', '{grade}', '{location}', '{doj}', '{mngr}', '{mngremail}')"

    # values = (user_id, user_name, manager_name)

    cursor.execute(insert_query)
    # time.sleep(0.0)


# Commit the changes and close the database connection
conn.commit()
conn.close()

print("Data has been successfully inserted into the MySQL database.")
