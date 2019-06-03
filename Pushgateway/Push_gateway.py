import time
import requests
from prometheus_client import CollectorRegistry, Gauge
from prometheus_client import push_to_gateway

HOURLY_RED_HAT = "https://api.weather.gov/gridpoints/RAH/73,57/forecast/hourly"


def get_temperature():
    result = requests.get(HOURLY_RED_HAT)
    return (result.json()["properties"]["periods"][0]["temperature"])


def prometheus_temperature(num):
    registry = CollectorRegistry()
    g = Gauge("red_hat_temp", "Temperature at Red Hat HQ", registry=registry)
    g.set(num)
    return registry



def push_temperature(url):
    while True:
        registry = prometheus_temperature(get_temperature())
        push_to_gateway(url, "temperature collector", registry)
        time.sleep(60 * 60)

if __name__ == '__main__':
    push_temperature('x.x.x.x:9091')
