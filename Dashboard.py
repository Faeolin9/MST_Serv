import matplotlib.pyplot as plt

import keyboard
import time


ax1 = plt.subplot(2,1,1)
def setup_ax1():
    ax1.set_title('Drill temperature')
    ax1.set_ylabel('Temperature in °C')
    ax1.set_xlabel('Seconds since measurement start')
    


ax2 = plt.subplot(2,1,2)
def setup_ax2():
    ax2.set_title('Drill power consumption')
    ax2.set_ylabel('Power in kW')
    ax2.set_xlabel('Seconds since measurement start')

plt.tight_layout(h_pad=0.3)

plt.ion()


history_temperature = []
history_power = []
last_hist_temp  = 0
last_hist_power = 0

# TODO Your Code goes here
# connect and read from MQTT and add it to the relevant lists

plt.show()
while not keyboard.is_pressed('Q'):
    if len(history_temperature) != last_hist_temp:
         last_hist_temp = len(history_temperature)
         # clear old drawing
         ax1.cla()
         setup_ax1()

         ax1.plot(history_temperature)
    if len(history_power) != last_hist_power:

        last_hist_power = len(history_power)
        # clear old drawing
        ax2.cla()
        setup_ax2()
        ax2.plot(history_power)


    time.sleep(1)
    

