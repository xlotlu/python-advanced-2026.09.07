# Exercițiu:
# dat fiind dataset-ul temp_sensor_data.csv
# scrieți o funcție ce primind calea către fișier
# returnează o listă cu prima valoare a temperaturii
# pentru fiecare oră

from decimal import Decimal
from datetime import time


def get_first_hourly_temp(csvfile):
    # pattern de acumulare:
    # inițializăm obiectul în care acumulăm
    temps = []

    current_hour = None
    with open("data/temp_sensor_data.csv") as f: # "context manager"
        for line in f:
            tstamp, temp = line.removesuffix("\n").split(',')
            # ne facem data validation / type casting mai întâi
            #tstamp[:2]
            #tstamp.split(":")[0]
            #int(tstamp)
            #time.strptime(tstamp, "%H:%M:%S")
            tstamp = time.fromisoformat(tstamp)
            temp = Decimal(temp)

            hour = tstamp.hour

            # acumulăm în obiect, condițional:
            if hour != current_hour:
                temps.append(temp)
                current_hour = hour

    return temps


# Exercițiu:
#
# Scrieți o funcție generator

def xrange():
    pass

# ce creează un generator infinit,
# ce yield-uiește numere crescător,
# începând de la 0.

# rezultatul:
# from time import sleep
# for v in xrange():
#    print(v)
#    sleep(1)
# va printa la nesfârșit: 0, 1, 2, .....

def xrange():
    x = 0
    while True:
        yield x
        x += 1

# modificați funcția de mai sus
# pentru a primi parametrul max=None.
# dacă max are o valoare, se oprește la
# acel număr.

def xrange(max=None):
    x = 0
    while True:
        yield x
        x += 1
        if x is not None and x >= max:
            break
# v.2.
def xrange(max=None):
    x = 0
    while max is None or x < max:
        yield x
        x += 1


# re-implementare "curată" func de mai sus
import csv

def get_first_hourly_temp(csvfile):
    temps = []

    current_hour = None
    with open("data/temp_sensor_data.csv") as f:
        reader = csv.reader(f)
        for tstamp, temp in reader:
            tstamp = time.fromisoformat(tstamp)
            temp = Decimal(temp)

            hour = tstamp.hour

            if hour != current_hour:
                temps.append(temp)
                current_hour = hour

    return temps

# utilizarea ei, spre exemplu:
for value in get_first_hourly_temp("data/temp_sensor_data.csv"):
    print(value)

# Exercițiu:
# transformați funcția de mai sus într-o funcție generator,
# astfel încât orice cod ce o folosea pentru a itera în rezultat
# va rămâne nemodificat.

def get_first_hourly_temp(csvfile):
    current_hour = None
    with open("data/temp_sensor_data.csv") as f:
        reader = csv.reader(f)
        for tstamp, temp in reader:
            tstamp = time.fromisoformat(tstamp)
            temp = Decimal(temp)

            hour = tstamp.hour

            if hour != current_hour:
                yield temp
                current_hour = hour

for value in get_first_hourly_temp("data/temp_sensor_data.csv"):
    print(value)


# Abordare utilă: ne spargem funcția în bucăți mici, specializate:

# Anume:
# 1. o funcție de procesare
def process_temps_file(csvfile):
    current_hour = None
    with open(csvfile) as f:
        reader = csv.reader(f)
        for tstamp, temp in reader:
            tstamp = time.fromisoformat(tstamp)
            temp = Decimal(temp)

            yield tstamp, temp
            # simulate network latency:
            # sleep(.05)

# 2. o funcție izolată pentru hourly value
def get_first_hourly_temp(iterable):
    current_hour = None

    for tstamp, temp in iterable:
        hour = tstamp.hour

        if hour != current_hour:
            yield temp
            current_hour = hour


# Cerință: dat fiind fișierul "temp_sensor_data.csv",
# scrieți o funcție ce primind calea ca parametru
# returnează un iterabil conținând tuple de forma
# (timestamp, medie),
# unde timestamp poate să fie o oră,
# sau un minut.

RESOLUTION_HOUR = 0
RESOLUTION_MINUTE = 1
def get_average_temps(csvfile, resolution=RESOLUTION_HOUR):
    resolution_args = {'second': 0}
    if resolution == RESOLUTION_HOUR:
        resolution_args['minute'] = 0

    total = 0
    count = 0
    current_interval = None

    # un if: dacă e hour indicele 0, altfel indicele 1

    for tstamp, value in process_temps_file(csvfile):
        # agregăm sumă și count
        interval = tstamp.replace(**resolution_args)

        if current_interval is not None and interval != current_interval:
            # it's a new hour
            yield current_interval, total / count

            # reset
            total = 0
            count = 0

        total += value
        count += 1

        current_interval = interval

    # finally, don't forget the final (current) average:
    yield current_interval, total / count
