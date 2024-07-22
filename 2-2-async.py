import time
import asyncio

async def deliver(customer:str, mealtime:int):
	print(f"{customer}에게 배달완료")
	await asyncio.sleep(mealtime)
	print(f"{customer}가-{mealtime}시간 동안 식사")
	print(f"{customer}그릇수거 완료")
	# return 0 (명시적이지 않은  return도 탈출점이 된)


async def main():
	task1 = asyncio.create_task(deliver("A",2))
	task2 = asyncio.create_task(deliver("B",10))
	task3 = asyncio.create_task(deliver("C",5))

if __name__ == "__main__":
	start = time.time()
	asyncio.run(main())
	end = time.time()
	print(f"배달 완료 시간 - {end-start}")	