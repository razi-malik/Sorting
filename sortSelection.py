#!/usr/bin/env python

'''
Selection Sort:

'''

def selectionSort(alist):
	for passnum in range(len(alist)):
		minPosition = passnum
		for i in range(passnum+1, len(alist)):
			if alist[minPosition] > alist[i]:
				minPosition = i
		temp = alist[passnum]
		alist[passnum] = alist[minPosition]
		alist[minPosition] = temp
	return alist

testList = [1, 20, 30, 5, 7]

print 'The original list: ', testList
print 'The selectionSort output: ', selectionSort(testList)























