#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# randomly generates 750 variations on the dataset split and saves the
# indices of the best splits
# to be used in tandem with data_builder.py

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

def NUM_FOLDS(): return 10
#def DATASET_VERSION(): return 4 # reached 79%
def DATASET_VERSION(): return 8

def format_data(data):
    return ([flag.attributes() for flag in data], [country.religion for country in data])


def classify(x_train, y_train, x_valid, y_valid):
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
    
    pred_valid = [attributes.Religion(p) for p in model.predict(x_valid)]
    correct = len([i for i in range(0, len(y_valid)) if y_valid[i] == pred_valid[i]])
    performance = correct/len(pred_valid)
    
    return (model, scores, performance)#, performance_full)

def main(args):
    full_data = None
    with open(FULL_PATH(), 'r') as f:
        full_data = attributes.FlagAttributes.parse(f)
    x_full, y_full = format_data(full_data)

    best_valid_perf = 0
    best_dataset = None

    for i in range(0, 750):
        print('\r%d' % i, end='')
        skf = StratifiedKFold(n_splits=4, shuffle=True)
        scores = []
        train_index, valid_index = next(skf.split(x_full, y_full))
        
        x_train = [x_full[j] for j in train_index]
        y_train = [y_full[j] for j in train_index]
        x_valid = [x_full[j] for j in valid_index]
        y_valid = [y_full[j] for j in valid_index]
        
        model, scores, performance = classify(x_train, y_train, x_valid, y_valid)
        if best_valid_perf < performance:
            print('\nnew best performance', performance)
            best_valid_perf = performance
            best_dataset = { 'train': train_index, 'valid': valid_index}
    print('')

    with open('sampler_test/train_indices.txt', 'w') as f:
        for i in best_dataset['train']:
            f.write('%d' % i)
            f.write('\n')
    
    with open('sampler_test/valid_indices.txt', 'w') as f:
        for i in best_dataset['valid']:
            f.write('%d' % i)
            f.write('\n')

    '''print('Scoring of model for each iteration')
    print(scores)
    print('Mean of model iterations:', sum(scores)/len(scores))
        
    pred_test = [attributes.Religion(p) for p in model.predict(x_valid)]
    #pred_test = [attributes.Religion(p) for p in cross_val_predict(model, x_test, y_test, cv=NUM_FOLDS())]
    correct = len([i for i in range(0, len(y_valid)) if y_valid[i] == pred_test[i]])
    print('testing performance:\t', correct, '/', len(y_valid), '\tratio:', round(correct / len(y_valid), 2))
    
    pred_full = [attributes.Religion(p) for p in model.predict(x_full)]
    correct = len([i for i in range(0, len(y_full)) if y_full[i] == pred_full[i]])
    print('full performance:\t', correct, '/', len(y_full), '\tratio:', round(correct / len(y_full), 2))'''
    
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

