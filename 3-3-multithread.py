import os 
import threading
import time

import requests


def fetcher(session:requests.Session, url:str):	
	print(f"{os.getpid()} process | {threading.get_ident()} url: {url}")
	# pid = 프로세스id
	# 
	with session.get(url)  as resp:
		return resp.text[:10]

def main():
	urls = ["https://www.naver.com","https://www.google.com"] * 50

	with requests.Session() as session:
		res = [fetcher(session, url) for url in urls]
	

if __name__ == '__main__':
	start = time.time()
	main()
	end = time.time()
	print(end-start, "소요시간")