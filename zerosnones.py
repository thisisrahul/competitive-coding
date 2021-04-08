#!/usr/bin/env python3

import time 

saves = 0

class Solution1:
	def findMaxForm(self, strs, m: int, n: int) -> int:
		mnns = {}
		for string in strs:
			if string not in mnns:
				zeros = 0
				ones = 0
				for ch in string:
					if ch == '0':
						zeros += 1
					else:
						ones += 1
				mnns[string] = (zeros, ones,)
		N = len(strs)
		self.arr = [[[-1]*(m+1) for i in range(n+1)] for j in range(N+1)]
		return self.zeros_n_ones(m, n, N-1, mnns)

	def zeros_n_ones(self, m, n, N, mnns):
		if N < 0:
			# see if this is redundant
			return 0
		zeros, ones = mnns[strs[N]]
		if N == 0:
			if zeros <= m and ones <= n:
				return 1
			return 0
		if self.arr[N][n][m] != -1:
			global saves
			saves += 1
			return self.arr[N][n][m]
		if zeros <= m and ones <= n:
			inclusive = self.zeros_n_ones(m-zeros, n-ones, N-1, mnns) + 1
		else:
			inclusive = 0
		exclusive = self.zeros_n_ones(m, n, N-1, mnns)
		self.arr[N][n][m] = max(inclusive, exclusive)
		return self.arr[N][n][m]


class Solution:
	def findMaxForm(self, strs, m: int, n: int) -> int:
		mnns = {}
		for string in strs:
			if string not in mnns:
				zeros = 0
				ones = 0
				for ch in string:
					if ch == '0':
						zeros += 1
					else:
						ones += 1
				mnns[string] = (zeros, ones,)
		N = len(strs)
		self.strs = strs
		self.results = {}
		return self.zeros_n_ones(m, n, N-1, mnns)

	def zeros_n_ones(self, m, n, N, mnns):
		global saves
		if N < 0:
			# see if this is redundant
			return 0
		zeros, ones = mnns[self.strs[N]]
		if N == 0:
			if zeros <= m and ones <= n:
				return 1
			return 0
		if N in self.results and f"{m}_{n}" in self.results[N]:
			saves += 1
			return self.results[N][f"{m}_{n}"]
		#if f"{m}_{n}" in self.results and N in self.results[f"{m}_{n}"]:
		#	return self.results[f"{m}_{n}"][N]
		if zeros <= m and ones <= n:
			if N-1 in self.results and f"{m-zeros}_{n-ones}" in self.results[N-1]:
				saves += 1
				res = self.results[N-1][f"{m-zeros}_{n-ones}"]
			else:
				res = self.zeros_n_ones(m-zeros, n-ones, N-1, mnns)
			inclusive = res + 1
		else:
			inclusive = 0
		if N-1 in self.results and f"{m}_{n}" in self.results[N-1]:
			saves += 1
			res = self.results[N-1][f"{m}_{n}"]
		else:
			res = self.zeros_n_ones(m, n, N-1, mnns)
		exclusive = res
		self.results[N] = {}
		self.results[N][f"{m}_{n}"] = max(inclusive, exclusive)
		return self.results[N][f"{m}_{n}"]

#strs = ["10","0001","111001","1","0"]
#m = 5
#n = 3

#strs = ["0","11","1000","01","0","101","1","1","1","0","0","0","0","1","0","0110101","0","11","01","00","01111","0011","1","1000","0","11101","1","0","10","0111"]
strs = ["0","11","1000","01","0","101","1","1","1","0","0","0","0","1"]
m = 9
n = 80

#strs = ["011","1","11","0","010","1","10","1","1","0","0","0","01111","011","11","00","11","10","1","0","0","0","0","101","001110","1","0","1","0","0","10","00100","0","10","1","1","1","011","11","11","10","10","0000","01","1","10","0"]
#m = 44
#n = 39
start_time = time.time()
s = Solution1()
print(s.findMaxForm(strs, m, n))
print(f"{time.time() - start_time}")
print(saves)

N = len(strs)
for i in range(N+1):
	for j in range(n+1):
		for k in range(m+1):
			if s.arr[i][j][k] > 0:
				print(f"{i}: {j}_{k} {s.arr[i][j][k]}", end=" ")

start_time = time.time()
s = Solution()
saves = 0
print("Using dictionary for memoization")
print(s.findMaxForm(strs, m, n))
print(f"{time.time() - start_time}")
print(s.results)
print(saves)