#!/usr/bin/env python

'''
Merge Sort:

'''
# Code for merging the arrays
def merge(a, b):
    """ Function to merge two arrays """
    c = []
    while len(a) != 0 and len(b) != 0:
        if a[0] < b[0]:
            c.append(a[0])
            a.remove(a[0])
        else:
            c.append(b[0])
            b.remove(b[0])
    if len(a) == 0:
        c += b
    else:
        c += a
    #print 'The current c list is: ', c
    return c

# Code for merge sort
def mergeSort(alist):
    """ Function to sort an array using merge sort algorithm """
    if len(alist) <= 1:
        return alist
    else:
        mid = len(alist)/2
        a = mergeSort(alist[:mid])
        b = mergeSort(alist[mid:])
        #print 'current A - {0} and B - {1}'.format(a, b)
        return merge(a, b)

theList = [1, 20, 30, 5, 7]
output = [1, 5, 7, 20]

print 'The original list: ', theList
print 'The MergeSort output: ', mergeSort(theList)






























