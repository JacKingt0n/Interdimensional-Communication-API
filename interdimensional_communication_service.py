import json

class InterdimensionalMessage:
    def __init__(self, type, data, sender, receiver, timestamp):
        self.type = type
        self.data = data
        self.sender = sender
        self.receiver = receiver
        self.timestamp = timestamp

class InterdimensionalCommunicationService:
    def __init__(self):
        self.messages = []

    def send_message(self, message):
        # Simulate sending a message
        print(f"Sending message: {message}")
        self.messages.append(message)
        return {"status": "success"}

    def receive_messages(self):
        return self.messages
