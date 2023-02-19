# E6 - Not Blocking UI When Running Stuff Exercise
from concurrent.futures import ThreadPoolExecutor
import requests
import time


def my_countdown(sec_amount: float):
    while sec_amount >= 0:
        print(f"{round(sec_amount, 1)} seconds left")
        sec_amount -= 0.1
        time.sleep(0.1)


def my_kanye_doesnt_wait(kanye_future):
    try:
        print(kanye_future.result().json()['quote'])
    except Exception as e:
        print("Error in future", e)


def my_kanye_countdown(sec_amount: float):
    with ThreadPoolExecutor(10) as executor:
        while sec_amount >= 0:
            print(f"{round(sec_amount, 1)} seconds left")
            if round(sec_amount, 1).is_integer():
                future = executor.submit(requests.get, "https://api.kanye.rest/")
                future.add_done_callback(my_kanye_doesnt_wait)
            sec_amount -= 0.1
            time.sleep(0.1)


if __name__ == "__main__":
    # my_countdown(5.0)
    my_kanye_countdown(5.0)
