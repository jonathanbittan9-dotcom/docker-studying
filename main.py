import time
import os

name = os.getenv("NAME", "world")
print(f"hello {name} from python, no docker yet")

for i in range(1, 4):
    print(f"count {i}")
    time.sleep(1)

print("done")
