import nltk
try:
    nltk.data.find('corpora/stopwords.zip')
except LookupError:
    nltk.download('stopwords')

from nltk.corpus import stopwords
import re
from nltk.tokenize import TweetTokenizer
from nltk.stem import PorterStemmer
import string

def run_pipeline(tweets, pipeline):
    data = []
    for tweet in tweets:
        sample = process_unit(pipeline, tweet['text'])
        label = tweet['category']
        data.append((sample, label))
    return data

def process_unit(pipeline, unit):
    result = unit
    for command in pipeline:
        result = command(result)
    return result

def remove_old_style_retweet_text(tweet):
    return re.sub(r'^RT[\s]+', '', tweet)

def remove_hyperlinks(tweet):
    return re.sub(r'https?:\/\/.*[\r\n]*', '', tweet)

def remove_hashtags(tweet):
    return re.sub(r'#', '', tweet)

def tokenize(tweet):
    tokenizer = TweetTokenizer(
        preserve_case=False,
        strip_handles=True,
        reduce_len=True
    )
    tokens = tokenizer.tokenize(tweet)
    return tokens

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
