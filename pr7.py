import random

n = int(input('Input N: '))

rand_list = [random.randint(1,30) for i in range (n)]
print(f"You'r list: {rand_list}")

min_val = min(rand_list)
max_val = max(rand_list)
min_index = rand_list.index(max_val)
max_index = rand_list.index(min_val)
start_index = min(min_index, max_index) + 1
end_index = max(min_index, max_index)

rand_list[start_index:end_index] = [0] * (end_index - start_index)
print(f"Modified list: {rand_list}")