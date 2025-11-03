from expense import Expense
class Budget:
    """Budget class"""
    
    def __init__(self, total_amount, spent_amount=0):
        self.total_amount = total_amount
        self.spent_amount = spent_amount
        self.expenses = []
    
    
    def get_remaining_budget(self):
        """Returns the remaining budget"""
        return self.total_amount - self.spent_amount
class add_expense(Budget):
    def add_expense(self, description, category, amount):
        expense = Expense(
            expense_id=len(self.expenses) + 1,
            description=description,
            amount=amount,
            category=category
        )
        self.expenses.append(expense)
        self.spent_amount += amount
        return expense