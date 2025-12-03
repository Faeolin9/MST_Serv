import matplotlib.pyplot as plt
import paho.mqtt.client as mqtt
import keyboard
import time
import json
import paho.mqtt.enums as en

ax1 = plt.subplot(2,1,1)

def setup_ax1():
    ax1.set_title('Drill temperature')
    ax1.set_ylabel('Temperature in °C')
    ax1.set_xlabel('Seconds since measurement start')
setup_ax1()

ax2 = plt.subplot(2,1,2)



def setup_ax2():
    ax2.set_title('Drill power consumption')
    ax2.set_ylabel('Power in kW')
    ax2.set_xlabel('Seconds since measurement start')


plt.ion() 


history_temperature = []
history_power = []
last_hist_temp  = 0
last_hist_power = 0
topic_temp = 'MST/Solution/Temperature'
topic_power = 'MST/Solution/Power'

def on_connect(client, userdata, flags, reason_code, properties):
    print(f'Connected with result code {reason_code}')

    client.subscribe(topic_temp)
    client.subscribe(topic_power)


def on_message(client, userdata, msg):
    content = json.loads(msg.payload.decode())

    if msg.topic == topic_temp:
            history_temperature.extend(content['data'])
    elif msg.topic == topic_power:
        history_power.extend(content['data'])


client = mqtt.Client(en.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message
client.connect("broker.hivemq.com", 1883, 60)
plt.show()
plt.tight_layout(h_pad=0.3)
client.loop_start()
while not keyboard.is_pressed('q'):
    if len(history_temperature) != last_hist_temp:
         print('Getting temp data')
         last_hist_temp = len(history_temperature)
         ax1.cla()
         setup_ax1()
         ax1.plot(history_temperature)
    if len(history_power) != last_hist_power:

        last_hist_power = len(history_power)
        ax2.cla()
        setup_ax2()
        ax2.plot(history_power)
   
    plt.pause(0.01)
    
client.loop_stop()
client.disconnect()

