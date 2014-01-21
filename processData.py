__author__ = 'guillaume'


import numpy as np


def splitData(X, k): #split the data W into k disjoint subsets of the same size reogonized the data
    nb_of_point = X.shape[0]
    permuted_data = np.matrix(np.zeros(X.shape))
    size_cluster = nb_of_point // k

    if (nb_of_point % k != 0):
        print "k should devise th number of point "
        return

    print "Split the data into  %i substets" %(k)
    permutation = np.random.permutation(range(nb_of_point))
    hash_list = np.zeros(nb_of_point)

    counter=0
    subset = 0
    for it in permutation:
        hash_list[it]= subset
        permuted_data[ counter, :] = X[ it , :]
        counter +=1
        if (counter % size_cluster == 0):
            subset += 1

    return (permuted_data , permutation , hash_list)

def reorder_data(permutation , permuted_data):
    original_data = np.matrix(np.zeros(permuted_data.shape))
    for it in range(len(permuted_data)):
        original_data[ permutation[it],: ] = permuted_data[ it , :]
    return original_data

def eliminate_class(original_data, class_to_remove):
    n= original_data.shape[1]
    percistance_list = np.zeros(n)

    mask = original_data[:,n-1] != class_to_remove
    #for i in range(original_data.shape[0]):
   #     if (original_data[:,n-1] != class_to_remove, axis = 1)[i]):
     #       percistance_list[i]=1
     #       processed_data = np.append(processed_data,original_data[i,:])
    print original_data[mask]
    return (original_data[mask],mask)

def bootstrap(data, alpha):
    #Returns bootstrap samples of size alpha.
    n = data.shape[0]
    m= np.floor(alpha*n)
    boostraped_index = np.random.randint(0,n,size =m)
    bootstraped_data = data[:,boostraped_index]
    return (bootstraped_data, boostraped_index)


