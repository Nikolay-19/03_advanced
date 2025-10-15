from collections import deque

times = deque(int(el) for el in input().split())  # LIFO
tasks = deque(int(el) for el in input().split())  # FIFO

darth_vader = range(0, 61)
thor = range(61, 121)
big_blue = range(121, 181)
small_yellow = range(181, 241)

smurf = 0
odinson = 0
chicken = 0
skywalker = 0

while times and tasks:
    t_minus = times.popleft()
    task = tasks.pop()
    time = t_minus * task

    if time > 240:
        task -= 2
        times.append(t_minus)
        tasks.append(task)
        continue

    else:
        if time in darth_vader:
            skywalker += 1
        elif time in thor:
            odinson += 1
        elif time in big_blue:
            smurf += 1
        elif time in small_yellow:
            chicken += 1

print(f"Congratulations, all tasks have been completed! Rubber ducks rewarded:\n"
      f"Darth Vader Ducky: {skywalker}\n"
      f"Thor Ducky: {odinson}\n"
      f"Big Blue Rubber Ducky: {smurf}\n"
      f"Small Yellow Rubber Ducky: {chicken}")
