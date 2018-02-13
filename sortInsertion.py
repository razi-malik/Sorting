#!/usr/bin/env python

'''
Insertion Sort:

'''

def insertionSort(alist):
	for index in range(1, len(alist)):
		currentvalue = alist[index]
		position = index
		while position > 0 and alist[position - 1] > currentvalue:
			alist[position] = alist[position - 1]
			position = position - 1
		alist[position] = currentvalue

	return alist

testList = [1, 20, 30, 5, 7]

print 'The original list: ', testList
print 'The InsertionSort output: ', insertionSort(testList)



























