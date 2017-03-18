import MySQLdb

db=MySQLdb.connect(host="localhost",user="root",passwd="9663302160",db="NISHA")
cur=db.cursor();
cur.execute("SELECT * FROM EMPLOYEE")

for col in cur.fetchall():
  print col
db.close()  
