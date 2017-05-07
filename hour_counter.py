from pymongo import MongoClient


def reset_current(current, doc):
    current['month'] = doc['month']
    current['day'] = doc['day']
    current['hour'] = doc['hour']
    return current


def check_match(doc, current):

    if current['month'] == doc['month'] and current['day'] == doc['day'] and current['hour'] == doc['hour']:
        return True


def process_count(current, current_count):
    hour = {}
    hour['month'] = current['month']
    hour['day'] = current['day']
    hour['hour'] = current['hour']
    hour['count'] = current_count

    return hour


def refactor_tweets(current, current_count):
    client = MongoClient('localhost', 27017)
    db = client['tweets_time_data']
    db2 = client['hour_counts']
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
            db2.hour_counts.insert(new_doc)
            current = reset_current(current, doc)
            current_count = 1


current = {'month': 2,
           'day': 2,
           'hour': 21
           }
current_count = 0
refactor_tweets(current, current_count)
