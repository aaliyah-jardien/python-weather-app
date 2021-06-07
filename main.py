# IMPORT TKINTER
from tkinter import *
from tkinter import messagebox
import requests
import requests.exceptions

# WINDOW FEATURES
window = Tk()
window.title("Weather App")
window.geometry("550x550")
window.resizable(0, 0)
window.config(bg="#51E3F2")

# DEFINING FUNCTIONS
# get weather details
def weather():
    try:
        city = enter_label.get()
        url = "https://api.openweathermap.org/data/2.5/weather?"
        weather_key = "d5f152c2169cc81875de09908d76d59a"
        params1 = {'appid': weather_key, 'q': city, 'units': 'Metric'}
        response = requests.get(url, params=params1)
        weather = response.json()
        desc_disp.configure(text='' + str(weather['weather'][0]['main']))
        temp_disp.configure(text='' + str(weather['main']['temp']))
        humi_disp.configure(text='' + str(weather['main']['humidity']))
        winds_disp.configure(text='' + str(weather['wind']['speed']))
    except requests.exceptions.ConnectionError:
        messagebox.showerror("Error", "NO internet Connection")

    except (ValueError, KeyError):
        messagebox.showerror("Error", "City cannot be found")

# clear button
def clear_btn():
    enter_label.delete(0, END)
    desc_disp.configure(text="")
    temp_disp.configure(text="")
    humi_disp.configure(text="")
    winds_disp.configure(text="")

# exit button
def exit_btn():
    sure = messagebox.askyesno(title="Alert", message="Are you sure you want to exit this window?")
    if sure == True:
        window.destroy()
    else:
        return None


# FRAME
my_frame = Frame(window, bg="#005E67")
my_frame.place(x=50, y=0, width=450, height=800)

# IMAGE
img = PhotoImage(file="Weather(1).png")
canvas = Canvas(window, width=300, height=180)
canvas.create_image(0, 0, anchor=NW, image=img)
canvas.place(x=120, y=0)

# ENTRIES
enter_label = Entry(window, borderwidth="4")
enter_label.place(x=250, y=220)

# LABELS
Label_text = StringVar

enter_city = Label(window, text=" Enter your city: ", bg="#51E3F2", borderwidth="5")
enter_city.place(x=120, y=220)

desc_label = Label(window, text=" Description: ", bg="#51E3F2", borderwidth="3")
desc_label.place(x=120, y=350)

temp_label = Label(window, text=" Temperature: ", bg="#51E3F2", borderwidth="3")
temp_label.place(x=120, y=400)

humi_label = Label(window, text=" Humidity: ", bg="#51E3F2", borderwidth="3")
humi_label.place(x=120, y=450)

winds_label = Label(window, text=" Wind Speed: ", bg="#51E3F2", borderwidth="3")
winds_label.place(x=120, y=500)

# answers in entry boxes
desc_disp = Label(window, bg="white", width="18", height="1")
desc_disp.place(x=270, y=350)

temp_disp = Label(window, bg="white", width="18", height="1")
temp_disp.place(x=270, y=400)

humi_disp = Label(window, bg="white", width="18", height="1")
humi_disp.place(x=270, y=450)

winds_disp = Label(window, bg="white", width="18", height="1")
winds_disp.place(x=270, y=500)

# BUTTONS
btn_1 = Button(window, text="Search", command=weather, bg="#51E3F2", borderwidth="4")
btn_1.place(x=120, y=270)

btn_2 = Button(window, text="Clear", command=clear_btn, bg="#51E3F2", borderwidth="4")
btn_2.place(x=240, y=270)

btn_3 = Button(window, text="Exit", command=exit_btn, bg="#51E3F2", borderwidth="4")
btn_3.place(x=360, y=270)

window.mainloop()
