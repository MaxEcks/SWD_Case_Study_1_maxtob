from abc import ABC
from abc import abstractmethod

class State(ABC):

    @abstractmethod
    def publish(self, document, current_user):
        pass

class Draft(State):
    def publish(self, document, current_user):
        if current_user.role == "user":
            document.state = Moderation()
        elif current_user.role == "admin":
            document.state = Published()

class Moderation(State):
    def publish(self, document, current_user):
        if current_user.role == "admin":
            document.state = Published()

class Published(State):
    def publish(self, document, current_user):
        pass  # Do nothing.

class Document:
    def __init__(self):
        self.state = Draft()

    def publish(self, current_user):
        self.state.publish(self, current_user)

# Example usage:
class User:
    def __init__(self, role):
        self.role = role

# Create a draft document
doc = Document()
print("Initial State:", type(doc.state).__name__)  # Output: Initial State: Draft

# Transition to moderation
doc.publish(User(role="user"))
print("After publish (non-admin):", type(doc.state).__name__)  # Output: After publish (non-admin): Moderation

# Transition to published (admin)
doc.publish(User(role="admin"))
print("After publish (admin):", type(doc.state).__name__)  # Output: After publish (admin): Published