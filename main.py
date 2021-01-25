from row_data_reader import read_csv
from db_operations import bulk_insert_sales


invoices = read_csv("/home/stephcyrille/Ecole/Niveau5/BI/TP/invoice_dataset.csv")
sales = []

i = 0
for _ in range(len(invoices)):
    invoice = invoices[i]
    items = invoices[i]["menus"]
    # import pdb; pdb.set_trace()

    j = 0
    for _ in range(len(items)):
        sale = (items[j]["designation"], items[j]["quantity"], items[j]["price"])
        sales.append(sale)
        j += 1
    i += 1

try:
    bulk_insert_sales(sales)
except Exception as e:
    print("Error on request execution!")