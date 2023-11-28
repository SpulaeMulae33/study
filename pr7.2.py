import random 
print("Enter list size: ")
s = int(input())
a = []
while len(a) < s:
    a.append(random.randint(1,30))
M = max(a)
m = min(a)
for index, value in enumerate(a):
    if value > M and value < m:
        a[value] = 0

print("U'r list: \n", a)