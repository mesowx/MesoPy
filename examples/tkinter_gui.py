# tkinter_gui.py
# Joshua Clark, 2015.
# This script displays a primitive GUI that displays weather information retrieved using the MesoPy package. It also
# uses PIL and urllib to download a few images from the web to display radar and satellite imagery
# Feel free to use this file as needed

from MesoPy import Meso
import urllib.request
from tkinter import *
from PIL import Image, ImageTk


# APP CREATION: The basics to generate the app window
root = Tk()
root.geometry('1800x1000+0+0')
root.title("Greeley Current Conditions")
root.config(bg="gray10")

# Retrieve observations using MesoPy and store as variable
m = Meso(api_token='3428e1e281164762870915d2ae6781b4')
latestkgxy = m.latest_obs(stid='kgxy', attime='201505010600', within='60',  units='temp|F, speed|mph')
kgxy_obs = latestkgxy['STATION'][0]['OBSERVATIONS']

# WIDGET LAYOUT: These are fairly obvious as I have tried to make variable names meaningful
whiteColor = 'ghost white'
topLine = "CURRENT CONDITIONS FOR GREELEY, COLORADO"
topText = Label(root, text=topLine, font=('Helvetica', 26), bg='gray10', fg=whiteColor)
topText.grid(row=0, column=0, sticky=W, padx=20, pady=20, columnspan=2)

updateLine = kgxy_obs['air_temp_value_1']['date_time']
updateText = Label(root, text=updateLine, font=('Helvetica', 16), bg='gray10', fg ='red')
updateText.grid(row=0, column=2, sticky=W, padx=20)

degreeSign = u'\N{DEGREE SIGN}'
temp = str(kgxy_obs['air_temp_value_1']['value']) + degreeSign + " F"
tempText = Label(root, text=temp, font=('Helvetica', 180, 'bold'), bg='gray10', fg=whiteColor)
tempText.grid(row=1, column=0, sticky=W, padx=20, columnspan=2, rowspan=5)

skyCond = "VISIBILITY: " + str(kgxy_obs['visibility_value_1']['value']) + " miles"
skyText = Label(root, text=skyCond, font=('Helvetica', 26), bg='gray10', fg=whiteColor)
skyText.grid(row=1, column=2, sticky=W, padx=20)

percentSign = u'\N{PERCENT SIGN}'
humidity = "HUMIDITY: " + str(kgxy_obs['relative_humidity_value_1']['value'])+" " + percentSign
humText = Label(root, text=humidity, font=('Helvetica', 26), bg="gray10", fg=whiteColor)
humText.grid(row=2, column=2, sticky=W, padx=20)

dewpoint = "DEWPOINT: " + str(kgxy_obs['dew_point_temperature_value_1']['value']) + degreeSign + " F"
dewText = Label(root, text=dewpoint, font=('Helvetica', 26), bg='gray10', fg=whiteColor)
dewText.grid(row=3, column=2, sticky=W, padx=20)

wind = "WIND SPEED: " + str(kgxy_obs['wind_speed_value_1']['value']) + " MPH "
windText = Label(root, text=wind, font=('Helvetica', 26), bg = 'gray10', fg = whiteColor)
windText.grid(row=4, column=2, sticky=W, padx=20)

url1 = urllib.request.urlretrieve("http://images.intellicast.com/WxImages/Radar/den.gif", "den.gif")
imUrl1 = Image.open("den.gif")    
imSmall1 = imUrl1.resize((625, 475), Image.ANTIALIAS)
img1 = ImageTk.PhotoImage(imSmall1)
finalImage1 = Label(root, image=img1, bd=2)
finalImage1.grid(row=7, column=0, columnspan=2, padx=50, pady=30, sticky=W)

url2 = urllib.request.urlretrieve("http://climate.cod.edu/data/satellite/1km/Colorado/current/Colorado.vis.gif",
                                  "Colorado.vis.gif")
imUrl2 = Image.open("Colorado.vis.gif")    
imSmall2 = imUrl2.resize((625, 475), Image.ANTIALIAS)
img2 = ImageTk.PhotoImage(imSmall2)
finalImage2 = Label(root, image=img2, bd=2)
finalImage2.grid(row=7, column=2, columnspan=2, padx=5, pady=30, sticky=W)

root.mainloop()
