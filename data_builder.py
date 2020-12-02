#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# reconstructs the indices produced by sampler.py into csv files

def FULL_PATH(): return 'data/attributes/flags.csv'
def TRAIN_PATH(): return 'sampler_test/train.csv'
def VALID_PATH(): return 'sampler_test/valid.csv'

def TRAIN_INDEX(): return 'sampler_test/train_indices.txt'
def VALID_INDEX(): return 'sampler_test/valid_indices.txt'

def reconstruct(index_path, output_path):
    indices = None
    with open(index_path, 'r') as f:
        indices = [int(l.strip()) for l in f]
    lines = None
    with open(FULL_PATH(), 'r') as f:
        lines = [l for i, l in enumerate(f) if i in indices]
    with open(output_path, 'w') as f:
        for l in lines:
            f.write(l)

def main(args):
    reconstruct(TRAIN_INDEX(), TRAIN_PATH())
    reconstruct(VALID_INDEX(), VALID_PATH())

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
