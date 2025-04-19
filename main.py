import os
import time
import redis

redis_host = os.getenv("REDIS_HOST")
redis_port = os.getenv("REDIS_PORT")

# Connect to Redis
r = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

print("👋 Connected to Redis")

# Set a value
r.set("mykey", "hello", ex=10)
print("Set 'mykey' = 'hello' with 10s TTL")

# Read it back
val = r.get("mykey")
print(f"Got 'mykey': {val}")

# Push and pop from a queue
r.lpush("myqueue", "task1")
r.lpush("myqueue", "task2")
print("Pushed 2 tasks to 'myqueue'")

# Pop tasks
while True:
    task = r.rpop("myqueue")
    if not task:
        break
    print(f"Processing: {task}")
