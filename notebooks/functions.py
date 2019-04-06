import csv
import pandas as pd
import re
import nltk
try:
    nltk.data.find('corpora/stopwords.zip')
except LookupError:
    nltk.download('stopwords')

from nltk.corpus import stopwords

from nltk.tokenize import TweetTokenizer
from nltk.stem import PorterStemmer
from sklearn.model_selection import train_test_split
from nltk import classify
from nltk import NaiveBayesClassifier

import string

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

def parse_input_as_dictonary():
    data = []
    f = open(DATASET, 'r')
    for row in csv.reader(f, delimiter= ' '):
        tweet = {
            'tweet_id': row[0],
            'category': row[1],
            'text': ' '.join(row[3:])
        }
        data.append(tweet)
    return data

def counts_by_category(tweets):
    query = tweets.groupby('category')
    query = query.count()
    query = query.sort_values('tweet_id', ascending=False)
    return query['tweet_id']

def remove_characters_from_tweet(tweet):
    tweet = remove_old_style_retweet_text(tweet)
    tweet = remove_hyperlinks(tweet)
    tweet = remove_hashtags(tweet)
    return tweet

def remove_old_style_retweet_text(tweet):
    return re.sub(r'^RT[\s]+', '', tweet)

def remove_hyperlinks(tweet):
    return re.sub(r'https?:\/\/.*[\r\n]*', '', tweet)

def remove_hashtags(tweet):
    return re.sub(r'#', '', tweet)

def tokenize(tweet):
    tokenizer = TweetTokenizer(preserve_case=False, strip_handles=True, reduce_len=True)
    tokens = tokenizer.tokenize(tweet)
    return tokens

def filter_tokens(tokens):
    tokens = reject_stopwords(tokens)
    tokens = reject_emoticons(tokens)
    tokens = reject_punctuations(tokens)
    return list(tokens)

def reject_stopwords(tokens):
    spanish_stopwords = stopwords.words('spanish')
    return filter(lambda token: token not in spanish_stopwords, tokens)

def reject_emoticons(tokens):
    emoticons_happy = set([
        ':-)', ':)', ';)', ':o)', ':]', ':3', ':c)', ':>', '=]', '8)', '=)', ':}',
        ':^)', ':-D', ':D', '8-D', '8D', 'x-D', 'xD', 'X-D', 'XD', '=-D', '=D',
        '=-3', '=3', ':-))', ":'-)", ":')", ':*', ':^*', '>:P', ':-P', ':P', 'X-P',
        'x-p', 'xp', 'XP', ':-p', ':p', '=p', ':-b', ':b', '>:)', '>;)', '>:-)',
        '<3'
        ])
    emoticons_sad = set([
        ':L', ':-/', '>:/', ':S', '>:[', ':@', ':-(', ':[', ':-||', '=L', ':<',
        ':-[', ':-<', '=\\', '=/', '>:(', ':(', '>.<', ":'-(", ":'(", ':\\', ':-c',
        ':c', ':{', '>:\\', ';('
        ])
    emoticons = emoticons_happy.union(emoticons_sad)
    return filter(lambda token: token not in emoticons, tokens)

def reject_punctuations(tokens):
    return filter(lambda token: token not in string.punctuation, tokens)

def stem(words):
    stemmer = PorterStemmer()
    stems = []
    for word in words:
        stems.append(stemmer.stem(word))
    return stems

def bag_of_words(words):
    return dict([word, True] for word in words)

def run_pipeline(pipeline, text):
    result = text
    for command in pipeline:
        result = command(result)
    return result

def labeled_featureset(tweets, pipeline):
    data = []

    for tweet in tweets:
        feature_set = run_pipeline(pipeline, tweet['text'])
        label = tweet['category']
        labeled_featureset = (feature_set, label)
        data.append(labeled_featureset)

    return data

def classify_with_naive_bayes(data, test_size, describe=True, show_top=10):
    training, test = train_test_split(data, test_size=test_size)

    classifier = NaiveBayesClassifier.train(training)
    accuracy = classify.accuracy(classifier, test)
    return {
        'accuracy': accuracy,
        'classifier': classifier
    }
