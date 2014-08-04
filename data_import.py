### data import module for budgeter
###
###by george bergmark
###
###takes in csv data and combines it with a common file, ensures there's no redundant entry.

import csv

def data_open(csvfile):
    '''csv file -> list of dictionary entries'''
    with open(csvfile) as new_file:
        new_entries = [each for each in csv.DictReader(new_file)]
    return new_entries


