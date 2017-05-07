
import jsonpickle
from pymongo import MongoClient
import time


def refactor_tweets():
    client = MongoClient('localhost', 27017)
    db = client['tweets_time_data']
    db2 = client['test_time']
    collection = db['tweets_time_data']
    print(collection.count())
    try:
        cursor = collection.find()

    except Exception as e:
        print("Unexpected error", type(e), e)

    count = 0
    for doc in cursor:
        count += 1
        month = 2
        print(count)
        print(doc)
        db2.test_time.insert(doc)
        if count == 5000:
            break


refactor_tweets()