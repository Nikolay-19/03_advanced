users_qt = int(input())
users = set()

for _ in range(users_qt):
    user = input()
    users.add(user)

for user in users:
    print(user)
