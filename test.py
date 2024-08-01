import mysql.connector
import re

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


# def save(name, brand, price, count):
#     # Connect
#     db = mysql.connector.connect(user="root", password="root123", database="warehouse", host="localhost")
#     cursor = db.cursor()
#     # opretions
#     cursor.execute("INSERT INTO product (name, brand, price, count) VALUES (%s,%s,%s,%s)" , [name, brand, price, count])
#     # save
#     db.commit()
#     # Discoonect
#     cursor.close()
#     db.close()
# save('manitor','msi','300','5')




# def find_by_price_range(start,end):
#     # Connect
#     db = mysql.connector.connect(user="root", password="root123", database="warehouse", host="localhost")
#     cursor = db.cursor()
#     # opretions
#     cursor.execute("SELECT * FROM product WHERE price BETWEEN %s AND %s" , [start,end])
#     # save (we dont need save cus we dont add anything to the product table)
#     product_list = cursor.fetchall()
#     # Discoonect
#     cursor.close()
#     db.close()
#     return product_list
# print(find_by_price_range(100,300))


def save_controller(category, brand, name, price, count):
        try:
                if re.match("^[a-zA-Z\s]{2-30}$", category) and re.match("^[a-zA-Z\s]{2-30}$", brand) and re.match("^[a-zA-Z0-9\s]{2-30}$", name) and price>0 and count>0:
                    save(category,brand,name,price,count)
                    return True, "Stuff saved"
                else:
                    raise ValueError("Invalid data")
        
        except Exception as e:
              return False, e
              

