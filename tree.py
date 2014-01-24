__author__ = 'martin'

import numpy as np

class Tree(object):
    def __init__(self, left, right, feature, split, data):
        self.left = left
        self.right = right
        self.feature = feature
        self.split = split
        self.data = data

    def print(self):
        print(self._str(0))

    def _str(self,depth):
        if self.data != None:
            return str(self.data).replace("\n",",")
        else:
            return  str(self.feature)        + ":\n" +  \
                   "\t"*depth + "+---" + self.left._str(depth+1)  + "\n" +   \
                   "\t"*depth + "+---" + self.right._str(depth+1)

def get_classes(samples):
    """returns the class column. (assumes the class is in the last column)"""
    return samples[:,np.size(samples, axis=1) - 1]

def sort_on_col(samples, col_idx):
    return samples[samples[:,col_idx].argsort()]

def all_same_class(classes):
    return np.max(classes) == np.min(classes)

def entropy(classes):
    counts = np.bincount(classes)
    tot    = classes.size
    probs  = counts[np.nonzero(counts)] / tot
    if probs.size == 0:
        return 0
    else:
        return - np.sum(probs * np.log2(probs))

def split(arr, split_idx):
    return arr[:split_idx], arr[split_idx:]

def info_gain(classes, split_idx):
    if split_idx < 1 or split_idx >= classes.size:
        return 0
    oldH = entropy(classes)
    left, right = split(classes, split_idx)
    newH = ( left.size / classes.size) * entropy(left) + \
           (right.size / classes.size) * entropy(right)
    return oldH - newH

def best_split(classes):
    idx = max(range(classes.size), key=lambda i: info_gain(classes, i))
    return idx, info_gain(classes,idx)

def best_feature_and_split(samples):
    feature_cols = range(np.size(samples, axis=1) - 1)
    splits = [(i, best_split(get_classes(sort_on_col(samples, i)))) for i in feature_cols]
    feature, (split, gain) = max(splits, key=lambda x: x[1][1]) # max by info_gain
    return feature, split, gain

# s = num of samples
# p = num of features
# samples:
# class1, x11, x21, ..., xf1
# class2, x21
#  .       .
#  .       .
#  .       .
# classS  xs1
def c45(samples) -> Tree:
    if(all_same_class(get_classes(samples))):
        return Tree(None, None, None, None, samples)
    #num_samples = np.size(samples, axis=0)
    feature, split_idx, gain = best_feature_and_split(samples)
    left, right = split(sort_on_col(samples, feature), split_idx)
    split_point = (left[-1] + right[0]) / 2.0
    return Tree(c45(left), c45(right), feature, split_point, None)

testdata = np.array([[1,1,0],
                     [2,2,1],
                     [3,1,0],
                     [4,2,1],
                     [2,1,2],
                     [2,2,2],
                     [3,1,3],
                     [3,2,3]])
