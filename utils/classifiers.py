from sklearn.model_selection import train_test_split
from  nltk import classify
from nltk import NaiveBayesClassifier

def classify_with_naive_bayes(data, test_size):
    training, test = train_test_split(
        data,
        test_size=test_size,
        random_state=random_state()
    )

    classifier = NaiveBayesClassifier.train(training)
    accuracy = classify.accuracy(classifier, test)
    return {
        'accuracy': accuracy,
        'classifier': classifier
    }

def random_state():
    return 42
