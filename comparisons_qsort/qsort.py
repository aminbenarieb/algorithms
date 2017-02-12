import random 

hw_filepath = "_32387ba40b36359a38625cbb397eee65_QuickSort.txt"

def swap(A, l, r):
	A[l], A[r] = A[r], A[l]

def median_pivot(A, lo, h):
	mid_index = (lo+h)/2

	f = A[lo]
	m = A[mid_index]
	l = A[h]

	if f <= m <= l or l <= m <= f :
		result = mid_index
	elif m <= f <= l or l <= f <= m:
		result = lo
	elif f <= l <= m or m <= l <= f:
		result = h

	# print "Choosed element "+ str(A[result]) + " from elements: " + str([f,m,l])
	return result

def arr_from_file(filepath):
	return [int(line.rstrip('\n')) for line in open(filepath)]

# -----------

def qSort(A):
	return _qSort(A, 0, len(A)-1)

def _qSort(A, lo, h):
	if not hasattr(_qSort, "cmp_count"):
		_qSort.cmp_count = 0

	if lo < h:
		_qSort.cmp_count += h-lo
		p = concrete_partition(A,lo,h)
		_qSort(A, lo, p - 1)
		_qSort(A, p + 1, h)

	return _qSort.cmp_count

def concrete_partition(A, lo, h):
	# i = random.randint(lo,h)
	# i = lo
	# i = h
	i = median_pivot(A, lo, h)
	swap(A, i, lo)
	return partition(A, lo, h)

def partition(A, p, h):
	pivot_value = A[p]
	i = p+1

	for j in xrange(p+1,h+1):
		if A[j] <= pivot_value:
			A[j], A[i] = A[i], A[j] 
			i += 1

	A[p], A[i-1] = A[i-1], A[p]

	return i-1

# -----------

alist = [3, 2, 9, 6, 5, 7, 8]
alist = arr_from_file(hw_filepath)
print(qSort(alist))
# print(alist)
