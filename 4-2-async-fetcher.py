# 코루틴사용한 aiohttp

import aiohttp
import time
import asyncio

async def fetcher(session:aiohttp.ClientSession, url:str):	
	async with session.get(url)  as resp:
		# return resp.text[:10] aiohttp로 응답한 결과는 awaitable 객체이므로
		return await resp.text()

async def main():
	urls = ["https://www.naver.com", "https://www.google.com"] * 10

	async with aiohttp.ClientSession() as session:
		res = [await fetcher(session, url) for url in urls]
		# 동시성
		#res = await asyncio.gather(*[fetcher(session, url) for url in urls])
	print(res)
	

if __name__ == '__main__':
	start = time.time()
	asyncio.run(main())
	end = time.time()
	print(end-start, "소요시간")