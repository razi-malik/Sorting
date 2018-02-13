#!/usr/bin/env python

'''
Bubble Sort:

'''

def bubbleSort(alist):
	for passnum in range(len(alist)-1, 0, -1):
		for i in range(passnum):
			if alist[i] > alist[i + 1]: 
				temp = alist[i]
				alist[i] = alist[i+1]
				alist[i+1] = temp

	return alist

testList = [1, 20, 5, 7]

print 'The original list: ', testList
print 'The BubbleSort output: ', bubbleSort(testList)



























