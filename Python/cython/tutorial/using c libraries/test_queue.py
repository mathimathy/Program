import time

import queue

Q = queue.Queue()

Q.append(10)
Q.append(20)
print(Q.peek())
print(Q.pop())
print(Q.pop())
try:
    print(Q.pop())
except IndexError as e:
    print("Error message: ", e)

i = 10000

values = range(i)

start_time = time.time()

Q.extend(values)

end_time = time.time() - start_time

print(f"Adding {i} items took {1000*end_time:1.3f} msecs.")

for i in range(41):
    Q.pop()

Q.pop()
print("The answer is:")
print(Q.pop())