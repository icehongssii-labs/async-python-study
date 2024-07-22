import requests
import time 
import os
import threading
from concurrent.futures import ThreadPoolExecutor

def fetcher(params):
	session, url = params
	print(f"{os.getpid()} process | {threading.get_ident()} url: {url}")
	with session.get(url) as resp:
		return resp.text

def main():
	urls = ["https://www.naver.com", "https://www.google.com"] * 50
	executor = ThreadPoolExecutor(max_workers=10) # 최대 스레드 개수 
	with requests.Session() as session:
		params = [(session, url) for url in urls]
		list(executor.map(fetcher, params))
		# map은 제너레이터라서 리스트로 변환

if __name__ == '__main__':
	start = time.time()
	main()
	end = time.time()
	print(end-start, "소요시간")		
