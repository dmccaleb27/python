#!/bin/python
import redis

r = redis.Redis()
r.mset({"Croatia": "Zagreb", "Bahamas": "Nassau"})
True
r.get("Bahamas")
b'Nassau'