#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from sklearn.neighbors import NearestCentroid
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
import attributes

def TRAIN_PATH(): return 'data/attributes/train.csv'
def TEST_PATH(): return 'data/attributes/test.csv'
def FULL_PATH(): return 'data/attributes/flags.csv'

def format_data(data):
    return ([flag.attributes() for flag in data], [country.religion for country in data])

def main(args):
    train_data = None
    with open(TRAIN_PATH(), 'r') as f:
        train_data = attributes.FlagAttributes.parse(f)
    x_train, y_train = format_data(train_data)
    
    test_data = None
    with open(TEST_PATH(), 'r') as f:
        test_data = attributes.FlagAttributes.parse(f)
    x_test, y_test = format_data(test_data)
    
    full_data = None
    with open(FULL_PATH(), 'r') as f:
        full_data = attributes.FlagAttributes.parse(f)
    x_full, y_full = format_data(full_data)
    
    model = RandomForestClassifier()
#    model = DecisionTreeClassifier()
#    model = MLPClassifier(solver='lbfgs', alpha=2.3, hidden_layer_sizes=(5, 2), random_state=0)
#    model = SVC()
#    model = NearestCentroid()
#    model = GaussianNB()

    model.fit(x_train, y_train)
    
    pred_train = [attributes.Religion(p) for p in model.predict(x_train)]
    correct = len([i for i in range(0, len(y_train)) if y_train[i] == pred_train[i]])
    print('training performance:\t', correct, '/', len(y_train), '\tratio:', round(correct / len(y_train), 2))
        
    pred_test = [attributes.Religion(p) for p in model.predict(x_test)]
    correct = len([i for i in range(0, len(y_test)) if y_test[i] == pred_test[i]])
    print('testing performance:\t', correct, '/', len(y_test), '\tratio:', round(correct / len(y_test), 2))
    
    pred_full = [attributes.Religion(p) for p in model.predict(x_full)]
    correct = len([i for i in range(0, len(y_full)) if y_full[i] == pred_full[i]])
    print('full performance:\t', correct, '/', len(y_full), '\tratio:', round(correct / len(y_full), 2))
    
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

