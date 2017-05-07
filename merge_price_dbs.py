from pymongo import MongoClient


def merge_dbs():
    client = MongoClient('localhost', 27017)
    db = client['btn_price']
    collection = db['btn_price']

    destination_db = client['all_prices']

    print(collection.count())

    count = 0

    try:
        cursor = collection.find()

    except Exception as e:
        print("Unexpected error", type(e), e)

    for doc in cursor:
        count += 1
        print(count)
        destination_db.all_prices.insert(doc)



merge_dbs()



