import random
import csv
from datetime import datetime

from faker import Faker


fake = Faker('fr_FR')
tab = []

cities = ["Yaounde", "Douala", "Bafoussam", "Bamenda", "Kribi", "Bertoua"]
my_word_list = [ 'Pizza au fromage', 'Hamburger', 'Cheeseburger', 'Moules Marinières', 'Salade Grecque',
        'Petit Hamburger', 'Petit Cheeseburger', 'Petit Bacon Burger', 'Petit Bacon Cheeseburger',
        'Sandwich Vegan', 'Sandwich Vegan au fromage', 'Fromage grillé', 'Pates',
        'Cheese Dog', 'Hot Dog', 'Welsh', 'Tartiflette', 'Boeuf Bourguignons']



def random_ref():
    rnd_nber = random.randrange(1000)
    d = datetime.now()
    day = d.day
    year = d.year
    month = d.month
    ref = "INVOICE/%s/%s/%s/%s" % (day, month, year, rnd_nber)
    return ref


def generate_invoices(nber):
    invoices = []
    if not nber > 1000:
        for _ in range(nber):
            items = fake.pyint(1, 10, 1)
            invoice = {}
            total = 0
            ref = random_ref()
            name = fake.name()
            date = fake.date_time_between(start_date = "-6w", end_date = "now").isoformat()

            invoice = {
                "ref": ref,
                "name": name,
                "date": date,
                "city": random.choice(cities),
                "menus": [],
            }

            for _ in range(items):
                quantity = fake.pyint(1, 10, 1)
                unit_price = fake.pyint(1000, 7000, 500),
                unit_price = unit_price[0]
                price = quantity * unit_price

                invoice["menus"].append({
                    "designation": random.choice(my_word_list),
                    "quantity": quantity,
                    "unit_price": unit_price,
                    "price": price
                })
                total += price

            invoice["total_price"] = total
            invoices.append(invoice)

        csv_columns = ['ref' ,'name','date', 'city', 'menus', 'total_price']

        try:
            with open('invoice_dataset.csv', 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                writer.writeheader()
                for data in invoices:
                    writer.writerow(data)
        except IOError:
            print("I/O error")
        return invoices

    else:
        return "Vous ne pouvez pas générer plus de 1000 factures"
