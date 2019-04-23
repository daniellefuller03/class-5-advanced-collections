from data import products_string

def transform_products_to_list(products_string):
    splitted = products_string.split('\n')
    products = []
    
    for item in splitted:
        if item:
            clean_item = item.split(',')
            products.append(clean_item)
    return products
    
    
#print(transform_products_to_list(products_string))
