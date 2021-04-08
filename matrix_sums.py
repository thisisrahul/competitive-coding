#!/usr/bin/env python3

# An efficient Python3 program to find sum
# of all subsquares of size k x k

# A O(n^2) function to find sum of all
# sub-squares of size k x k in a given
# square matrix of size n x n
counter = 0

def printSumTricky(mat, k):
	global n
	global counter
	
	# k must be smaller than or
	# equal to n
	if k > n:
		return

	# 1: PREPROCESSING
	# To store sums of all strips of size k x 1
	stripSum = [[None] * n for i in range(n)]

	# Go column by column
	for j in range(n):
		
		# Calculate sum of first k x 1
		# rectangle in this column
		Sum = 0
		for i in range(k):
			counter += 1
			Sum += mat[i][j]
		stripSum[0][j] = Sum

		# Calculate sum of remaining rectangles
		for i in range(1, n - k + 1):
			counter += 1
			Sum += (mat[i + k - 1][j] -
					mat[i - 1][j])
			stripSum[i][j] = Sum

	# 2: CALCULATE SUM of Sub-Squares
	# using stripSum[][]
	for i in range(n - k + 1):
		
		# Calculate and prsum of first
		# subsquare in this row
		Sum = 0
		for j in range(k):
			counter += 1
			Sum += stripSum[i][j]
		print(Sum, end = " ")

		# Calculate sum of remaining squares
		# in current row by removing the leftmost
		# strip of previous sub-square and adding
		# a new strip
		for j in range(1, n - k + 1):
			counter += 1
			Sum += (stripSum[i][j + k - 1] -
					stripSum[i][j - 1])
			print(Sum, end = " ")

		print()

# Driver Code
n = 5
mat = [[1, 1, 1, 1, 1],
	[2, 2, 2, 2, 2],
	[3, 3, 3, 3, 3],
	[4, 4, 4, 4, 4],
	[5, 5, 5, 5, 5]]
k = 3
printSumTricky(mat, k)

# This code is contributed by PranchalK

print(f"counter = {counter}")