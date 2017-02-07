import random 

def qSort(A):
	_qSort(A, 0, len(A)-1)

def _qSort(A, lo, h):
	if lo < h:
		p = partition(A,lo,h)
		_qSort(A, lo, p - 1)
		_qSort(A, p + 1, h)

def partition(A, lo, h):
	p = random.randint(lo,h)
	A[p], A[h] = A[h], A[p]
	j = lo

	for i in xrange(lo,h):
		if A[i] < A[h]:
			A[i], A[j] = A[j], A[i] 
			j += 1
	# after loop: A[<j] <= A[j] <= A[>j]

	A[h], A[j] = A[j], A[h]

	return j

alist = [54,26,93,17,77,31,44,55,20]
qSort(alist)
print(alist)