import asyncio
import time

async def delivery(home:str, mealtime:int):
    print(f"{home}에 진입")
    await asyncio.sleep(mealtime)
    print(f"{mealtime}동안 식사")
    print(f"{home}그릇 수거")

async def main():
    await asyncio.gather(
        delivery("a",1),
        delivery("b",5),
        delivery("c",2),
    )

if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(end-start, "--배달소요시간")