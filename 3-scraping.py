from bs4 import BeautifulSoup as bs
import aiohttp
import asyncio
import time

BASE_URL = "https://bjpublic.tistory.com/category/%EC%A0%84%EC%B2%B4%20%EC%B6%9C%EA%B0%84%20%EB%8F%84%EC%84%9C"


async def fetcher(session, url):
	async with session.get(url) as resp:
		html = await resp.text()
		soup = bs(html, "html.parser")
		book_list = soup.find_all("div", "cont_thumb")
		for book in book_list:
			title = book.find("p", "txt_thumb")
			if title:
				print(title.text)

async def main():
	urls = [f"{BASE_URL}?page={i}" for i in range(1,10)]
	async with aiohttp.ClientSession() as session: 
		# 만약에 여기서 await지우면 session이 닫혔다고 
		"""
		urls = [
			"https://www.naver.com?page=1",
			"https://www.naver.com?page=2",
			"https://www.naver.com?page=3",
			"https://www.naver.com?page=4",
			...
			"https://www.naver.com?page=10",

		]

		10개의 페이지에 10개의 fetcher함수를 동시에 실행시킨
		"""
		await asyncio.gather(*[fetcher(session,i) for i in urls])


if __name__ == '__main__':
	asyncio.run(main())
