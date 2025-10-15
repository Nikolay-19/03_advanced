class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, sub_id):
        result = []
        for sub in self.subscriptions:
            if sub.id == sub_id:
                result.append(sub.__repr__())

        for sub in self.customers:
            if sub.id == sub_id:
                result.append(sub.__repr__())

        for sub in self.trainers:
            if sub.id == sub_id:
                result.append(sub.__repr__())

        for sub in self.equipment:
            if sub.id == sub_id:
                result.append(sub.__repr__())

        for sub in self.plans:
            if sub.id == sub_id:
                result.append(sub.__repr__())

        return "\n".join(str(el) for el in result)
