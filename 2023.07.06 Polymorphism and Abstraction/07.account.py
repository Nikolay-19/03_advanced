class Account:
    def __init__(self, owner, amount=0):
        self.owner = owner
        self.amount = amount
        self.start = amount
        self._transactions = []

    def handle_transaction(self, transaction_amount):
        if transaction_amount < 0 and self.amount + transaction_amount < 0:
            raise ValueError("sorry cannot go in debt!")

        self.amount += transaction_amount
        self._transactions.append(transaction_amount)
        return f"New balance: {self.amount}"

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError("please use int for amount")

        self.handle_transaction(amount)

    @property
    def balance(self):
        return self.amount

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.start}"

    def __repr__(self):
        return f"Account({self.owner}, {self.amount})"

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, item):
        return self._transactions[item]

    def __iter__(self):
        for el in self._transactions:
            yield el

    def __reversed__(self):
        return reversed(self._transactions)

    def __lt__(self, other):
        if self.amount < other.amount:
            return True
        return False

    def __le__(self, other):
        if self.amount <= other.amount:
            return True
        return False

    def __eq__(self, other):
        if self.amount == other.amount:
            return True
        return False

    def __add__(self, other):
        a = Account(owner=f"{self.owner}&{other.owner}", amount=self.start + other.start)
        a._transactions = self._transactions + other._transactions
        return a
