from tkinter import *
import requests
import time

def getWeather():
        city = textfield.get()
        api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=29d8677a8660a4c63da8f2d95fb7fcba"
        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        temp = int(json_data['main']['temp'] - 273.15)
        min_temp = int(json_data['main']['temp_min'] - 273.15)
        max_temp = int(json_data['main']['temp_max'] - 273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']
        sunrise = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunrise'] - 21600)) #according to timezone from the time
        sunset = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunset'] - 21600))

        final_info = condition + "\n" + str(temp) + "°C"
        final_data = "\n" + "Max Temp: " + str(max_temp) + "\n" + "Min Temp: " + str(min_temp) + "\n" + "Pressure: " + str(pressure) + "\n" + "Humidity: " + str(humidity) + "\n" + "Wind Speed: " + str(wind) + "\n" + "Sunrise: " + str(sunrise) + "\n" + "Sunset: " + str(sunset)
        label1.config(text = final_info)
        label2.config(text = final_data)
    
    
class EntryWithPlaceholder(Entry):
    def __init__(self, master=None, placeholder="empty", color='grey', **kw):
        super().__init__(master, **kw)

        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']

        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)

        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    def foc_in(self, *args):
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color

    def foc_out(self, *args):
        if not self.get():
            self.put_placeholder()


root = Tk()
root.geometry("600x500")
root.title("Weather App")

f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

textfield = EntryWithPlaceholder(root, "Enter a city", font= t)
textfield.pack(pady = 20)
textfield.bind('<Return>', getWeather)

search = Button(root, text="search", command=getWeather)
search.pack(pady=10)

label1 = Label(root, font = t)
label1.pack()
label2 = Label(root, font = f)
label2.pack()

root.mainloop()