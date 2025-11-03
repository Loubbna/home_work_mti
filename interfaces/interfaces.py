from ABC import ABC, abstractmethod
class Payable(ABC):
    @abstractmethod
    def process_pay(self,amount):
        pass

class Registable(ABC):
    @abstractmethod
    def schedue(self,member):
        pass
class Organizable(ABC):
    @abstractmethod
    def organize_event(self,event):
        pass
class StoageInteface(ABC):
    @abstractmethod
    def save(self,data):
        pass
    @abstractmethod
    def load(self,identifier):
        pass
class UiInterface(ABC):
    @abstractmethod
    def display(self,content):
        pass