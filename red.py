#!/bin/python
import redis
import datetime

r = redis.Redis()
today = datetime.date.today()
stoday = today.isoformat()
visitors = {"Dylan", "Emmet", "Jeff"}
r.mset(*visitors, stoday)
print(r.get("Dylan"))