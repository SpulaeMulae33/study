N = int(input("Input N: "))
friends = []
fri = {}
temp = {}
for i in range(N):
    if i < N:
        key = input()
        value = input()
        temp[key] = value
        friends.append(temp)
    
print(friends)
