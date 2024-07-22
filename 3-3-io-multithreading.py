import asyncio
import time
import threading
import os 

import aiohttp

async def fetcher(session:aiohttp.ClientSession, url:str):	
	print(f"{os.getpid()} process | {threading.get_ident()} url: {url}")	
	async with session.get(url)  as resp:
		return await resp.text()

async def main():
	urls = ["https://www.naver.com", "https://www.google.com"] * 50

	async with aiohttp.ClientSession() as session:
		res = await asyncio.gather(*[fetcher(session, url) for url in urls])
	

if __name__ == '__main__':
	start = time.time()
	asyncio.run(main())
	end = time.time()
	print(end-start, "소요시간")