import asyncio

async def say_hello():
	print("hello world")
	return 123	

if __name__ == '__main__':
	asyncio.run(say_hello())