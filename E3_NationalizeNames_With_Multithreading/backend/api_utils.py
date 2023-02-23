import concurrent.futures
import os.path
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests

futures_list = []


def get_nationalize_data(request_names: list[str]):
    responses = []
    for request_name in request_names:
        response = requests.get("https://api.nationalize.io/", params={'name': request_name})
        if response.status_code == 200:
            responses.append(response.json())
        else:
            raise ValueError
    return responses


def get_nationalize_data_multithread(request_names: list[str]):
    results_list = []
    with ThreadPoolExecutor(10) as executor:
        for request_name in request_names:
            future_name = executor.submit(requests.get, "https://api.nationalize.io/", params={'name': request_name})
            futures_list.append(future_name)
        for done_future in as_completed(futures_list):
            if done_future.result().status_code == 200:
                results_list.append(done_future.result().json())
            else:
                raise ValueError
    return results_list


def get_nationalize_data_from_file(file_path: str):
    responses = []
    with open(file_path, 'r') as f:
        while True:
            request_name = f.readline()
            if not request_name:
                break
            response = requests.get("https://api.nationalize.io/", params={'name': request_name.strip('\n')})
            if response.status_code == 200:
                responses.append(response.json())
            else:
                raise ValueError
    with open(os.path.basename(file_path)+'_returned.txt', 'w') as f:
        for result in responses:
            f.write(f"Name: {result['name']}, Country: {result['country'][0]['country_id']}\n")
    return responses


def get_nationalize_data_multithread_from_file(file_path: str):
    results_list = []
    with open(file_path, 'r') as f:
        with ThreadPoolExecutor(10) as executor:
            while True:
                request_name = f.readline()
                if not request_name:
                    break
            request_name = f.readline()
            future_name = executor.submit(requests.get, "https://api.nationalize.io/",
                                          params={'name': request_name})
            futures_list.append(future_name)
            with open(os.path.basename(file_path) + '_returned_multithread.txt', 'w') as fw:
                for done_future in concurrent.futures.as_completed(futures_list):
                    if done_future.result().status_code == 200:
                        results_list.append(done_future.result().json())
                        executor.submit(fw.write, f"Name: "
                                                  f"{done_future.result().json()['name']},"
                                                  f" Country: "
                                                  f"{done_future.result().json()['country'][0]['country_id']}\n")
                    else:
                        raise ValueError(f"Status Code: {done_future.result().status_code}")
    return results_list


def get_countryrest_data(country_code: str):
    response = requests.get(f"https://restcountries.com/v3.1/alpha/{country_code}")
    if response.status_code == 200:
        return response.json()
