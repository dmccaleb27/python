#!/bin/python
import redis

r = redis.Redis()
r.mset({"Dylan": "McCaleb", "Emmet": "Waggle"})
print(r.get("Dylan"))