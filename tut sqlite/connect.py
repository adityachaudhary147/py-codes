#jai mata di#
import sys
sys.stdin = open('input.in', 'r')  
sys.stdout = open('output.out', 'w') 


import sqlite3
conn= sqlite3.connect('test.db')
print("Succes")
# conn.execute('''CREATE TABLE IF NOT EXISTS COMPANY(
# ID INT PRIMARY KEY NOT NULL,
# NAME TEXT NOT NULL,
# ADDRESS CHAR(50),
# SALARY REAL);''')
# print("success table created")
# conn.execute("INSERT INTO COMPANY (ID,NAME,ADDRESS,SALARY) VALUES(2,'ADITYA','FARIDABAD',15000.00)");
# conn.execute("INSERT INTO COMPANY (ID,NAME,ADDRESS,SALARY) VALUES(3,'AKHIL','HISAR',14000.00)");
# print("values updated")
# conn.execute("UPDATE COMPANY SET SALARY=50000.00 WHERE ID=3")
cursor= conn.execute("SELECT ID, NAME ,ADDRESS,SALARY from COMPANY;")
# conn.execute("DESCRIBE COMPANY;")
# print(cursor)
for row in cursor:
	# print("123")
	print(row)


conn.commit()

conn.close()

