__author__ = 'roc'

import csv
import numpy as np

def modify_row(csv, row, i):
	woman = 0
	aux = []
	for item in row:
		if(item == 'Woman'): 
			woman = 1
			item = 0
		if(item == 'Man'):
			item = 1
		if(item == '?'):
			if(woman == 1): 
				item = 1
			else:
				item = 0
		
		item = [item]
		aux = np.append(aux, item, 1)
		aux.shape
	
	csv.writerow(aux)

cr = csv.reader(open('dataset-har-PUC-Rio-ugulino.csv', "r"), delimiter=";")
test = csv.writer(open('test.csv', "w"))
nonTest = csv.writer(open('training-data.csv', "w"))

i = 0


for row in cr:
	if(i==0):
		nonTest.writerow(row+['woman'])
		test.writerow(row+['woman'])

	if(i != 0):
		if(i%3==0): modify_row(test, row+['?'], i)
		else: modify_row(nonTest, row+['?'], i)
	i+=1