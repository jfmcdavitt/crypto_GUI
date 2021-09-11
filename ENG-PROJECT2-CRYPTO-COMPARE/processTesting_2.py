import concurrent.futures
import time
def increase():
    for i in range(15):
        print("Increasing:", i ** i, "\n")
        time.sleep(0.25)
    return "Joe"
def decrease():
    for i in range(100, 85, -1):
        print('Decreasing:', i - 20, "\n")
        time.sleep(0.26)
    print(a.result())

if __name__ == "__main__":
    with concurrent.futures.ProcessPoolExecutor() as pool:
        a = pool.submit(increase)
        b = pool.submit(decrease)
        pool.shutdown(wait=True)
        