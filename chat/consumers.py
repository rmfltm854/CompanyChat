import json

from channels.generic.websocket import WebsocketConsumer

from chat import GPT

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        print(text_data)
        result = GPT.chat(text_data)
        # message = text_data_json["message"]
        print(result)
        super().send(result)