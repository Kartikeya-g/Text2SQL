import mysql.connector as ms

def query_db(sql_query):
    con = ms.connect(host="localhost",user="root",password="Kartikkartik78",database="customers")
    cursor = con.cursor()
    
    cursor.execute(sql_query)
    data = cursor.fetchall()
    for row in data:
        print(row)

    cursor.close()
    con.close()
