import csv
import pandas as pd

DATASET = '../datasets/DatasetCatSpa_collected'

def parse_input():
    data = []
    f = open(DATASET, 'r')
    for row in csv.reader(f, delimiter= ' '):
        tweet = {
            'tweet_id': row[0],
            'category': row[1],
            'text': ' '.join(row[3:])
        }
        data.append(tweet)

    return pd.DataFrame(data)

def counts_by_category(tweets):
    query = tweets.groupby('category')
    query = query.count()
    query = query.sort_values('tweet_id', ascending=False)
    return query['tweet_id']
