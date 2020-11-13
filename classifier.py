#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sklearn.model_selection import cross_val_score, cross_val_predict
#from sklearn.model_selection import KFold
from sklearn.model_selection import StratifiedKFold
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

def NUM_FOLDS(): return 10

def format_data(data):
    return ([flag.attributes() for flag in data], [country.religion for country in data])

def main(args):
#    train_data = None
#    with open(TRAIN_PATH(), 'r') as f:
#        train_data = attributes.FlagAttributes.parse(f)
#    x_train, y_train = format_data(train_data)
    
#    test_data = None
#    with open(TEST_PATH(), 'r') as f:
#        test_data = attributes.FlagAttributes.parse(f)
#    x_test, y_test = format_data(test_data)
    
    full_data = None
    with open(FULL_PATH(), 'r') as f:
        full_data = attributes.FlagAttributes.parse(f)
    x_full, y_full = format_data(full_data)
    
    #train_x, train_y, test_x, test_y = (None, None, None, None)
    #train_x, train_y = (None, None)
    #with open(TRAIN_PATH(), 'r') as f:
    #    train_x, train_y = format_data(attributes.FlagAttributes.parse(f))

    train_i, test_i = next(StratifiedKFold(n_splits=3, shuffle=True).split(x_full, y_full))
    x_train = [x_full[i] for i in train_i]
    y_train = [y_full[i] for i in train_i]
    x_test = [x_full[i] for i in test_i]
    y_test = [y_full[i] for i in test_i]

    #train_index, test_index = kf.split(x_full)
    #print(train_index, test_index)

    model = RandomForestClassifier()
#    model = DecisionTreeClassifier()
#    model = MLPClassifier(solver='lbfgs', alpha=2.3, hidden_layer_sizes=(5, 2), random_state=0)
#    model = SVC()
#    model = NearestCentroid()
#    model = GaussianNB()

    skf = StratifiedKFold(n_splits=NUM_FOLDS(), shuffle=True)
    scores = []
    for train_index, test_index in skf.split(x_train, y_train):
        model.fit([x_train[i] for i in train_index], [y_train[i] for i in train_index])
        scores.append(model.score([x_train[i] for i in test_index], [y_train[i] for i in test_index]))
    
    #scores = cross_val_score(model, x_train, y_train, cv=10)
    #print(scores)

    #model.fit(x_train, y_train)
    
    #pred_train = [attributes.Religion(p) for p in model.predict(x_train)]
    #correct = len([i for i in range(0, len(y_train)) if y_train[i] == pred_train[i]])
    #print('training performance:\t', correct, '/', len(y_train), '\tratio:', round(correct / len(y_train), 2))
    
    print('Scoring of model for each iteration')
    print(scores)
    print('Mean of model iterations:', sum(scores)/len(scores))
        
    pred_test = [attributes.Religion(p) for p in model.predict(x_test)]
    #pred_test = [attributes.Religion(p) for p in cross_val_predict(model, x_test, y_test, cv=NUM_FOLDS())]
    correct = len([i for i in range(0, len(y_test)) if y_test[i] == pred_test[i]])
    print('testing performance:\t', correct, '/', len(y_test), '\tratio:', round(correct / len(y_test), 2))
    
    pred_full = [attributes.Religion(p) for p in model.predict(x_full)]
    correct = len([i for i in range(0, len(y_full)) if y_full[i] == pred_full[i]])
    print('full performance:\t', correct, '/', len(y_full), '\tratio:', round(correct / len(y_full), 2))
    
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

