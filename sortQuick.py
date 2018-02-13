#!/usr/bin/env python

'''
Quick Sort:

'''
def quickSort(alist):
    if len(alist) <= 1:
        return alist

    pivot = alist[0]
    less = []
    equal = []
    greater = []
    for each in alist:
        if each < pivot:
            less.append(each)
        elif each == pivot:
            equal.append(each)
        else:
            greater.append(each)
    return quickSort(less) + equal + quickSort(greater)
        
theList = [1, 20, 30, 5, 7]
output = [1, 5, 7, 20]

print 'The original list: ', theList
print 'The QuickSort output: ', quickSort(theList)






























