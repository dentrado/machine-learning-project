__author__ = 'roc'

import csv

cr = csv.reader(open('dataset-har-PUC-Rio-ugulino.csv', "r"), delimiter=";")
test = csv.writer(open('test.csv', "w"))
nonTest = csv.writer(open('non-test.csv', "w"))

i = 0


for row in cr:
    if(i==0):
        nonTest.writerow(row)
        test.writerow(row)
    else:
        if(i%3 != 0): nonTest.writerow(row)
        else: test.writerow(row)
    i+=1