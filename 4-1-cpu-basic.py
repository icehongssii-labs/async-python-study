import time
import os
import threading

nums = [50, 63, 32]

def cpu_bound_func(num: int):
	print(f"{os.getpid()} process | {threading.get_ident()} thread: {num}")	
	total = 1
	numbers = range(1, num)
	for i in numbers:
		for j in numbers:
			for k in numbers:
				total *= i*j*k
	return total 

def main():
    for num in nums:
    	cpu_bound_func(num)


if __name__ == '__main__':
	start = time.time()
	main()
	end = time.time()
	print(end-start, "< 소요시")