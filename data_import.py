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

def combine_data(new_entries):
	'''the tricky one. combine old data and new data 
	into one big file. remove any redundant entries'''
	with open(COMMONFILE,'rb') as old_list:
		old_entries = [each for each in csv.DictReader(old_list)]
	for new in new_entries:
		for old in old_entries:
			if new == old:
				new_entries.pop(new_entries.index(new))
	return new_entries + old_entries



def write_data(csvDictReaderList):
    '''write all entries to csv file. Redundant entries should be removed by now'''
    with open(COMMONFILE,'wb') as main_list:
        writer = csv.DictWriter(main_list, [each for each in csvDictReaderList[0]])
        writer.writeheader()
        writer.writerows(csvDictReaderList)
