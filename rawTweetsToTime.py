import jsonpickle
from pymongo import MongoClient
import time


def dissect(doc_dict):
    tweet = {}
    tweet['tmstp'] = int((doc_dict['timestamp_ms']))/1000
    time_tuple = time.gmtime(tweet['tmstp'])
    # print(repr(time_tuple))
    # time.struct_time(tm_year=2017, tm_mon=2, tm_mday=2, tm_hour=21, tm_min=4, tm_sec=52, tm_wday=3, tm_yday=33, tm_isdst=0)
    tweet['month'] = time_tuple[1]
    tweet['day'] = time_tuple[2]
    tweet['hour'] = time_tuple[3]
    tweet['min'] = time_tuple[4]
    tweet['text'] = doc_dict['text']
    tweet['hashtags'] = doc_dict['hashtags']
    tweet['user_info'] = doc_dict['user_info']
    # print(tweet)
    return tweet


def convert_to_json(dict_doc):
    json_doc = jsonpickle.encode(dict_doc)
    return json_doc


def refactor_tweets():
    client = MongoClient('localhost', 27017)
    db = client['tweets_processed_2']
    db2 = client['tweets_time_data']
    collection = db['tweets_processed_2']
    print(collection.count())
    try:
        cursor = collection.find()

    except Exception as e:
        print("Unexpected error", type(e), e)

    count = 0
    for doc in cursor:
        count += 1
        print(count)
        new_doc = dissect(doc)
        print(new_doc)
        db2.tweets_time_data.insert(new_doc)
        # if count == 1:
        #     break


refactor_tweets()










