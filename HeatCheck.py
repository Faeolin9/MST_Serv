import paho.mqtt.client as mqtt
import paho.mqtt.enums as en
import json


def check(heat_value, thresh=42):

    if heat_value > thresh:
        print('Drill overheating, reduce load')




# TODO your code goes here
topic_temp = 'MST/Solution/Temperature'

def on_connect(client, userdata, flags, reason_code, properties):
    print(f'Connected with result code {reason_code}')

    client.subscribe(topic_temp)



def on_message(client, userdata, msg):
    content = json.loads(msg.payload.decode())

    if msg.topic == topic_temp:
            data = content['data']
            for sample in data:
                check(sample)
   


client = mqtt.Client(en.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message
client.connect("broker.hivemq.com", 1883, 60)

client.loop_forever()
