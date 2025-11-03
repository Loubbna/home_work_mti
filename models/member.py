from EventRegistration import EventRegistration
from datetime import datetime
from interfaces import Registrable,StorageInterface,UiInterface

class EventRegistrationService:
    """Handles event registration for members"""
    
    def __init__(self):
        self.registrations = []
    
    def register_member_for_event(self, member, event):
        registration = EventRegistration(
            registration_id=len(self.registrations) + 1,
            member=member,
            event=event,
            registration_date=datetime.now()
        )
        self.registrations.append(registration)
        event.receives_registration(registration)
        return registration
    def registable(self,):
        """Register the member for an event"""
        print(f"Registering member for event")
    def save_registration(self, storage:StorageInterface):
        data = [{"registration_id": reg.registration_id,
                 "member": reg.member,
                 "event": reg.event,
                 "registration_date": reg.registration_date} for reg in self.registrations]
        storage.save(data)
    def display_registrations(self, ui:UiInterface):
        for reg in self.registrations:
            ui.display(f"Registration ID: {reg.registration_id}, Member: {reg.member}, Event: {reg.event}, Date: {reg.registration_date}")
    
