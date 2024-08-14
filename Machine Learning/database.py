import sqlite3
conn=sqlite3.connect("bikedata.db")

# create table ("owner int,brand varcahr(40),kms_drivwn int,power int,age int,prediction_price int")


query_to_create_table='''
create table bikedetails ("owner int,brand varcahr(40),kms_drivwn int,power int,age int,prediction_price int")
'''
cur=conn.cursor()
cur.execute(query_to_create_table)
cur.close()
conn.close()