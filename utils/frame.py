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

def random_subsample(tweets, fraction):
    return tweets.sample(frac = fraction)

def grid_subsamples(tweets, fractions, replicas):
    data = []
    for fraction in fractions:
        for replica in range(replicas):
            descriptor = percentage_by_category(random_subsample(tweets, fraction))
            descriptor['fraction'] = fraction
            data.append(descriptor)
    return pd.DataFrame(data)

def percentage_by_category(tweets):
    total = tweets.shape[0]
    return (counts_by_category(tweets) / total).to_dict()
