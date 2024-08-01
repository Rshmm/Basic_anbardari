import re
from products_db import save,find_all


def save_controller(category, brand, name, price, count):
        try:
                if re.match("^[a-zA-Z\s]{2,30}$", category) and re.match("^[a-zA-Z\s]{2,30}$", brand) and re.match("^[a-zA-Z0-9\s]{2,30}$", name) and int(price) > 0 and int(count) > 0:
                    save(category,brand,name,price,count)
                    return True, "Stuff saved"
                else:
                    raise ValueError("Invalid data")
        
        except Exception as e:
              return False, e
              


def find_all_controller():
        try:
            return True,find_all()
        
        except Exception as e:
              return False, e