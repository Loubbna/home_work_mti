class EventRegistration:
    """EventRegistration class"""
    
    def __init__(self, registration_id, member, event, registration_date):
        self.registration_id = registration_id
        self.member = member
        self.event = event
        self.registration_date = registration_date
        self.status = "Pending"
    
    def cancel_registration(self):
        """Cancels the registration"""
        self.status = "Cancelled"
    
    def check_in(self):
        """Checks in the member for the event"""
        self.status = "Checked In"