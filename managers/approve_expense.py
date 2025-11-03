from ..models.expense import Expense
from ..models.budget import Budget
class approve_expense(Budget, Expense):

    def approve_expense(self, expense, budget):
        if budget.remaining_amount >= expense.amount:
            budget.remaining_amount -= expense.amount
            expense.status = "Approved"
            print(f"Expense of {expense.amount} approved. Remaining budget: {budget.remaining_amount}")
        else:
            expense.status = "Denied"
            print(f"Expense of {expense.amount} denied. Insufficient budget.")