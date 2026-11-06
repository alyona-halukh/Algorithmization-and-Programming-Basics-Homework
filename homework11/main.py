import time

n = 500000
target = 499999

my_list = list(range(n))

my_set = set(my_list)

start = time.perf_counter()
result1 = target in my_list
end = time.perf_counter()

list_time = end - start

start = time.perf_counter()
result2 = target in my_set
end = time.perf_counter()

set_time = end - start

print("List search:", list_time, "сек")
print("Set search:", set_time, "сек")