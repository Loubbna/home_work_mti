class Event:
    """Event class"""
    
    def __init__(self, event_id, title, description, event_type, 
                 date_time, location, max_participants, status, creator):
        self.event_id = event_id
        self.title = title
        self.description = description
        self.event_type = event_type
        self.date_time = date_time
        self.location = location
        self.max_participants = max_participants
        self.status = status
        self.creator = creator
        self.registrations = []
        self.budget = None
    
    def publish_event(self):
        """Publishes the event"""
        self.status = "Published"
    
    def check_capacity(self):
        """Returns remaining capacity"""
        return self.max_participants - len(self.registrations)
    
    def cancel_event(self):
        """Cancels the event"""
        self.status = "Cancelled"
    
    def receives_registration(self, registration):
        """Receives a new registration"""
        if self.check_capacity() > 0:
            self.registrations.append(registration)
    
    def has_budget(self, budget):
        """Associates a budget with the event"""
        self.budget = budget