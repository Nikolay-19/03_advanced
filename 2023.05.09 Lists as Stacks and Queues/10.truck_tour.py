from collections import deque

# pumps = deque([[int(x) for x in input().split()] for _ in range(int(input()))])
# print(pumps)

pumps = int(input())
tank = 0
fuel_list = []
distance_list = []
idx = 0

for _ in range(pumps):
    command = input().split()
    fuel_list.append(int(command[0]))
    distance_list.append(int(command[1]))

pumps_data = deque(zip(fuel_list, distance_list))
data_copy = pumps_data.copy()

while data_copy:
    petrol, distance = data_copy.popleft()
    tank += petrol
    if tank >= distance:
        tank -= distance
    else:
        pumps_data.rotate(-1)
        data_copy = pumps_data.copy()
        idx += 1
        tank = 0

print(idx)
