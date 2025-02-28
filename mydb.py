from datetime import datetime
import mysql.connector
import os 

mydb = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    database=os.getenv("DB_DATABASE"),
    password=os.getenv("DB_PASSWORD")
)

mycursor = mydb.cursor()

def make_entry(mycursor, filename):
    sql = f"INSERT INTO images (name, date) VALUES ('{filename}', '{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}')"
    mycursor.execute(sql)
    mydb.commit()
    print("the entry in db was succesfully made")
