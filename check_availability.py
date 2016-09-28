#!/usr/bin/env python
import os
import sys
import signal
import time
import requests

region_url = "https://reserve.cdn-apple.com/NL/nl_NL/reserve/iPhone/"
stores_url = region_url + "stores.json"
availability_url = region_url + "availability.json"


models = {
    "MN4V2": "iPhone 7 Plus Jet Black - 128 GB",
    "MN512": "iPhone 7 Plus Jet Black - 256 GB",
    "MNQM2": "iPhone 7 Plus Black - 32 GB",
    "MN4M2": "iPhone 7 Plus Black - 128 GB",
    "MN4W2": "iPhone 7 Plus Black - 256 GB",
    "MNQQ2": "iPhone 7 Plus Rose Gold - 32 GB",
    "MN4U2": "iPhone 7 Plus Rose Gold- 128 GB",
    "MN4Y2": "iPhone 7 Plus Rose Gold - 256 GB",
    "MNQP2": "iPhone 7 Plus Gold - 32 GB",
    "MN4Q2": "iPhone 7 Plus Gold - 128 GB",
    "MN502": "iPhone 7 Plus Gold - 256 GB",
    "MNQN2": "iPhone 7 Plus Silver - 32 GB",
    "MN4P2": "iPhone 7 Plus Silver - 128 GB",
    "MN4X2": "iPhone 7 Plus Silver - 256 GB",
}


def check_availability():
    stores_data = requests.get(stores_url).json()
    availability_data = requests.get(availability_url).json()

    if 'stores' in stores_data:
        for store in stores_data["stores"]:
            store_models = availability_data.get(store.get("storeNumber"))
            for model in store_models:
                if store_models.get(model) == "NONE":
                    continue

                # match if the first five characters match the list of models
                # we are interested in
                model_name = models.get(model[0:5])
                if model_name:
                    print("store:" + store.get("storeName")),
                    print("model:" + model_name + " is Available now")
                    alert(20)
        print("."),


def alert(n):
    beep = lambda x: os.system("echo -n '\a';sleep 0.2;" * x)
    beep(n)


def stop(signal, frame):
    print('Stop')
    sys.exit(0)


signal.signal(signal.SIGINT, stop)
print('Start')

while True:
    check_availability()
    time.sleep(30)
    sys.stdout.flush()


