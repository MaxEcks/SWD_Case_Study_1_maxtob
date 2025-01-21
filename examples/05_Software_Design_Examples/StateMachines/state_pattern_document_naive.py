class Document:
    def __init__(self):
        self.state = "draft"

    def publish(self, current_user):
        if self.state == "draft":
            if current_user.role == "user":
                self.state = "moderation"
            elif current_user.role == "admin":
                self.state = "published"
        elif self.state == "moderation":
            if current_user.role == "admin":
                self.state = "published"
        elif self.state == "published":
            pass  # Do nothing.

# Example usage:
class User:
    def __init__(self, role):
        self.role = role

# Create a draft document
doc = Document()
print("Initial State:", doc.state)  # Output: Initial State: draft

# Transition to moderation
doc.publish(User(role="user"))
print("After publish (non-admin):", doc.state)  # Output: After publish (non-admin): moderation

# Transition to published (admin)
doc.publish(User(role="admin"))
print("After publish (admin):", doc.state)  # Output: After publish (admin): published