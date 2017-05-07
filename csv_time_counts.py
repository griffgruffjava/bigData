import csv
from pymongo import MongoClient
from datetime import datetime

__author__ = 'Ciaran Griffin t00175569'


def write_to_csv():
    client = MongoClient('localhost', 27017)

    # for minute counts
    db = client['minute_counts']
    collection = db['minute_counts']

    # for hour counts
    # db = client['hour_counts']
    # collection = db['hour_counts']

    # for day counts
    # db = client['day_counts']
    # collection = db['day_counts']

    try:
        cursor = collection.find()

    except Exception as e:
        print("Unexpected error", type(e), e)

    try:
        # minutes
        writer = csv.writer(open("minute_tweet_counts.csv", 'w', newline=''))

        # hours
        # writer = csv.writer(open("hour_tweet_counts.csv", 'w', newline=''))

        # days
        # writer = csv.writer(open("day_tweet_counts.csv", 'w', newline=''))

        writer.writerow(('date_time',
                         'month',
                         'day',
                         'hour',
                         'minute',
                         'count',))

        counter = 0

        for doc in cursor:
            counter += 1

            date_time = datetime(2017,
                                 doc['month'],
                                 doc['day'],
                                 doc['hour'],
                                 doc['min']
                                 )
            print(date_time)
            writer.writerow((date_time,
                             doc['month'],
                             doc['day'],
                             doc['hour'],
                             doc['min'],
                             doc['count']))
            print(counter)
            # if counter == 3:
            #     break

    finally:
        print("out a here")


write_to_csv()
