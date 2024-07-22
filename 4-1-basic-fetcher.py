import requests
import time

def fetcher(session:requests.Session, url:str):	
	with session.get(url)  as resp:
		return resp.text[:10]

def main():
	urls = ["https://www.naver.com", "https://www.google.com"] * 10

	with requests.Session() as session:
		res = [fetcher(session, url) for url in urls]
	print(res)
	

if __name__ == '__main__':
	start = time.time()
	main()
	end = time.time()
	print(end-start, "소요시간")