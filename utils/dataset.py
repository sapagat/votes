import csv
import os
import pandas as pd

ROOT_PATH = os.getenv('PYTHONPATH')
DATASET_FOLDER = os.getenv('DATASET_FOLDER') or 'datasets/development/'
CSV_DELIMITER = ';'
CSV_FIELDS = ['tweet_id', 'category', 'text']

def read_tweets(filename):
    return read_tweets_from(_build_path(filename))

def read_tweets_from(path):
    tweets = []
    for row in _dataset_rows(path):
        tweet = _parse_row(row)
        tweets.append(tweet)
    return tweets

def write_tweets_to(path, tweets):
    with open(path, 'w') as file:
        writer = csv.DictWriter(file, delimiter=CSV_DELIMITER, fieldnames=CSV_FIELDS)
        writer.writerows(tweets)

def _build_path(filename):
    return ROOT_PATH + DATASET_FOLDER + filename

def _dataset_rows(path):
    f = open(path, 'r')
    return csv.reader(f, delimiter= CSV_DELIMITER)

def _parse_row(row):
    return dict(zip(CSV_FIELDS, row))
