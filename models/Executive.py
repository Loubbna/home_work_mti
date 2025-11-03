from user import User
from event import Event
from datetime import datetime

class Executive(User):
    """Executive class inheriting from User"""
    
    def __init__(self, user_id, email, password, last_name, is_active, 
                 position, max_approval_amount):
        super().__init__(user_id, email, password, last_name, is_active)
        self.position = position
        self.max_approval_amount = max_approval_amount
        self.created_events = []
    
    def create(self):
        """Creates a new event"""
        event = Event(
            event_id=len(self.created_events) + 1,
            title="",
            description="",
            event_type="",
            date_time=datetime.now(),
            location="",
            max_participants=0,
            status="Draft",
            creator=self
        )
        self.created_events.append(event)
        return event
    
