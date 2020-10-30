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
def ATTRIBUTE_PATH(): return 'data/attributes/flags.csv'

def format_data(data):
    return ([flag.attributes() for flag in data], [country.religion for country in data])

def main(args):
    train_data = None
    with open(TRAIN_PATH(), 'r') as f:
        train_data = attributes.FlagAttributes.parse(f)
#    model = DecisionTreeClassifier()
#    model = MLPClassifier(solver='lbfgs', alpha=2.3, hidden_layer_sizes=(5, 2), random_state=0)
#    model = SVC()
#    model = NearestCentroid()
    model = RandomForestClassifier()
#    model = GaussianNB()
    x_train, y_train = format_data(train_data)
    model.fit(x_train, y_train)

    full_data = None
    with open(ATTRIBUTE_PATH(), 'r') as f:
        full_data = attributes.FlagAttributes.parse(f)
    x_full, y_full = format_data(full_data)
    y_pred = [attributes.Religion(p) for p in model.predict(x_full)]

    #print(y_pred)
    correct = 0
    for i in range(0, len(full_data)):
        #print('%s\treal: %s\tpred: %s' % (full_data[i].name, str(y_full[i]), str(y_pred[i])))
        if full_data[i].religion != y_pred[i]:
            print('%s\t\treal: %s\t\tpred: %s' % (full_data[i].name, str(full_data[i].religion), str(y_pred[i])))
        else:
            correct += 1
    print('%d/%d' % (correct, len(full_data)))
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

