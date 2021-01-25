import csv
import json


def read_csv(file_path):
    #file_path = 'invoice_dataset.csv'
    invoices = []
    new_invoices = []

    try:
        with open(file_path,'r') as data:
            for line in csv.DictReader(data):
                invoices.append(line)
    except IOError:
        print("I/O error")

    i = 0
    for _ in range(len(invoices)):
        items = eval(invoices[i]["menus"])

        invoice = {
            "ref": invoices[i]["ref"],
            "name": invoices[i]["name"],
            "date": invoices[i]["date"],
            "total_price": invoices[i]["total_price"],
            "menus": items,
        }
        new_invoices.append(invoice)
        i += 1

    return new_invoices
