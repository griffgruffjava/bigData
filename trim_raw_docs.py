import jsonpickle
from pymongo import MongoClient


def dissect(doc_dict):
    processed_tweet = {}
    user_info = {}

    entities = doc_dict['entities']
    user = doc_dict['user']

    required_fields = ['timestamp_ms',
                       'id',
                       'coordinates',
                       'geo',
                       'created_at',
                       'text']

    required_entities_fields = ['hashtags']

    required_user_fields = ['followers_count',
                            'created_at',
                            'name',
                            'id',
                            'location',
                            'following',
                            'screen_name',
                            'verified',
                            'description']

    for field in required_fields:
        processed_tweet[field] = doc_dict[field]

    for field in required_entities_fields:
        processed_tweet[field] = entities[field]

    for field in required_user_fields:
        user_info[field] = user[field]

    processed_tweet['user_info'] = user_info
    processed_tweet['mongo_id'] = str(doc_dict['_id'])

    return processed_tweet


def convert_to_json(dict_doc):
    json_doc = jsonpickle.encode(dict_doc)
    return json_doc


def refactor_tweets():
    # client = MongoClient()
    client = MongoClient('localhost', 27017)
    db = client['tweets']
    db2 = client['tweets_processed_2']
    collection = db['tweets']
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
        db2.tweets_processed_2.insert(new_doc)


refactor_tweets()











