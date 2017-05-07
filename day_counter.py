import jsonpickle
from pymongo import MongoClient
import time


def reset_current(current, doc):
    current['month'] = doc['month']
    current['day'] = doc['day']
    return current


def check_match(doc, current):

    if current['month'] == doc['month'] and current['day'] == doc['day']:
        return True


def process_count(current, current_count):
    day = {}
    day['month'] = current['month']
    day['day'] = current['day']
    day['count'] = current_count

    return day


def refactor_tweets(current, current_count):
    client = MongoClient('localhost', 27017)
    db = client['tweets_time_data']
    db2 = client['day_counts']
    collection = db['tweets_time_data']
    print(collection.count())
    try:
        cursor = collection.find()

    except Exception as e:
        print("Unexpected error", type(e), e)

    count = 0
    for doc in cursor:
        count += 1
        print(count)

        if check_match(doc, current):
            current_count += 1
        else:
            new_doc = process_count(current, current_count)
            print(new_doc)
            db2.day_counts.insert(new_doc)
            current = reset_current(current, doc)
            current_count = 1


current = {'month': 2,
           'day': 2
           }
current_count = 0
refactor_tweets(current, current_count)
