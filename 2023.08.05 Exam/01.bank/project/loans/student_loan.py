from project.loans.base_loan import BaseLoan


class StudentLoan(BaseLoan):
    INCREASE = 0.2

    def __init__(self):
        super().__init__(1.5, 2000.0)

    def increase_interest_rate(self):
        self.interest_rate += StudentLoan.INCREASE
