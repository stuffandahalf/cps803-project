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
