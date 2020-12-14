# Final project for CPS803
This is a flag classifier built from two seperate models. The goal is to
categorize countries by the dominant religion of the population.

Licensed under GPLv3. You should have received a copy of the license with this
file.

## Model 1. Extracting flag attribute information
Built using a convolutional neural network
Files:
- flag_labeler.ipynb

Inputs:
- Flag images

Outputs:
- Flag attributes

## Model 2. Categorizing flag attributes into one of 8 religion groups.
Built using a random forest classifier trained with k-fold cross validation
Files:
- attributes.py
- classifier.py

Inputs:
- Flag atributes

Outputs:
- One of eight religion classes.

Required libraries:
- keras
- scikit
