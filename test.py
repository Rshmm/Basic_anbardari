import mysql.connector


# # Connect to db
# db = mysql.connector.connect(user="root", password="root123", database="warehouse", host="localhost")
# curser = db.cursor()
# # Oprations
# curser.execute("INSERT INTO product (name, brand, price, count) VALUES ('phone' , 'samsung', '1700', '12')")
# # Save
# db.commit()
# # Disconnect
# curser.close()
# db.close()


# Connect
db = mysql.connector.connect(user="root", password="root123", database="warehouse", host="localhost")
cursor = db.cursor()
# opretions
cursor.execute("SELECT * FROM product")
# save (we dont need save cus we dont add anything to the product table)
product_list = cursor.fetchall()
# Discoonect
cursor.close()
db.close()

print(product_list)