from abc import ABC, abstractmethod # step-1

# only blueprint
# cannot create object
class NotificationService(ABC): # step-2

    @abstractmethod # decorator
    def send_message(self, message):
        pass
    
    @abstractmethod
    def read_message(self, message):
        pass

    def add(self):
        print("Abstract class add")

class EmailNotification(NotificationService):

    def send_message(self, message):
        return f"Sending email with message : {message}"

    def read_message(self, message):
            return f"Reading message : {message}"

class SlackNotification(NotificationService):

    def send_message(self, message):
        return f"Sending Slack-messagge with message : {message}"

    def send_message_slack(self, message):
        return f"Sending Whatsapp-messagge with message : {message}"

    def read_message(self, message):
        return f"Reading message : {message}"
    
obj_1 = EmailNotification()
obj_4 = SlackNotification()