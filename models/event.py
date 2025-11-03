from interfaces import Organizable
from interfaces import StoageInteface , abstractmethod
from Ui import UIInterface
from event import Event
from datetime import datetime
from interfaces import Organizable
class Event:
    """Event class"""
    
    def __init__(self, event_id, title, event_type, 
                 date_time, location, max_participants, status, creator,storaege:StoageInteface,ui:UIInterface):
        self.event_id = event_id
        self.title = title
        self.event_type = event_type
        self.date_time = date_time
        self.location = location
        self.max_participants = max_participants
        self.status = status
        self.creator = creator
        self.registrations = []
        self.budget = None
        self.storage=storaege
        self.ui=ui
    
    def describe(self):
        return f"Event {self.title}, Type: {self.event_type}, Date: {self.date_time}, Location: {self.location}, Status: {self.status}"
    def display_event_deatails(self):
        return f"Event ID: {self.event_id}\nTitle: {self.title}\nType: {self.event_type}\nDate & Time: {self.date_time}\nLocation: {self.location}\nMax Participants: {self.max_participants}\nStatus: {self.status}\nCreator: {self.creator.last_name}"
    def organize(self):
        """Organize the event"""
        print(f"Organizing event: {self.title} by {self.creator}")
    def schedule(self, date_time, location):
        self.ui.display(f"Scheduling '{self.title}' at {location} on {date_time}")

    def register_member(self, member):
        self.members.append(member)
        self.ui.display(f"Member {member} registered for {self.title}")

    def save_event(self):
        data = {"title": self.title, "location": self.location, "members": self.members}
        self.storage.save(data)
#class trip
class trip(Event):
    def __init__(self, event_id, title, event_type, 
                 date_time, location, max_participants, status, creator,
                 destination, duration_days):
        super().__init__(event_id, title, event_type, 
                         date_time, location, max_participants, status, creator)
        self.destination = destination
        self.duration_days = duration_days

    def describe(self):
        event_description = super().describe()
        return f"{event_description}, Destination: {self.destination}, Duration: {self.duration_days} days"
    def organize(self):
        print(f"Organizing trip to {self.destination} for {self.duration_days} days.")
        #class meeting

class meeting(Event):
    def __init__(self,meeting_id,title,event_type,
                 date_time,location,max_participants,status,creator,
                 minutes):
        super().__init__(meeting_id,title,event_type,
                         date_time,location,max_participants,status,creator)
        self.minutes = minutes
    def desribe(self):
        event_description = super().describe()
        return f"{event_description}, Minutes: {self.minutes}"
    def organize(self):
        print(f"Organizing meeting: {self.title}.")
        #class compitition
class compitition(Event):
    def __init__(self,competition_id,title,event_type,
                 date_time,location,max_participants,status,creator,
                 prize):
        super().__init__(competition_id,title,event_type,
                         date_time,location,max_participants,status,creator)
        self.prize = prize
    def describe(self):
        return super().describe() + f", Prize: {self.prize}"
    def organize(self):
        print(f"Organizing competition: {self.title} with prize {self.prize}.")
#test the clases
if __name__ == "__main__":
    base_event = Event(
        event_id=1,
        title="Tech Workshop",
        event_type="Workshop",
        date_time=datetime(2025, 11, 10, 10, 0),
        location="Tech Hub",
        max_participants=50,
        status="Scheduled",
        creator="Admin"
    )
    print(base_event.describe())
trip_event = trip(
        event_id=2,
        title="Mountain Adventure",
        event_type="Trip",
        date_time=datetime(2025, 12, 5, 8, 0),
        location="National Park",
        max_participants=20,
        status="Planned",
        creator="amin",
        destination="chrea mountains",
        duration_days=3
    )

meeting_event = meeting(
        meeting_id=3,
        title="Team Meeting",
        event_type="Meeting",
        date_time=datetime(2025, 11, 15, 14, 0),
        location="Office Room 4",
        max_participants=10,
        status="Scheduled",
        creator="Manager",
        minutes="Discussed project deadlines"
    )

comp_event = compitition(
        competition_id=4,
        title="Coding Challenge",
        event_type="Competition",
        date_time=datetime(2025, 12, 20, 9, 0),
        location="University of bouira",
        max_participants=100,
        status="Upcoming",
        creator="Tech Club",
        prize="$1000"
    )

    
print("=== testing describe() ===")
print(base_event.describe())
("test describe for the class trip")
print(trip_event.describe())
("test describe for te class meeting")
print(meeting_event.describe())
("test describe for the class compitition")
print(comp_event.describe())

print ("test the methode organize()")
base_event.organize()
trip_event.organize()
meeting_event.organize()
comp_event.organize()