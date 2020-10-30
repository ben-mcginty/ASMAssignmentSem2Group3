# This software is distributed to you under the licence set out in the GNU General Public Licence 3.0.
# Licence avaliable at https://www.gnu.org/licenses/gpl-3.0

from microbit import *
import radio

radio.on()                           # Turns on radio
channel = 0                          
radio.config(channel=channel)              # Choose your own channel number
radio.config(power=7)                # Turn the signal up to full strength
channelConnected = False

while channelConnected == False:
    recieve = radio.recieve()
    if recieve == "Attempting link":
        channelConnected = True
        radio.send("Channel is "+ str(channel))
        display.show(Image.YES)
    else:
        channel += 1
        radio.config(channel=channel)