class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        for room in self.rooms:
            if room.number == room_number and room.capacity >= people and not room.is_taken:
                room.guests += people
                self.guests += people
                room.is_taken = True
                return
        else:
            f"Room number {room_number} cannot be taken"

    def free_room(self, room_number):
        for room in self.rooms:
            if room_number == room.number:
                if room.is_taken:
                    room.is_taken = False
                    self.guests -= room.guests
                    room.guests = 0
                    return
                return f"Room number {room.number} is not taken"

    def status(self):
        result = f"Hotel {self.name} has {self.guests} total guests\n" \
                 f"Free rooms: {', '.join(str(room.number) for room in self.rooms if not room.is_taken)}\n" \
                 f"Taken rooms: {', '.join(str(room.number) for room in self.rooms if room.is_taken)}"
        return result
