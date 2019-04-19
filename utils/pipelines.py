from . import nlp
from . import classifiers
from . import frame
from datetime import datetime

TEST_SIZE = 0.2
MAX_ITERATIONS = 500

def run_naive_bayesian(tweets):
    start = iso_timestamp()
    data = nlp.run_pipeline(tweets, [
        nlp.remove_old_style_retweet_text,
        nlp.remove_hyperlinks,
        nlp.remove_hashtags,
        nlp.tokenize,
        nlp.reject_stopwords,
        nlp.reject_emoticons,
        nlp.reject_punctuations,
        nlp.stem,
        nlp.bag_of_words
    ])
    result = classifiers.classify_with_naive_bayes(data, TEST_SIZE)
    finish = iso_timestamp()
    return {
        'start': start,
        'finish': finish,
        'accuracy': result['accuracy']
    }

def run_svm(tweets):
    start = iso_timestamp()
    pipeline = [
        nlp.remove_old_style_retweet_text,
        nlp.remove_hyperlinks,
        nlp.remove_hashtags,
        nlp.tokenize,
        nlp.reject_stopwords,
        nlp.reject_emoticons,
        nlp.reject_punctuations,
        nlp.stem
    ]
    stem_sentences = [nlp.process_unit(pipeline, tweet['text']) for tweet in tweets]
    sentences = classifiers.bag_of_words_for_svm(stem_sentences)['sentences']

    X = sentences
    y = [tweet['category'] for tweet in tweets]

    result = classifiers.classify_with_svm(X, y, TEST_SIZE, MAX_ITERATIONS)
    finish = iso_timestamp()
    return {
        'start': start,
        'finish': finish,
        'accuracy': result['accuracy']
    }

def run_multisamples_naive_bayesian(tweets, fractions, replicas):
    results = []
    for fraction in fractions:
        for replica in range(replicas):
            subsample = frame.random_subsample(tweets, fraction).to_dict('records')
            result = run_naive_bayesian(subsample)
            result['fraction'] = fraction
            results.append(result)
    return results

def run_multisamples_svm(tweets, fractions, replicas):
    results = []
    for fraction in fractions:
        for replica in range(replicas):
            subsample = frame.random_subsample(tweets, fraction).to_dict('records')
            result = run_svm(subsample)
            result['fraction'] = fraction
            results.append(result)
    return results

def iso_timestamp():
    return datetime.now().isoformat(' ')
