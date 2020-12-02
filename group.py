#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import attributes as a

def FULL_PATH(): return 'data/attributes/flags.csv'
def TRAIN_PATH(): return 'data/attributes/forced/train.csv'
def VALID_PATH(): return 'data/attributes/forced/valid.csv'

def group(data):
	return {k: [d.name for d in data if d.religion == k] for k in a.Religion}

def main(args):
	full_data = None
	with open(FULL_PATH(), 'r') as f:
		full_data = a.FlagAttributes.parse(f)
	
	train_data = None
	with open(TRAIN_PATH(), 'r') as f:
		train_data = a.FlagAttributes.parse(f)
	
	valid_data = None
	with open(VALID_PATH(), 'r') as f:
		valid_data = a.FlagAttributes.parse(f)
	
	full_groups = group(full_data)
	train_groups = group(train_data)
	valid_groups = group(valid_data)
	
	rels = [a.Religion.BUDDHIST, a.Religion.HINDU, a.Religion.OTHER_CHRISTIAN]
	
	print('VALIDATION')
	for r in rels:
		print(r.name, ':', valid_groups[r])
	print('')
	print('TRAIN')
	for r in rels:
		print(r.name, ':', train_groups[r])
	print('')
	
	for r in a.Religion:
		print(r.name, ':', len(valid_groups[r]), '\t', len(train_groups[r]))
	
	#for g in groups.keys():
		#print(g, ':', len(groups[g]))
	
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
    
