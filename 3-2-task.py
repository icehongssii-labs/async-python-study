import asyncio
import time

async def deliver(customer:str, mealtime:int):
	print(f"{customer}에게 배달완료")
	await asyncio.sleep(mealtime)
	print(f"{customer}가-{mealtime}시간 동안 식사")
	print(f"{customer}그릇수거 완료")
	return f"{customer}와{mealtime}"


async def main():
	res = await asyncio.gather(
		deliver("A",1),
		deliver("B",3),
		deliver("C",10)
		)
	print(res)


if __name__ == '__main__':
	start = time.time()
	asyncio.run(main())
	end = time.time()
	print(f"배달 완료 시간 - {end-start}")