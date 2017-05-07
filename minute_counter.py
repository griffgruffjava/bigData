import jsonpickle
from pymongo import MongoClient
import time


def reset_current(current, doc):
    current['month'] = doc['month']
    current['day'] = doc['day']
    current['hour'] = doc['hour']
    current['min'] = doc['min']
    return current


# def reset_current2(current):
#
#     if current['min'] == 59:
#         current['min'] = 0
#         current['hour'] += 1
#     else:
#         current['min'] += 1
#
#     if current['hour'] == 24:
#         current['hour'] = 0
#         current['day'] += 1
#
#     if current['day'] == 32:
#         current['day'] = 1
#         current['month'] += 1
#
#     return current


def check_match(doc, current):

    if current['month'] == doc['month'] and current['day'] == doc['day'] and current['hour'] == doc['hour'] and current['min'] == doc['min']:
        return True


def process_count(current, current_count):
    minute = {}
    minute['month'] = current['month']
    minute['day'] = current['day']
    minute['hour'] = current['hour']
    minute['min'] = current['min']
    minute['count'] = current_count

    return minute


def refactor_tweets(current, current_count):
    client = MongoClient('localhost', 27017)
    db = client['tweets_time_data']
    db2 = client['minute_counts']
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
            db2.minute_counts.insert(new_doc)
            current = reset_current(current, doc)
            current_count = 1


current = {'month': 2,
           'day': 2,
           'hour': 21,
           'min': 4,
           }
current_count = 0
refactor_tweets(current, current_count)
