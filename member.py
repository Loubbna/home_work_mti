from user import User
from EventRegistration import EventRegistration
from datetime import datetime
class Member(User):
    """Member class inheriting from User"""
    
    def __init__(self, user_id, email, password, last_name, is_active, 
                 phone, membership_status, skills):
        super().__init__(user_id, email, password, last_name, is_active)
        self.phone = phone
        self.membership_status = membership_status
        self.skills = skills
        self.event_registrations = []
    
    def register_for_event(self, event):
        """Register member for an event"""
        registration = EventRegistration(
            registration_id=len(self.event_registrations) + 1,
            member=self,
            event=event,
            registration_date=datetime.now()
        )
        self.event_registrations.append(registration)
        event.receives_registration(registration)
        return registration
    
    def update_profile(self):
        """Update member profile"""
        pass
