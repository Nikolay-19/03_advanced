from abc import ABC, abstractmethod


class BaseLoan(ABC):
    def __init__(self, interest_rate, amount):
        self.interest_rate = float(interest_rate)
        self.amount = float(amount)

    @abstractmethod
    def increase_interest_rate(self):
        pass
