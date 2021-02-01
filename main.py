import os
from row_data_reader import read_csv
from db_operations import insert_invoice, bulk_insert_sales, bulk_insert_invoices


path = os.getcwd()
base_dir = os.path.dirname(os.path.normpath(path))
file_path = os.path.join(base_dir, 'invoice_dataset.csv')

invoices = read_csv(file_path)

sales = []
invoices_to_save = []

i = 0
for _ in range(len(invoices)):
    invoice = invoices[i]
    items = invoices[i]["menus"]
    # import pdb; pdb.set_trace()

    j = 0
    for _ in range(len(items)):
        sale = (items[j]["designation"], items[j]["quantity"], items[j]["price"], invoices[i]["city"])
        sales.append(sale)
        j += 1
    i += 1

    invoice_to_save = (invoices[i]["ref"], invoices[i]["name"], invoices[i]["total_price"])
    insert_invoice(invoice_to_save)
    invoices_to_save.append(invoice_to_save)

try:
    bulk_insert_invoices(invoices_to_save)
    bulk_insert_sales(sales)
except Exception as e:
    print("Error on request execution!")