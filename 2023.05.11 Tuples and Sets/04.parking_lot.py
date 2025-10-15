cars_qt = int(input())
parking = set()

for _ in range(cars_qt):
    command = input().split(", ")
    direction = command[0]
    license_plate = command[1]

    if direction == "IN":
        parking.add(license_plate)
    elif direction == "OUT" and license_plate in parking:
        parking.remove(license_plate)

if parking:
    for car in parking:
        print(car)
else:
    print("Parking Lot is Empty")
