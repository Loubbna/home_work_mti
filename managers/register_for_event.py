from user import User
from EventRegistration import EventRegistration
from datetime import datetime

class Register_for_event:
    """Register member for an event"""

    def __init__(self):
        # Initialize event_registrations as an empty list
        self.event_registrations = []

    def register(self, event):
        registration = EventRegistration(
            registration_id=len(self.event_registrations) + 1,
            member=self,
            event=event,
            registration_date=datetime.now()
        )
        self.event_registrations.append(registration)
        event.receives_registration(registration)
        return registration