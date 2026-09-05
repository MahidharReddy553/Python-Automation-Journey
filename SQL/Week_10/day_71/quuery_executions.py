from mysql.connector import connect

conn = connect(host = "localhost",
               user = "root",
               password = "root",
               database = "mydb")


cur = conn.cursor()

query_1 = cur.execute("Select * from books;")
q1_res = cur.fetchall()

query_2 = cur.execute("Select * from books where price > %s;", ((500,)))
q2_res = cur.fetchall()

query_3 = cur.execute("Select * from books where price < %s;", ((500,)))
q3_res = cur.fetchall()

query_4 = cur.execute("Select * from books where price > %s;", ((400,)))
q4_res = cur.fetchall()

query_5 = cur.execute("Select * from books order by price desc;")
q5_res = cur.fetchall()

query_6 = cur.execute("Select * from books order by price asc;")
q6_res = cur.fetchall()

print("Query 1 result: ", q1_res)
print("Query 2 result: ", q2_res)
print("Query 3 result: ", q3_res)
print("Query 4 result: ", q4_res)
print("Query 5 result: ", q5_res)
print("Query 6 result: ", q6_res)

cur.close()
conn.close()