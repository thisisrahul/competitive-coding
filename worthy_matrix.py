#!/usr/bin/env python3
avg = []
rowsum = []
colsum = []
counter = 0

def init_sums(arr, N, M):
	global rowsum
	global colsum
	rowsum = [[0]*M for i in range(N)]
	colsum = [[0]*M for i in range(N)]
	for i in range(N-1, -1, -1):
		S = 0
		for j in range(M-1, -1, -1):
			S += arr[i][i]
			rowsum[i][j] = S
	for i in range(M-1, -1, -1):
		S = 0
		for j in range(N-1, -1, -1):
			S += arr[i][i]
			colsum[i][j] = S
	return rowsum, colsum

def is_worthy(arr, K, row, col, k):
	global counter
	Sum = 0
	N = len(arr)
	M = len(arr[0])
	if avg[k-1][row][col] != -1:
		Sum = rowsum[row-k+1][col-k+1]
		Sum += colsum[row-k+1][col-k+1]
		Sum -= arr[row-k+1][col-k+1]
		# for i in range(row-k+1, row+1):
		# 	counter += 1
		# 	Sum += arr[i][col-k+1]
		# for i in range(col-k+1, col+1):
		# 	counter += 1
		# 	Sum += arr[row-k+1][i]
		# Sum -= arr[row-k+1][col-k+1]
		average = (avg[k-1][row][col]*(k-1)*(k-1) + Sum)/(k*k)
		# print(f"Sum - {Sum}, avg[k-1][row][col]*(k-1)*(k-1) = {avg[k-1][row][col]*(k-1)*(k-1)}")
		# print(f"average exists! prev average = {avg[k-1][row][col]}")
	elif row < N-1 and avg[k][row+1][col] != -1:
		if k != 1:
			print("prev not known")
		Sum = avg[k][row+1][col]*k*k
		for i in range(col-k+1, col+1):
			counter += 2
			Sum -= arr[row+1][i]
			Sum += arr[row-k+1][i]
		average = Sum/(k*k)
	elif col < M-1 and avg[k][row][col+1] != -1:
		if k != 1:
			print("prev not known")
		Sum = avg[k][row][col+1]*k*k
		for i in range(row-k+1, row+1):
			counter += 2
			Sum -= arr[i][col+1]
			Sum += arr[i][col-k+1]
		average = Sum/(k*k)
	else:
		if k != 1:
			print("prev not known")
		for i in range(row-k+1,row+1):
			for j in range(col-k+1, col+1):
				counter += 1
				Sum +=  arr[i][j]
	## # print(f"Sum = {Sum}, row = {row}, col={col}")
		average = Sum/(k*k)
	## print(f"row = {row}, col = {col}, k = {k}")
	avg[k][row][col] = average
	# print(f"avg = {average}, row = {row}, col={col}, k = {k}")
	return average >= K

def find_worthy(arr, K):
	global counter
	N = len(arr)
	M = len(arr[0])
	limit = min(M, N)
	Count = 0
	if arr[0][0] >= K:
		for k in range(1, limit):
			Count += (M-k+1)*(N-k+1)
		return Sum
	if arr[N-1][M-1] < K:
		return 0	
	init_sums(arr, N, M)
	top = [-1] * M
	left = -1
	for k in range(1, limit+1):
		# print(f" k = {k}")
		col = M-1
		while col > left and col >= k-1:
			row = N-1
			while  row > top[col] and row >= k-1:
				# counter += 1
				if is_worthy(arr, K, row, col, k):
					# print(f"col = {col}, row = {row}, k = {k}")
					Count += 1
				else:
					if row == N-1:
						left = col
					else:
						top[col] = row
					# print(f"Not worthy! col = {col}, row = {row}, k = {k}")
					# # print(f" left = {left}, top = {top}")
					break
				row -= 1
			col -= 1
		# print(avg)
		## print(f"k = {k}, top = {top}")
	return Count

T = int(input())
while T > 0:
	N,M,K = list(map(int, input().split()))
	arr = []
	for i in range(N):
		arr.append(list(map(int, input().split())))
		limit = min(M, N)
		avg = [[[-1] * M for i in range(N)]]*(limit+1)
	#init_sums(arr, N, M)
	print(find_worthy(arr, K))
	T -= 1

#print(counter)