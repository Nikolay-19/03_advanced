class Account:
    def __init__(self, id, balance, pin):
        self.id = id
        self.balance = balance
        self.pin = pin

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def pin(self):
        return self.__pin

    @pin.setter
    def pin(self, value):
        self.__pin = value

    def get_id(self, pin):
        if pin == self.pin:
            return self.id
        return "Wrong pin"

    def change_pin(self, old, new):
        if old == self.pin:
            self.pin = new
            return "Pin changed"
        return "Wrong pin"
