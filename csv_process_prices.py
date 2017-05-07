import csv
# import sys
from pymongo import MongoClient

__author__ = 'Ciaran Griffin t00175569'


def write_to_csv():

    client = MongoClient('localhost', 27017)
    db = client['all_prices']
    collection = db['all_prices']

    try:
        cursor = collection.find()

    except Exception as e:
        print("Unexpected error", type(e), e)

    try:
        writer = csv.writer(open("price_data.csv", 'w', newline=''))
        writer.writerow(('iso_time', 'usd', 'gbp', 'eur'))

        counter = 0
        for doc in cursor:
            counter += 1

            time = doc.get('time', {}).get('updatedISO')
            usd = doc.get('bpi', {}).get('USD', {}).get('rate_float')
            gbp = doc.get('bpi', {}).get('GBP', {}).get('rate_float')
            eur = doc.get('bpi', {}).get('EUR', {}).get('rate_float')

            print(counter, time, usd, gbp, eur)

            writer.writerow((time, usd, gbp, eur))

            # if counter == 25000:
            #     break

    finally:
        print("out a here")


write_to_csv()
