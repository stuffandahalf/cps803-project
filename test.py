#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sklearn.ensemble as skle
import attributes

def ATTRIBUTE_PATH(): return 'data/attributes/flags.csv'

def main(args):
    data = None
    with open(ATTRIBUTE_PATH(), 'r') as f:
        data = attributes.FlagAttributes.parse(f)
    print([att.__dict__ for att in data])
    model = skle.RandomForestClassifier()
    print(model)
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

