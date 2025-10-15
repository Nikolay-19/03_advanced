from project.loans.base_loan import BaseLoan


class MortgageLoan(BaseLoan):
    INCREASE = 0.5

    def __init__(self):
        super().__init__(3.5, 50000.0)

    def increase_interest_rate(self):
        self.interest_rate += MortgageLoan.INCREASE
