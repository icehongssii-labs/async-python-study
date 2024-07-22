import time
def delivery(home:str, mealtime:int):
    print(f"{home}에 진입")
    time.sleep(mealtime)
    print(f"{mealtime}동안 식사")
    print(f"{home}그릇 수거")

if __name__ == "__main__":
    start = time.time()
    delivery("a", 1)
    delivery("b", 2)
    delivery("c", 5)
    end = time.time()
    print(end-start, "--배달소요시간")