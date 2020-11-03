# This software is distributed to you under the licence set out in the GNU General Public Licence 3.0.
# Licence avaliable at https://www.gnu.org/licenses/gpl-3.0

from microbit import *
import radio
import random
radio.on()
channelNum = random.randrange(1,100)
radio.config(channel=channelNum)        # Choose your own channel number
radio.config(power=7)           # Turn the signal up to full strength

display.scroll(channelNum)

# Event loop.
while False:
    radio.send("Attempting link")
    dataRecieved = radio.recieve()
    if dataRecieved == "Channel is "+ str(channelNum):
        radio.send("Correct channel")
        display.show(Image.YES)
        break
display.scroll("YAY")
