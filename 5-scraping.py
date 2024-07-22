from bs4 import BeautifulSoup as bs
import aiohttp
import asyncio
import json
import time

BASE_URL = "https://openapi.naver.com/v1/search/image"
HEADERS = {"X-Naver-Client-Id":"wainckHB_4NkL7uzOr7g",
			"X-Naver-Client-Secret":"sTtzWAYAI5"}
 

async def fetcher(session, url, i):
	print(i+1)

	async with session.get(url, headers=HEADERS) as resp:
		res = await resp.json()
		print(res)

async def main():
	keyword = "cat"
	urls = [f"{BASE_URL}?query={keyword}&display=20&start={i}" for i in range(1,10)]
	async with aiohttp.ClientSession() as session: 
		await asyncio.gather(*[fetcher(session,url,i) for i,url in enumerate(urls)])


if __name__ == '__main__':
	asyncio.run(main())
