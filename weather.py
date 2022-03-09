import tkinter as tk
import requests
import time

def getWeather(canvas):
    lat = textfield.get()
    lon = textfield2.get()
    api = "https://api.openweathermap.org/data/2.5/weather?lat="+lat+"&lon="+lon+"&appid=29d8677a8660a4c63da8f2d95fb7fcba"
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
    final_data = "\n" + "Max Temp" + str(max_temp) + "\n" + "Min_Temp" + str(min_temp) + "\n" + "Pressure" + str(pressure) + "\n" + "Humidity" + str(humidity) + "\n" + "Wind Speed" + str(wind) + "\n" + "Sunrise" + str(sunrise) + "\n" + "Sunset" + str(sunset)
    label1.config(text = final_info)
    label2.config(text = final_data)

canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")

f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

textfield = tk.Entry(canvas, font = t)
textfield.pack(pady = 20)
textfield.focus()
textfield.bind('<Return>', getWeather)

textfield2 = tk.Entry(canvas, font = t)
textfield2.pack(pady = 20)
textfield2.focus()
textfield2.bind('<Return>', getWeather)

label1 = tk.Label(canvas, font = t)
label1.pack()
label2 = tk.Label(canvas, font = f)
label2.pack()

canvas.mainloop()