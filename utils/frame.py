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

def random_subsamples(tweets, fraction, replicas):
    result = []
    for i in range(replicas):
        result.append(percentage_by_category(random_subsample(tweets, fraction)).to_dict())
    return result

def grid_subsamples(tweets, fractions, replicas):
    descriptor = {
        'categories': tweets['category'].unique(),
        'subsamples': []
    }
    for fraction in fractions:
        descriptor['subsamples'].append({
            'fraction': fraction,
            'replicas': random_subsamples(tweets, fraction, replicas)
        })
    return descriptor

def percentage_by_category(tweets):
    total = tweets.shape[0]
    return counts_by_category(tweets) / total
