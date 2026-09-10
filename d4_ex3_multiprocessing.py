from multiprocessing import Process, current_process
import requests


URLS = [
    f"https://jsonplaceholder.typicode.com/albums/{num}"
    for num in range(1, 11)
]


def load_url(url):
    #import random
    #if random.choice([True, False]):
    #    raise Exception("Great choice!")
    response = requests.get(url)

    data = response.json()
    print(data)

    return data

# foarte mare atenție!!!
# dacă scrieți cod la nivel main
# acesta va fi rulat în mod repetat de fiecare proces

# v.1: așa e cu handling manual
def main():
    processes = []

    for url in URLS:
        p = Process(target=load_url, args=(url,) )
        processes.append(p)

    for p in processes:
        p.start()

    for p in processes:
        p.join()

print(__name__, current_process())

#if __name__ == "__main__":
#    main()


# v.2:
import concurrent.futures

def main():
    # ce este mai jos este copy-paste de la versiunea cu Threading
    # API-ul este exact același.
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        future_to_url = {
            executor.submit(load_url, url): url
            for url in URLS
        }

        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                # implementarea este superbă,
                # se ocupă ProcessPoolExecutor de inter-process communication
                # între parent process și cele spawn-ate de aici.
                data = future.result()
            except Exception as exc:
                print('%r generated an exception: %s' % (url, exc))
            else:
                print("%r result was: %s" % (url, data))

if __name__ == "__main__":
    main()