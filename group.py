#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# SPDX-License-Identifer: GPL-3.0-only

# Copyright (C) 2020 Gregory Norton
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, version 3.
# 
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along with
# this program. If not, see <https://www.gnu.org/licenses/>.

# Groups the dataset by religion to perform analysis and transformations

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
    
