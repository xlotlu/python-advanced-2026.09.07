from threading import (
    Thread,
    Event,
    Lock,
)


"""
Decision tree guideline for concurrent execution:

(concurrent = not necessarily parallel)

procese separate = paralelism adevărat
                   (if enough cpu cores anyway)
                   (kernel-ul face scheduling-ul)
thread-uri separate multi-cpu = paralelism adevărat
                                (aceeași notă ca mai sus)
thread-uri separate single-cpu = time-sharing
async = time-sharing


time-sharing: perfect pentru task-uri I/O-bound
parallelism: pentru task-uri CPU-bound



v.1. python classic
paralelism: posibil doar cu multiprocessing
time-sharing: asta face threading

v.2. python "free-threading"
paralelism: posibil cu multiprocessing
            ȘI cu threading


"""

# 1. the simplest form

from time import sleep
from random import randint

def myfunc(arg):
    sleep(1 / randint(2, 10))
    print("»", arg, "is done")

threads = []
for x in range(5):
    threads.append(
        Thread(target=myfunc, args=(x,))
    )

for t in threads:
    t.start()

# la final, facem asta, ca să nu iasă
# din execuție main-thread-ul
for t in threads:
    t.join() # this is blocking

# concepte:
# 1. process
# 2. thread. it runs /inside/ a process.
#    can run on a different CPU,
#    but!!! it has access to the same
#    memory as the parent process.
#
# implicație: thread-urile au memorie comună
# implicație 2: superb d.p.d.v. development
#               .... mai puțin când 2 thread-uri
#               scriu deodată în același loc.
#               == memory corruption


# 2. signalling pentru a putea opri
#    un thread cu while True, din părinte:

stop = Event()

def worker():
    while not stop.is_set():
        print("Working...")
        sleep(1)

    print("Worker stopping")

thread = Thread(target=worker)
thread.start()

sleep(5) # some time later...

stop.set()
thread.join()


# 3. problemă: cum capturăm rezultatul?

# 3.1. chinuitor, rescriem cod, funcția în sine
#      își stochează rezultatul într-o variabilă top-level.
#      (care atenție: obiectul trebuie să fie thread-safe)
#      (lista este thread-safe)

results = []

# și evident, ne va trebui un mecanism
# să știm care thread a dat ce rezultat

def myfunc(t, arg):
    retval = randint(2, 10)
    sleep(retval)
    print("»", arg, "is done")

    results.append(
        (t, retval)
    )

    # nici nu mai are sens să returnăm
    #return retval

# 3.2. varianta elegantă, facem rewrite la Thread.run()
#      pentru a captura rezultatul

class RThread(Thread):
    """
    An implementation that captures the target's result
    in `self.result`.
    """
    def run(self):
        try:
            if self._target is not None:
                self.result = self._target(*self._args, **self._kwargs)
        finally:
            # Avoid a refcycle if the thread is running a function with
            # an argument that has a member that points to the thread.
            del self._target, self._args, self._kwargs

def myfunc(arg):
    s = randint(1, 10)

    sleep(s)
    return (arg, s)

threads = []
for x in range(5):
    threads.append(
        RThread(target=myfunc, args=(x,))
    )

for t in threads:
    t.start()

# haidem să procesăm incremental rezultatele
# după cum sunt gata:

while threads:
    for idx, thread in enumerate(threads):
        if not thread.is_alive():
            # we have a new thread that finished
            print("» thread", thread, "::", thread.result)

            # warning: be careful when mutating a list
            # while iterating through it
            del threads[idx]
            break

    # don't forget to not loop so tight!
    sleep(.00001)


x = 0
lock = Lock()

def myfunc():
    global x

    for _ in range(1000):
        lock.acquire()

        current = x * 1
        sleep( 1 / (100000 * randint(1000, 2000)))
        x = current + 1

        lock.release()

threads = [ Thread(target=myfunc) for _ in range(10) ]
for t in threads: t.start()
for t in threads: t.join()
print(x)

# sau echivalent, lock as context manager:

x = 0
lock = Lock()

def myfunc():
    global x

    for _ in range(1000):
        with lock:
            current = x * 1
            sleep( 1 / (100000 * randint(1000, 2000)))
            x = current + 1

threads = [ Thread(target=myfunc) for _ in range(10) ]
for t in threads: t.start()
for t in threads: t.join()
print(x)


# Task:
# date fiind aceste url-uri
URLS = [
    f"https://jsonplaceholder.typicode.com/albums/{num}"
    for num in range(1, 11)
]

# populați o listă cu fiecare din structurile de date
# disponibile în endpoint


import concurrent.futures
import requests

def load_url(url):
    import random
    if random.choice([True, False]):
        raise Exception("Great choice!")
    response = requests.get(url)
    return response.json()


# We can use a with statement to ensure threads are cleaned up promptly
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    # Start the load operations and mark each future with its URL
    future_to_url = {
        executor.submit(load_url, url): url
        for url in URLS
    }

    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        try:
            data = future.result()
        except Exception as exc:
            print('%r generated an exception: %s' % (url, exc))
        else:
            print("%r result was: %s" % (url, data))