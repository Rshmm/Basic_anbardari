import mysql.connector

# # testing add function
# # Connect to db
# db = mysql.connector.connect(user="root", password="root123", database="warehouse", host="localhost")
# curser = db.cursor()
# # Oprations
# curser.execute("INSERT INTO product (name, brand, price, count) VALUES ('laptop' , 'hp', '1300', '8')")
# # Save
# db.commit()
# # Disconnect
# curser.close()
# db.close()




# testing find all function
# # Connect
# db = mysql.connector.connect(user="root", password="root123", database="warehouse", host="localhost")
# cursor = db.cursor()
# # opretions
# cursor.execute("SELECT * FROM product")
# # save (we dont need save cus we dont add anything to the product table)
# product_list = cursor.fetchall()
# # Discoonect
# cursor.close()
# db.close()
# print(product_list)




# # testing the find by name function
# # Connect
# db = mysql.connector.connect(user="root", password="root123", database="warehouse", host="localhost")
# cursor = db.cursor()
# # opretions
# cursor.execute("SELECT * FROM product WHERE name = 'laptop'")
# # save (we dont need save cus we dont add anything to the product table)
# product_list = cursor.fetchall()
# # Discoonect
# cursor.close()
# db.close()
# print(product_list)
