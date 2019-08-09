from flask import Flask 
from flask_restful import Resource, Api
import queue 
import paho.mqtt.client as mqtt
import threading

broker_url = "127.0.0.1"
broker_port = 1883
client = mqtt.Client()
client.connect(broker_url, broker_port)

message_stack = []

app = Flask(__name__)
api = Api(app)

class TopicHandler:
    message_dict = {}
    @classmethod
    def create(cls, topic):
        print("Init " + topic + " topic")
        if topic not in cls.message_dict.keys():
            cls.message_dict[topic] = []
    @classmethod
    def on_message(cls, client, userdata, message):
        print(message.topic + "\t" + message.payload.decode())
        cls.message_dict[message.topic].append(message.payload.decode())

# class MqttThread(threading.Thread):
#     def __init__(self):
#         client.on_message = self.on_message
#     def on_message(self, client, userdata, message):

#     def run(self):
#         client.loop_forever()

class Subscribe(Resource):
    def get(self, topic):
        # return TopicHandler.message_dict[topic].pop()
        if len(TopicHandler.message_dict[topic]) != 0:
            print("List not empty")
            return TopicHandler.message_dict[topic].pop()
        else:
            return "", 200
    def put(self, topic):
        print(topic)
        client.subscribe(topic)
        TopicHandler.create(topic)
        client.on_message = TopicHandler.on_message
        return '',201
    def delete(self, topic):
        client.unsubscribe(topic)
        del TopicHandler.message_dict[topic]
        return '',204
class Publish(Resource):
    def get(self):
        return
    def put(self):
        return 

api.add_resource(Subscribe, '/subscribe/<string:topic>')
api.add_resource(Publish, '/publish/<string:topic>')

if __name__ == '__main__':
    client.loop_start()
    app.run(port=9001)
