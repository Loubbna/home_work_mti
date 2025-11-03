from interfaces import UIInterface

class WebUI(UIInterface):
    def display(self, message):
        print(f"[Web Interface] {message}")

class CLIUI(UIInterface):
    def display(self, message):
        print(f"[Command Line] {message}")