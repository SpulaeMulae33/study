N = int(input("Input N: "))
friends = []
for i in range(N):
    name = input(f'Friend {i+1}:')
    age = int(input(f'Age of friend {i+1}:'))
    friend = {'name':name , 'age':age }
    friends.append(friend)
    
friends.sort(key= lambda x: x['name'])
for friend in friends:
    print(friend)