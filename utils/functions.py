from sklearn.model_selection import train_test_split
import numpy as np
from sklearn import svm

def bag_of_words_for_svm(examples):
    vocabulary = vocabulary_from(examples)
    sentences = np.zeros((len(examples), len(vocabulary)))
    for sentence_id, words in enumerate(examples):
        for word in words:
            word_id = vocabulary.index(word)
            sentences[sentence_id, word_id] += 1
    return {
        'vocabulary_size': len(vocabulary),
        'sentences': sentences
    }

def vocabulary_from(sentences):
    vocabulary = set()
    for sentence in sentences:
        for word in sentence:
            if word in vocabulary:
                continue

            vocabulary.add(word)

    return list(vocabulary)

def classify_with_svm(X, y, test_size, maximum_iterations):
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=random_state()
    )
    classifier = svm.SVC(
        gamma='scale',
        max_iter=maximum_iterations,
        random_state=random_state()
    )
    classifier.fit(X_train, y_train)
    y_predicted = classifier.predict(X_test)
    total_correct = np.sum(y_predicted == y_test)
    return {
        'total_correct': total_correct,
        'accuracy': float(total_correct) / len(y_test)
    }

def random_state():
    return 42
