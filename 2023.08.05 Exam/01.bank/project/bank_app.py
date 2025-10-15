from project.clients.adult import Adult
from project.clients.student import Student
from project.loans.student_loan import StudentLoan
from project.loans.mortgage_loan import MortgageLoan


class BankApp:
    def __init__(self, capacity):
        self.capacity = capacity
        self.loans = []
        self.clients = []

    def add_loan(self, loan_type):
        if loan_type not in ["StudentLoan", "MortgageLoan"]:
            raise Exception("Invalid loan type!")

        if loan_type == "StudentLoan":
            loan = StudentLoan()
        elif loan_type == "MortgageLoan":
            loan = MortgageLoan()

        self.loans.append(loan)
        return f"{loan_type} was successfully added."

    def add_client(self, client_type, client_name, client_id, income):
        if client_type not in ["Adult", "Student"]:
            raise Exception("Invalid client type!")
        if len(self.clients) + 1 > self.capacity:
            return "Not enough bank capacity."

        if client_type == "Adult":
            client = Adult(client_name, client_id, float(income))
        elif client_type == "Student":
            client = Student(client_name, client_id, float(income))

        self.clients.append(client)
        return f"{client_type} was successfully added."

    def get_client_by_id(self, client_id):
        for client in self.clients:
            if client.client_id == client_id:
                return client
        return None

    def get_loan_by_type(self, loan_type):
        for loan in self.loans:
            if type(loan).__name__ == loan_type:
                return loan
        return None

    def grant_loan(self, loan_type, client_id):
        client = self.get_client_by_id(client_id)
        loan = self.get_loan_by_type(loan_type)

        if loan_type == "StudentLoan" and type(client).__name__ != "Student":
            raise Exception("Inappropriate loan type!")
        elif loan_type == "MortgageLoan" and type(client).__name__ != "Adult":
            raise Exception("Inappropriate loan type!")

        self.loans.remove(loan)
        client.loans.append(loan)
        return f"Successfully granted {loan_type} to {client.name} with ID {client.client_id}."

    def remove_client(self, client_id):
        client = self.get_client_by_id(client_id)
        if client is None:
            raise Exception("No such client!")
        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client.client_id}."

    def increase_loan_interest(self, loan_type):
        count = 0
        for loan in self.loans:
            if loan_type == type(loan).__name__:
                loan.increase_interest_rate()
                count += 1

        return f"Successfully changed {count} loans."

    def increase_clients_interest(self, min_rate):
        count = 0
        for client in self.clients:
            if client.interest < float(min_rate):
                client.increase_clients_interest()
                count += 1

        return f"Number of clients affected: {count}."

    def get_statistics(self):
        result = []
        income = 0
        granted = 0
        granted_qt = 0
        not_granted = 0
        not_granted_qt = 0
        total_interest = 0

        for client in self.clients:
            for loan in client.loans:
                granted += 1
                granted_qt += loan.amount
            income += client.income
            total_interest += client.interest

        for loan in self.loans:
            not_granted += 1
            not_granted_qt += loan.amount

        if len(self.clients) > 0:
            average_rate = total_interest / len(self.clients)
        else:
            average_rate = 0

        result.append(f"Active Clients: {len(self.clients)}")
        result.append(f"Total Income: {income:.2f}")
        result.append(f"Granted Loans: {granted}, Total Sum: {granted_qt:.2f}")
        result.append(f"Available Loans: {not_granted}, Total Sum: {not_granted_qt:.2f}")
        result.append(f"Average Client Interest Rate: {average_rate:.2f}")

        return "\n".join(el for el in result)


bank = BankApp(3)
print(bank.add_loan('StudentLoan'))
print(bank.add_loan('MortgageLoan'))
print(bank.add_loan('StudentLoan'))
print(bank.add_loan('MortgageLoan'))
print(bank.add_client('Student', 'Peter Simmons', '1234567891', 500))
print(bank.add_client('Adult', 'Samantha Peters', '1234567000', 1000))
print(bank.add_client('Student', 'Simon Mann', '1234567999', 700))
print(bank.add_client('Student', 'Tammy Smith', '1234567555', 700))
print(bank.grant_loan('StudentLoan', '1234567891'))
print(bank.grant_loan('MortgageLoan', '1234567000'))
print(bank.grant_loan('MortgageLoan', '1234567000'))
print(bank.remove_client('1234567999'))
print(bank.increase_loan_interest('StudentLoan'))
print(bank.increase_loan_interest('MortgageLoan'))
print(bank.increase_clients_interest(1.2))
print(bank.increase_clients_interest(3.5))
print(bank.get_statistics())
