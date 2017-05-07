from pymongo import MongoClient


def count_it():
    client = MongoClient('localhost', 27017)
    db = client['day_counts']
    collection = db['day_counts']
    print(collection.count())
    try:
        cursor = collection.find()

    except Exception as e:
        print("Unexpected error", type(e), e)

    count = 0
    total = 0
    for doc in cursor:
        count += 1
        total += doc['count']
        print(count)
        print(doc)
        # if count>10:
        #     break
    print('total is ', total)


def see_it():
    client = MongoClient('localhost', 27017)
    db2 = client['tweets_time_data']
    collection2 = db2['tweets_time_data']
    print(collection2.count())
    try:
        cursor = collection2.find()

    except Exception as e:
        print("Unexpected error", type(e), e)

    count = 0
    for doc in cursor:
        count += 1
        print(count)
        print(doc)


# count_it()

see_it()
