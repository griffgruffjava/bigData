import csv
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
        writer = csv.writer(open("usd_minute", 'w', newline=''))
        writer.writerow(('date_time', 'usd'))

        counter = 0
        for doc in cursor:
            counter += 1

            time = doc.get('time', {})

            usd = doc.get('bpi', {}).get('USD', {}).get('rate_float')

            print(counter, time, usd)

            writer.writerow((time, usd))

            # if counter == 25000:
            #     break

    finally:
        print("out a here")


write_to_csv()
