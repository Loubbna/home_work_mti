from interfaces import Payable,StorafeInterface,UiInterface
class Subscription(Payable):
    def __init__(self, subscription_id, member, plan, start_date, end_date , storage:StorafeInterface,ui:UiInterface):
        self.subscription_id = subscription_id
        self.member = member
        self.plan = plan
        self.start_date = start_date
        self.end_date = end_date
        self.storage=storage
        self.ui=ui
    def process_pay(self, amount):
        print(f"Processing payment of {amount} for subscription {self.subscription_id}")
    def save_subscription(self):
        data={
            "subscription_id": self.subscription_id,
            "member": self.member,
            "plan": self.plan,
            "start_date": self.start_date,
            "end_date": self.end_date

        }
        self.storage.save(data)
    def display_subscription_details(self):
        details = (f"Subscription ID: {self.subscription_id}\n"
                   f"Member: {self.member}\n"
                   f"Plan: {self.plan}\n"
                   f"Start Date: {self.start_date}\n"
                   f"End Date: {self.end_date}")
        self.ui.display(details)
# implement the class donation that inherits from Subscription
class donation(Subscription):
    def __init__(self, subscription_id, member, plan, start_date, end_date,
                  amount, frequency):
        super().__init__(subscription_id, member, plan, start_date, end_date)
        self.amount = amount
        self.frequency = frequency

    def process_pay(self, amount):
        print(f"Processing donation of {amount} for subscription {self.subscription_id} with frequency {self.frequency}")
class monthlySubscription(Subscription):
    def __init__(self, subscription_id, member, plan, start_date, end_date,
                 monthly_fee):
        super().__init__(subscription_id, member, plan, start_date, end_date)
    
        self.monthly_fee = monthly_fee
    def process_pay(self, amount):
        print(f"Processing monthly payment of {amount} for subscription {self.subscription_id}")
    # implement the class annualSubscription that inherits from Subscription
class annualSubscription(Subscription):
    def __init__(self, subscription_id, member, plan, start_date, end_date,
                 annual_fee):
        super().__init__(subscription_id, member, plan, start_date, end_date)
        self.annual_fee = annual_fee
    def process_pay(self, amount):
        print(f"Processing annual payment of {amount} for subscription {self.subscription_id}")