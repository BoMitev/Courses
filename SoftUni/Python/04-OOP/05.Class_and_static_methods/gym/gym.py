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
            customer.__class__.id += 1

    def add_trainer(self, trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)
            trainer.__class__.id += 1

    def add_equipment(self, equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)
            equipment.__class__.id += 1

    def add_plan(self, plan):
        if plan not in self.plans:
            self.plans.append(plan)
            plan.__class__.id += 1

    def add_subscription(self, subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)
            subscription.__class__.id += 1

    def subscription_info(self, subscription_id):
        sub = [s for s in self.subscriptions if s.id == subscription_id][0]
        trainer_id = sub.trainer_id
        customer_id = sub.customer_id
        plan_id = None
        equipment_id = None
        info = []

        for plan in self.plans:
            if plan.trainer_id == trainer_id:
                plan_id = plan.id
                equipment_id = plan.equipment_id

        info.append(sub.__repr__())
        info.extend([c.__repr__() for c in self.customers if c.id == customer_id])
        info.extend([t.__repr__() for t in self.trainers if t.id == trainer_id])
        info.extend([e.__repr__() for e in self.equipment if e.id == equipment_id])
        info.extend([p.__repr__() for p in self.plans if p.id == plan_id])

        return '\n'.join(info)