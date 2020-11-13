# This software is distributed to you under the licence set out in the GNU General Public Licence 3.0.
# Licence avaliable at https://www.gnu.org/licenses/gpl-3.0

from microbit import * 
import radio


radio.on()
channelNum = 0                          
radio.config(channel=channelNum)
radio.config(power=7)
channelConnected = False

while channelConnected == False:
    message = radio.receive()
    print(str(channelNum))
    if message == "Attempting link":
        channelConnected = True
        radio.send("Connected") 
        display.show(Image.YES)
    elif channelNum != 83:
        channelNum += 1
        radio.config(channel=channelNum)
    else:
        channelNum = 0
