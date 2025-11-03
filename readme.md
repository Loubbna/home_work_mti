In this code we are applying SOLID principle to get a clean code 

1.Single responsabilty principle :
in the class member:
we create the class UpdateProfil so we sperate it from the class member 
in the class event :
we craete the classe register_for_event 
we create the classe managers : eventStatusManager and eventBudgetManager
in the class buget :
we craete the class add_expenses so we can seperate it from the budget class
*** Problem solved :
Before applying SRP, each class was doing too many things making the code hard to maintain and test.
by separating responsibilities, each class now focuses on one job, which simplifies debugging, improves readability, and makes updates easier.

2.open closed modification:
we craete meeting and trip and compitition which are subclasses from the class event , so here we can add classes without modify the class event applying OCP of solid .
also , we created a nes types of subscription donation , monthlySubscription and annuallysubscription  without modifying the super class .

** Problem solved :
Previously, adding new event or subscription types required modifying existing classes, which could break old code.now , with OCP principle each time we add a new type we can easily implement without modifying the class code 


3.Liskov Substitution Principle (LSP)
to aplly this principle , we created the methode display_info_event()
then we create the methode describe() and make sure that the subclasses are extending it correctly.

**Problem Solved :
now subclasses of the calass event can act like the high level class Event , so we call call them without breaking the code .

 def describe(self):
        event_description = super().describe()
        return f"{event_description}, Destination: {self.destination}, Duration: {self.duration_days} days"
**
4.Interface Segregation Principle (ISP) :

to apply this principle , we have to abstract the interfaces oragnizable , registable and payable.
1. payable: we  implemnt the methode process_pay() in the class subscription and its subclasses .
2. registrable: we implement the methode schedule () at the class member .
3. oragizable : we implement the methode organize_event() at the class event and its subclasses to get informations  about event oganization informations.

**problem solved :
Before applying ISP, some classes were forced to implement methods they didn’t need.
By splitting interfaces, each class now depends only on methods it actually uses, reducing unnecessary code and dependencies.

5. dependency inversion Principle (DIP):
we craete the abstract interface storage and Ui so we do not have to modify the superclass in each time we need to add a new type of storage like JsonStorage and CSVStorage , also for ui so each time we do not need to modify the class Ui to add a new user interface like WebUI or MobileUi.

**problem solved :
Without DIP, high level classes were directly dependent on low-level details, causing tight coupling.
By introducing abstractions, the system is now flexible . we can switch storage types or user interfaces without modifying logic.
