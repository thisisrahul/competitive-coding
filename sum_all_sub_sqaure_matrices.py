#!/usr/bin/env python3
counter=0


def set_sum_k_strips(arr, k):
	global counter
	n = len(arr)
	sum_strips = [[None] * n for i in range(n-k+1)]
	# populate the fist N vertical k-strips across
	for col in range(n):
		Sum = 0
		for row in range(k):
			counter += 1
			Sum += arr[row][col]
		sum_strips[0][col] = Sum
	# populate the rest of the vertical K-strips using the previous results and next and last element
	for col in range(n):
		for row in range(1, n-k+1):
			counter += 1
			sum_strips[row][col] = sum_strips[row-1][col] + arr[row+k-1][col] - arr[row-1][col]
	return sum_strips

def find_sum(arr, k):
	k_strips = set_sum_k_strips(arr, k)
	global counter
	# find sum of the first k * k square matrix from top left corner
	n = len(arr)
	Sums = [[None] * (n-k+1) for i in range(n-k+1)]
	for row in range(n-k+1):
		Sum = 0
		for col in range(k):
			counter += 1
			Sum += k_strips[row][col]
		Sums[row][0] = Sum
	for row in range(n-k+1):
		for col in range(1,n-k+1):
			counter += 1
			Sums[row][col] = Sums[row][col-1] +k_strips[row][col+k-1]-k_strips[row][col-1]
	return Sums

def printm(arr):
	for row in arr:
		for col in row:
			print(col, end=" ")
		print()


arr = [[1, 1, 1, 1, 1],
		[2, 2, 2, 2, 2],
		[3, 3, 3, 3, 3],
		[4, 4, 4, 4, 4],
		[5, 5, 5, 5, 5]]
k = 3

Sums = find_sum(arr, k_strips, k)
printm(Sums)
print(f"counter = {counter}")