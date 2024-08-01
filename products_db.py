import mysql.connector

def save(category, brand, name,  price, count):
    # Connect
    db = mysql.connector.connect(user="root", password="root123", database="warehouse", host="localhost")
    cursor = db.cursor()
    # opretions
    cursor.execute("INSERT INTO product (category, brand, name,  price, count) VALUES (%s,%s,%s,%s,%s)" , [category, brand, name, price, count])
    # save
    db.commit()
    # Discoonect
    cursor.close()
    db.close()


def edit(code, category, brand, name,  price, count):
    # Connect
    db = mysql.connector.connect(user="root", password="root123", database="warehouse", host="localhost")
    cursor = db.cursor()
    # opretions
    cursor.execute("UPDATE product SET category=%s, brand=%s, name=%s, price=%s, count=%s WHERE code=%s" , [category, brand, name, price, count, code])
    # save
    db.commit()
    # Discoonect
    cursor.close()
    db.close()

def remove(code):
    # Connect
    db = mysql.connector.connect(user="root", password="root123", database="warehouse", host="localhost")
    cursor = db.cursor()
    # opretions
    cursor.execute("DELETE FROM product WHERE code=%s" , [code])
    # save
    db.commit()
    # Discoonect
    cursor.close()
    db.close()



def find_all():
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
    return product_list



def find_by_category(category):
    # Connect
    db = mysql.connector.connect(user="root", password="root123", database="warehouse", host="localhost")
    cursor = db.cursor()
    # opretions
    cursor.execute("SELECT * FROM product WHERE category LIKE %s" , [category+"%"])
    # save (we dont need save cus we dont add anything to the product table)
    product_list = cursor.fetchall()
    # Discoonect
    cursor.close()
    db.close()
    return product_list



def find_by_price_range(start,end):
    # Connect
    db = mysql.connector.connect(user="root", password="root123", database="warehouse", host="localhost")
    cursor = db.cursor()
    # opretions
    cursor.execute("SELECT * FROM product WHERE price BETWEEN %s AND %s" , [start,end])
    # save (we dont need save cus we dont add anything to the product table)
    product_list = cursor.fetchall()
    # Discoonect
    cursor.close()
    db.close()
    return product_list



def find_by_name(name):
    # Connect
    db = mysql.connector.connect(user="root", password="root123", database="warehouse", host="localhost")
    cursor = db.cursor()
    # opretions
    cursor.execute("SELECT * FROM product WHERE name = %s" , [name])
    # save (we dont need save cus we dont add anything to the product table)
    product_list = cursor.fetchall()
    # Discoonect
    cursor.close()
    db.close()
    return product_list
