import csv
# import sys
from pymongo import MongoClient

__author__ = 'Ciaran Griffin t00175569'


def return_field(dict_fields, field_name):
    try:
        field = dict_fields[field_name]
        if isinstance(field, str):
            field = field.encode("ascii", 'replace')
        if field is None:
            field = "NA"
            field = field.encode("ascii", 'replace')
    except Exception as e:
        field = "NA"
        field = field.encode("ascii", 'replace')
        print(e)
    return field


def get_hashtags(hashtags_ls):
    tag_ls = []
    # tags = "NA"
    if hashtags_ls:
        try:
            for hashtag_entry in hashtags_ls:
                hashtag = hashtag_entry['text']
                tag_ls.append(hashtag.encode("ascii", 'replace'))
        except Exception as e:
            print(e)

    # if tag_ls:
    #     str1 = " ".join(str(x) for x in tag_ls)
    #     tags = str1

    # print(tags)
    decoded_tags = []
    for tag in tag_ls:
        decoded_tags.append(tag.decode('utf'))
    return " ".join(str(x) for x in decoded_tags)


def write_to_csv():
    # client = MongoClient()
    client = MongoClient('localhost', 27017)
    db = client['tweets_processed']
    collection = db['tweets_processed']

    try:
        cursor = collection.find()

    except Exception as e:
        print("Unexpected error", type(e), e)

    try:
        writer = csv.writer(open("tweet_data.csv", 'w', newline=''))

        writer.writerow(('mongo_id',
                         'tweet_id',
                         'timestamp_ms',
                         'created_at',
                         # 'geo', This data is the same
                         'coordinates',
                         'text',
                         'follower_count',
                         'verified_user',
                         'user_created_at',
                         'name',
                         'screen_name',
                         'user_id',
                         'user_location',
                         'user_description',
                         'hash_tags'))

        counter = 0

        for doc in cursor:
            counter += 1
            user = doc['user_info']
            hashtags_list = doc['hashtags']

            hashtags_str = get_hashtags(hashtags_list)

            # if(counter == 1):
            #     print(float(return_field(doc, 'id')))

            writer.writerow((return_field(doc, '_id'),
                             return_field(doc, 'id'),
                             return_field(doc, 'timestamp_ms').decode('utf-8'),
                             return_field(doc, 'created_at').decode('utf-8'),
                             # return_field(doc, 'geo'),
                             return_field(doc, 'coordinates'),
                             return_field(doc, 'text').decode('utf-8'),
                             return_field(user, 'followers_count'),
                             return_field(user, 'verified'),
                             return_field(user, 'created_at').decode('utf-8'),
                             return_field(user, 'name').decode('utf-8'),
                             return_field(user, 'screen_name').decode('utf-8'),
                             return_field(user, 'id'),
                             return_field(user, 'location').decode('utf-8'),
                             return_field(user, 'description').decode('utf-8'),
                             hashtags_str))
            print(counter)
            # if counter == 1000000:
            #     break

    finally:
        print("out a here")


write_to_csv()
