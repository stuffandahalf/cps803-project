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

#def TRAIN_PATH(): return 'data/attributes/train.csv'
#def TEST_PATH(): return 'data/attributes/test.csv'
def FULL_PATH(): return 'data/attributes/flags.csv'

#60-40 tests
#def TRAIN_PATH(): return 'data/attributes/6040/train.csv'
#def TEST_PATH(): return 'data/attributes/6040/valid.csv'

#70-30 tests
def TRAIN_PATH(): return 'data/attributes/7030/train.csv'
def TEST_PATH(): return 'data/attributes/7030/valid.csv'

#80-20 tests
#def TRAIN_PATH(): return 'data/attributes/8020/train.csv'
#def TEST_PATH(): return 'data/attributes/8020/valid.csv'

def NUM_FOLDS(): return 10

def format_data(data):
    return ([flag.attributes() for flag in data], [country.religion for country in data])

def main(args):
    full_data = None
    with open(FULL_PATH(), 'r') as f:
        full_data = attributes.FlagAttributes.parse(f)
    x_full, y_full = format_data(full_data)

    train_data = None
    with open(TRAIN_PATH(), 'r') as f:
        train_data = attributes.FlagAttributes.parse(f, skip_first=True)
    x_train, y_train = format_data(train_data)
    
    valid_data = None
    with open(TEST_PATH(), 'r') as f:
        valid_data = attributes.FlagAttributes.parse(f, skip_first=True)
    x_valid, y_valid = format_data(valid_data)

    model = RandomForestClassifier()
#    model = DecisionTreeClassifier()
#    model = MLPClassifier(solver='lbfgs', alpha=2.3, hidden_layer_sizes=(5, 2), random_state=0)
#    model = SVC()
#    model = NearestCentroid()
#    model = GaussianNB()

    skf = StratifiedKFold(n_splits=NUM_FOLDS())#, shuffle=True)
    scores = []
    for train_index, test_index in skf.split(x_train, y_train):
        model.fit([x_train[i] for i in train_index], [y_train[i] for i in train_index])
        scores.append(model.score([x_train[i] for i in test_index], [y_train[i] for i in test_index]))

    print('Scoring of model for each iteration')
    print(scores)
    print('Mean of model iterations:', sum(scores)/len(scores))
        
    pred_test = [attributes.Religion(p) for p in model.predict(x_valid)]
    #pred_test = [attributes.Religion(p) for p in cross_val_predict(model, x_test, y_test, cv=NUM_FOLDS())]
    correct = len([i for i in range(0, len(y_valid)) if y_valid[i] == pred_test[i]])
    print('testing performance:\t', correct, '/', len(y_valid), '\tratio:', round(correct / len(y_valid), 2))
    
    pred_full = [attributes.Religion(p) for p in model.predict(x_full)]
    correct = len([i for i in range(0, len(y_full)) if y_full[i] == pred_full[i]])
    print('full performance:\t', correct, '/', len(y_full), '\tratio:', round(correct / len(y_full), 2))
    
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

