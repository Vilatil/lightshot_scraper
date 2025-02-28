from datetime import datetime
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="lightshot"
)
mycursor = mydb.cursor()

def make_entry(mycursor, filename):
    sql = f"INSERT INTO images (name, date) VALUES ('{filename}', '{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}')"
    mycursor.execute(sql)
    mydb.commit()
    print("the entry in db was succesfully made")
