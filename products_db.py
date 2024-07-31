import mysql.connector

def save():
    # Connect
    db = mysql.connector.connect(user="root", password="root123", database="warehouse", host="localhost")
    cursor = db.cursor()
    # opretions
    cursor.execute("INSERT INTO product (name, brand, price, count) VALUES ('phone' , 'samsung', '1700', '12')")
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



def find_by_name(name):
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