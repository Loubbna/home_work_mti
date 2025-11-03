from user import User 
from Executive import Executive
from member import Member
from event import Event
from budget import Budget
from EventRegistration import EventRegistration
from expense import Expense
from datetime import datetime
from storage import JSONStorage
from ui import WebUi



if __name__ == "__main__":
    # Create an executive
    exec1 = Executive(
        user_id=1,
        email="amin@gmail.com",
        password="password123",
        last_name="amin",
        is_active=True,
        position="President",
        max_approval_amount=5000.00
    )
    
    # Create a member
    member1 = Member(
        user_id=2,
        email="line@gmail.com",
        password="pass456",
        last_name="lina",
        is_active=True,
        phone="555-0123",
        membership_status="Active",
        skills=["Python", "Project Management"]
    )
    
    # Executive creates an event
    event = exec1.create()
    event.title = "Annual Tech Conference"
    event.description = "Yearly technology conference"
    event.event_type = "Conference"
    event.location = "Main Hall"
    event.max_participants = 100
    event.publish_event()
    
    # Create budget for event
    budget = Budget(total_amount=10000.00)
    event.has_budget(budget)
    
    # Add expense to budget
    expense = budget.add_expense(
        description="Venue Rental",
        category="Venue",
        amount=3000.00
    )
    
    # Executive approves expense
    exec1.approve_expense(expense)
    
    # Member registers for event
    registration = member1.register_for_event(event)
    
    print(f"Event: {event.title}")
    print(f"Status: {event.status}")
    print(f"Registrations: {len(event.registrations)}")
    print(f"Budget remaining: ${budget.get_remaining_budget()}")
    print(f"Expense approved: {expense.approved}")
storage = JSONStorage()   
ui = WebUi()           

    # Inject them into Event
event = Event("Tech Conference", "Tech Center", storage, ui)
event.schedule(datetime(2025, 12, 10, 9, 0), "Main Hall")
event.register_member("line")
event.save_event()