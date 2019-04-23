from data import products_string
from step_1 import transform_products_to_list
from pprint import pprint


def calculate_total_per_invoices(products_string):
    products_list = transform_products_to_list(products_string)
    
    customers = {}

    for product in products_list:
        customer_id = product[-2]
        invoice_id = product[0]
        quantity = float(product[3])
        price = float(product[-3])
        total_price = round(quantity * price, 3)
        
        customers.setdefault(customer_id, {})
        customers[customer_id].setdefault(invoice_id, 0)
        customers[customer_id][invoice_id] += total_price
    return customers


pprint(calculate_total_per_invoices(products_string))