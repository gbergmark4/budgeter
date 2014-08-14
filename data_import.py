### data import module for budgeter
###
###by george bergmark
###
###takes in csv data and combines it with a common file, ensures there's no redundant entry.

import csv

COMMONFILE = 'new.csv'

def data_open(csvfile):
    '''csv file -> list of dictionary entries'''
    with open(csvfile) as new_file:
        new_entries = [each for each in csv.DictReader(new_file)]
    return new_entries

def combine_data(csvDictReaderList):
    COMMONFILE = 'new.csv'
    '''write new entries to csv file. *do not write header info or redundant entries*'''
    with open(COMMONFILE,'a') as main_list:
        writer = csv.DictWriter(COMMONFILE,[each for each in csvDictReaderList[0])
        writer.writerows(csvDictReaderList)
