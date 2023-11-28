import random 
print("Enter list size: ")
s = int(input())
a = []
while len(a) < s:
    a.append(random.randint(1,30))
M = max(a)
m = min(a)
b = list(map(lambda x: x if x > M or x < m else 0, a))

print("U'r list: \n", a, b)