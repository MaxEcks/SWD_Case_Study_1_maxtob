class NotificationNaive:
    def __init__(self, use_slack=False, use_sms=False):
        self.use_slack = use_slack
        self.use_sms = use_sms

    def send(self, message: str):
        if self.use_slack:
            print(f"Slack: {message}")
        if self.use_sms:
            print(f"SMS: {message}")
        print(f"Default notification: {message}")

if __name__ == "__main__":
    # Example: enabling Slack notifications
    notification = NotificationNaive(use_slack=True, use_sms=False)
    notification.send("Hello World!")


class Notification:
    def send(self, message: str):
        pass

class BaseDecorator(Notification):
    def __init__(self, notification: Notification):
        self.notification = notification

    def send(self, message: str):
        self.notification.send(message)


class SlackNotificationDecorator(BaseDecorator):
    def send(self, message: str):
        print(f"Slack: {message}")
        # Mach auch das, was der Decorator bisher auch macht
        self.notification.send(message)

class SMSNotificationDecorator(BaseDecorator):
    def send(self, message: str):
        print(f"SMS: {message}")
        self.notification.send(message)

if __name__ == "__main__":
    notification = Notification()
    notification = SlackNotificationDecorator(notification)
    #notification = SMSNotificationDecorator(notification)

    notification.send("Hello World!")