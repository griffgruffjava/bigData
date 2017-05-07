import csv
import datetime
from pymongo import MongoClient

__author__ = 'Ciaran Griffin t00175569'


def get_next_date(date):
    prev = datetime.datetime.strptime(date, "%Y-%m-%d")
    # delta = datetime.timedelta(days=7)
    delta = datetime.timedelta(days=1)
    next_date = prev + delta
    str_date = next_date.strftime('%Y-%m-%d')
    return str_date


def write_to_csv():

    client = MongoClient('localhost', 27017)
    db = client['historical_prices_raw_3']
    collection = db['historical_prices_raw_3']

    try:
        cursor = collection.find()

    except Exception as e:
        print("Unexpected error", type(e), e)

    try:
        writer = csv.writer(open("history_prices_3.csv", 'w', newline=''))
        writer.writerow(('date', 'usd'))
        start_date = '2016-08-02'

        counter = 0
        for doc in cursor:
            counter += 1
            bpi = doc.get('bpi')
            price = bpi.get(start_date, {})

            print(start_date, price)
            start_date = get_next_date(start_date)

            writer.writerow((start_date, price))

    finally:
        print("out a here")


write_to_csv()
