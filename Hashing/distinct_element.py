# Python3 program to count distinct
# elements in every window of size K

import math as mt

# Counts distinct elements in window
# of size K


def countWindowDistinct(win, K):

	dist_count = 0

	# Traverse the window
	for i in range(K):

		# Check if element arr[i] exists
		# in arr[0..i-1]
		j = 0
		while j < i:
			if (win[i] == win[j]):
				break
			else:
				j += 1
		if (j == i):
			dist_count += 1

	return dist_count


# Counts distinct elements in all
# windows of size k
def countDistinct(arr, N, K):

	# Traverse through every window
	for i in range(N - K + 1):
		print(countWindowDistinct(arr[i:K + i], K))


# Driver's Code
if __name__=='__main__':
arr = [1, 2, 1, 3, 4, 2, 3]
K = 4
N = len(arr)

# Function call
countDistinct(arr, N, K)

