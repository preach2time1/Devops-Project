import pymysql

schema_name = "mydb"

# Establishing a connection to DB
conn = pymysql.connect(host='127.0.0.1', port=3306, user='user', passwd='password', db=schema_name)
conn.autocommit(True)

# Getting a cursor from Database
cursor = conn.cursor()

cursor.execute(f"DELETE FROM {schema_name}.users WHERE id = '4'")

cursor.close()
conn.close()