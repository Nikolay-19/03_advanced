guests_qt = int(input())
guests = set()

for _ in range(guests_qt):
    guest = input()
    guests.add(guest)

while True:
    command = input()
    if command == "END":
        break
    guests.remove(command)

print(f"{len(guests)}")
for el in sorted(guests):
    print(el)
