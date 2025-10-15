class Guitar:
    @staticmethod
    def play():
        return "Playing the guitar"


class Children:
    @staticmethod
    def play():
        return "Children are playing"


def start_playing(self):
    return self.play()


guitar = Guitar()
children = Children()
print(start_playing(guitar))
print(start_playing(children))
