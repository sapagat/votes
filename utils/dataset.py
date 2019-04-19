import csv
import os

ROOT_PATH = os.getenv('PYTHONPATH')
DATASET_FOLDER = os.getenv('DATASET_FOLDER') or 'datasets/production/'

def read_tweets(filename):
    path = _build_path(filename)
    tweets = []
    for row in _dataset_rows(path):
        tweet = _parse_row(row)
        tweets.append(tweet)
    return tweets

def _build_path(filename):
    return ROOT_PATH + DATASET_FOLDER + filename

def _dataset_rows(path):
    f = open(path, 'r')
    return csv.reader(f, delimiter= ';')

def _parse_row(row):
    return {
        'tweet_id': row[0],
        'category': row[1],
        'text': row[2]
    }
