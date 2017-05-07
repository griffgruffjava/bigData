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


def get_string_date(month, day):
    dt_obj = datetime.date(2017, month, day)
    date_str = dt_obj.strftime("%Y-%m-%d")
    return date_str


def write_to_file():

    client = MongoClient('localhost', 27017)
    db = client['tweets_time_data']
    collection = db['tweets_time_data']

    try:
        cursor = collection.find()

    except Exception as e:
        print("Unexpected error", type(e), e)

    try:
        f = open("senti_pre_D.txt", "w+")

        counter = 0
        for doc in cursor:

            counter += 1
            if counter > 2400000:
                month = doc['month']
                day = doc['day']
                text = doc['text']
                text = text.replace('\n', ' ').replace('\r', '')          #http://stackoverflow.com/questions/16566268/remove-all-line-breaks-from-a-long-string-of-text
                print(get_string_date(month, day) + '\t' + text + '\n')
                try:
                    f.write(get_string_date(month, day) + '\t' + text + '\n')
                except Exception as e:
                    print("fuck it!! Keep going!")

                if counter > 3200000:
                    break

    finally:
        f.close()
        print("out a here")


write_to_file()
