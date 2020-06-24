# pip install mysql-connector

from mysql.connector import connect

cnx = connect(
	host='35.238.34.27',
	database='demo',
	user='nivratti',
	password='Rajendra4@@', 
	port=3306
)

print("Successfully connected to database.")