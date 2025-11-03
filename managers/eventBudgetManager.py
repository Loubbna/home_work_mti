class EventBudgetManager:
    """Handles event budget operations."""

    def assign_budget(self, event, budget):
        event.budget = budget
        print(f"Budget of {budget} assigned to event: {event.name}")