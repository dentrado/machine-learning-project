__author__ = 'roc'

import csv
import mdp
import random
import scipy
import scipy.stats as stat

#################################################
#Stuff that is done elswhere
#################################################

#Guillaume part???
def split():
    return []


#################################################
#       PARAMETERS
#################################################
K = 10  #number of subsets
L = 10  #number of the classifiers                      #Random number, should find a good one!!


#gets the data headers
def get_headers():
    cr = csv.reader(open('training-data.csv', "r"), delimiter=";")
    row = cr.readline()
    return row

#returns the mean
def mean(X):
    return sum(X)/ float(len(X))

#bootstrap the data
def bootstrap(sample, samplesize = None, nsamples = 1000, statfunc = mean):
    """
    Arguments:
       sample - input sample of values
       nsamples - number of samples to generate
       samplesize - sample size of each generated sample
       statfunc- statistical function to apply to each generated sample.

    Performs resampling from sample with replacement, gathers
    statistic in a list computed by statfunc on the each generated sample.
    """
    if samplesize is None:
        samplesize=len(sample)
    print ("input sample = ",  sample)
    n = len(sample)
    X = []
    for i in range(nsamples):
        print ("i = ",  i,)
        resample = [sample[j] for j in stat.randint.rvs(0, n-1, size=samplesize)]
        x = statfunc(resample)
        X.append(x)
    return X

#Class confidence calculation
def class_confidence_calculation(L, D):         ### IT MAY NEED PARAMETERS!!!!!!!!
    aux = 0
    for item in D:
        aux += item
    return aux/L

random.seed([3]) #seting the random seed

Y = get_headers()
for i in Y:
    F = split()
    for j in K:
        #should return a number between 0 and Y.size()
        #The algorithm should delete a random subset of classes
        keepCols = []
        deletedCols = []
        for jj in K:
            if(random.randrange(1)==1): keepCols.append(jj) #every column has 50% to be deleted
            else: deletedCols.append(jj)
        #the 'p' means that's a prime
        Xijp = bootstrap(F[keepCols], 1, len(F)*0.75) #option 2 http://climateecology.wordpress.com/2013/08/19/r-vs-python-speed-comparison-for-bootstrapping/
        Cij = mdp.pca(Xijp)

        #arrangin the rotation matrix
        Ri = [len(Cij)][K]
        id=0
        for a in len(Cij):
            aux = 0
            for b in K:
                aux += Cij[a][b]
            if(id == a): Ri[a][a] = aux #does the diagonal
            ++id

        #It should have the same order but without some columns, so is ok

