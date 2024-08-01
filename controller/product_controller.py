import re

def save(category, brand, name, price, count):
        if re.match("^[a-zA-Z\s]{2-30}$", category) and re.match("^[a-zA-Z\s]{2-30}$", brand) and re.match("^[a-zA-Z0-9\s]{2-30}$", name)and price>0 and count>0