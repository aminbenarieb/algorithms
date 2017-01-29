hw_filepath = "_bcb5c6658381416d19b01bfc1d3993b5_IntegerArray.txt"

def arr_from_file(filepath):
	return [int(line.rstrip('\n')) for line in open(filepath)]


def split_inversion(b,c):
	# print(str(b) + " m " + str(c))
	n, m = len(b), len(c)
	inv, i, j = 0,0,0
	d = []
	while (i < n and j < m):
		if b[i] < c[j]:
			d.append(b[i])
			i += 1
		elif b[i] > c[j]:
			d.append(c[j])
			j += 1
			# ******
			inv += (n+m)/2 - i 
			# ******
		else:
			d.append(b[i])
			d.append(c[j])
			j += 1
			i += 1


	while i < n:
		d.append(b[i])
		i += 1
	while j < m:
		d.append(c[j])
		j += 1

	return d, inv


def inversion(a):
	if len(a) <= 1:
		return a, 0

	mid_ind = len(a)/2
	b, x = inversion(a[:mid_ind])
	c, y = inversion(a[mid_ind:])
	a, z = split_inversion(b,c)

	return a, x + y + z


a = [6, 5, 4, 3, 2, 1]


print("\n")
print(inversion(arr_from_file(hw_filepath)))
# print(inversion(a))
