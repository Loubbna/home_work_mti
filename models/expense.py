class Expense:
    """Expense class"""
    
    def __init__(self, expense_id, description, amount, category):
        self.expense_id = expense_id
        self.description = description
        self.amount = amount
        self.category = category
        self.approved = False
        self.approver = None
    
    def approved_by(self, executive):
        """Records the executive who approved the expense"""
        self.approver = executive