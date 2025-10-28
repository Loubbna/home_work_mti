import csv
from datetime import datetime
from user import User
from budget import Budget
from member import Member
from Executive import Executive



class Member:
    def __init__(self, member_id, name, email, phone, status):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.phone = phone
        self.status = status
        self.subscriptions = []
        self.skills = []
        self.interests = []

    def __repr__(self):
        return f"Member({self.name}, {self.email}, {self.status})"


class Subscription:
    def __init__(self, sub_id, member_id, start_date, end_date, amount):
        self.sub_id = sub_id
        self.member_id = member_id
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d")
        self.end_date = datetime.strptime(end_date, "%Y-%m-%d")
        self.amount = float(amount)

    def __repr__(self):
        return f"Subscription({self.sub_id}, {self.amount}$)"


class Skill:
    def __init__(self, skill_id, member_id, skill_name):
        self.skill_id = skill_id
        self.member_id = member_id
        self.skill_name = skill_name

    def __repr__(self):
        return f"Skill({self.skill_name})"


class Interest:
    def __init__(self, interest_id, member_id, interest_name):
        self.interest_id = interest_id
        self.member_id = member_id
        self.interest_name = interest_name

    def __repr__(self):
        return f"Interest({self.interest_name})"


class Event:
    def __init__(self, event_id, title, date, location, max_participants):
        self.event_id = event_id
        self.title = title
        self.date = datetime.strptime(date, "%Y-%m-%d")
        self.location = location
        self.max_participants = int(max_participants)

    def __repr__(self):
        return f"Event({self.title}, {self.date.date()}, {self.location})"


class AssociationData:
    def __init__(self):
        self.members = []
        self.subscriptions = []
        self.skills = []
        self.interests = []
        self.events = []

    def load_csv(self, filename, class_type):
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if class_type == "member":
                    self.members.append(Member(**row))
                elif class_type == "subscription":
                    self.subscriptions.append(Subscription(**row))
                elif class_type == "skill":
                    self.skills.append(Skill(**row))
                elif class_type == "interest":
                    self.interests.append(Interest(**row))
                elif class_type == "event":
                    self.events.append(Event(**row))

    def link_data(self):
        for member in self.members:
            member.subscriptions = [s for s in self.subscriptions if s.member_id == member.member_id]
            member.skills = [s for s in self.skills if s.member_id == member.member_id]
            member.interests = [i for i in self.interests if i.member_id == member.member_id]

    def show_summary(self):
        print("\n=== MEMBERS DATA ===")
        for m in self.members:
            print(f"\n{m}")
            print(f"  Skills: {[s.skill_name for s in m.skills]}")
            print(f"  Interests: {[i.interest_name for i in m.interests]}")
            print(f"  Subscriptions: {[s.amount for s in m.subscriptions]}")

        print("\n=== EVENTS ===")
        for e in self.events:
            print(e)


# === Example Usage ===
if __name__ == "__main__":
    data = AssociationData()

    
    data.load_csv("association_data.csv", "member")
    data.load_csv("subscriptions.csv", "subscription")
    data.load_csv("skills.csv", "skill")
    data.load_csv("interests.csv", "interest")
    data.load_csv("events.csv", "event")

    data.link_data()


    data.show_summary()
