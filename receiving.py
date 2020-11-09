# This software is distributed to you under the licence set out in the GNU General Public Licence 3.0.
# Licence avaliable at https://www.gnu.org/licenses/gpl-3.0

#Import libraries
from microbit import * 
import radio

#setting up radio
radio.on()
channelNum = 0                          
radio.config(channel=channelNum)
radio.config(power=7)
channelConnected = False

#event loop
while channelConnected == False:
    message = radio.receive() #recieving message
    print(str(channelNum)) #printing the channel number to console
    if message == "Attempting link":
        channelConnected = True #see if channel is received
        radio.send("Connected") 
        display.show(Image.YES)
        #increment channel by 1 if below 83 otherwise 0
    elif channelNum != 83:
        channelNum += 1
        radio.config(channel=channelNum)
    else:
        channelNum = 0
