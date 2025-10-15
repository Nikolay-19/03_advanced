from abc import ABC, abstractmethod


class Device(ABC):
    @abstractmethod
    def connect(self, device2, cable):
        pass


class Outlet(Device):
    def connect(self, device2, cable):
        return f"Connecting {self.__class__.__name__} with {device2.__class__.__name__} via {cable.__class__.__name__}"


class TV(Device):
    def connect(self, device2, cable):
        return f"Connecting {self.__class__.__name__} with {device2.__class__.__name__} via {cable.__class__.__name__}"


class Console(Device):
    def connect(self, device2, cable):
        return f"Connecting {self.__class__.__name__} with {device2.__class__.__name__} via {cable.__class__.__name__}"


class DVD(Device):
    def connect(self, device2, cable):
        return f"Connecting {self.__class__.__name__} with {device2.__class__.__name__} via {cable.__class__.__name__}"


class Router(Device):
    def connect(self, device2, cable):
        return f"Connecting {self.__class__.__name__} with {device2.__class__.__name__} via {cable.__class__.__name__}"


class Cable:
    @staticmethod
    @abstractmethod
    def connect(device1, device2):
        pass


class HDMI(Cable):
    def connect(self, device1, device2):
        if device1 != device2 and device1 in [TV, Console, Outlet] and device2 in [TV, Console, Outlet]:
            device1.connect(device2, self)


class Power(Cable):
    def connect(self, device1, device2):
        if device1 != device2 and device1 in [Outlet] and device2 in [TV, Console, Outlet]:
            device1.connect(device2, self)


class RCA(Cable):
    def connect(self, device1, device2):
        if device1 != device2 and device1 in [TV, DVD, Outlet] and device2 in [TV, DVD, Outlet]:
            device1.connect(device2, self)


class Ethernet(Cable):
    def connect(self, device1, device2):
        if device1 != device2 and device1 in [Router, TV, Console, Outlet] and device2 in [Router, TV, Console, Outlet]:
            device1.connect(device2, self)
