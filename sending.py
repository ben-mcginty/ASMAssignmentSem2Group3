# This software is distributed to you under the licence set out in the GNU General Public Licence 3.0.
# Licence avaliable at https://www.gnu.org/licenses/gpl-3.0

from microbit import *
import radio
import random

channel = random.randrange(1,82,0)
radio.on()
radio.config(channel=channel)
radio.config(power=7)

display.scroll(channel)

while True:
    radio.send("Attempting link")
    dataRecieved = radio.receive()
    if dataRecieved == "Connected":
        display.show(Image.YES)
        break
