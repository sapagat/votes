import pandas as pd
import seaborn as sns
from . import dataset

def read_tweets(filename):
    tweets = dataset.read_tweets(filename)
    return pd.DataFrame(tweets)

def counts_by_category(tweets):
    query = tweets.groupby('category')
    query = query.count()
    query = query.sort_values('tweet_id', ascending=False)
    return query['tweet_id']

def plot_categories_distribution(tweets):
    sns.distplot(counts_by_category(tweets))
