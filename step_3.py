from data import products_string
from step_1 import transform_products_to_list
from pprint import pprint


def group_products_by_customer_and_invoice(products_string):
    products_list = transform_products_to_list(products_string)
    
    customers = {}
    
    for item in products_list:
        customer_id = item[-2]
        invoice_id = item[0]
        customers.setdefault(customer_id, {})
        customers[customer_id].setdefault(invoice_id, [])
        customers[customer_id][invoice_id].append(item)
    return customers


pprint(group_products_by_customer_and_invoice(products_string))
        
