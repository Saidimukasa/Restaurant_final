import mysql.connector
# Connect to the database
#
mydatabase = mysql.connector.connect(host ="localhost", user ="root",password= "", database="restaurant")
mycursor = mydatabase.cursor()
Cid = input("Enter your customer ID: ")
Cname = input("Enter your name : ")
CAdress = input("Enter your adress : ")
CPhone = input("Enter your phone number : ")

# Inserting data into the database
mycursor.execute("INSERT INTO customer (CID,CName,CAddress,CPhone) VALUES (%s,%s,%s,%s)",(Cid,Cname,CAdress,CPhone))
mycursor.close()

mydatabase.commit()

