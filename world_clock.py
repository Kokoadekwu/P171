import tkinter as tk
from tkinter import PhotoImage, Button, Label
from datetime import datetime
import pytz

class WorldClockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("World Clock")
        self.root.geometry("400x400")

        # Load map images
        self.india_image = PhotoImage(file="india_map.png")
        self.usa_image = PhotoImage(file="usa_map.png")
        self.australia_image = PhotoImage(file="australia_map.png")
        self.japan_image = PhotoImage(file="japan_map.png")

        # Display India map
        self.india_clock = Label(root, image=self.india_image)
        self.india_clock.place(relx=0.2, rely=0.1)

        # Display USA map
        self.usa_clock = Label(root, image=self.usa_image)
        self.usa_clock.place(relx=0.6, rely=0.1)

        # Buttons to show time for India and USA
        self.btn_india_time = Button(root, text="Show India Time", command=self.show_india_time)
        self.btn_india_time.place(relx=0.2, rely=0.4)

        self.btn_usa_time = Button(root, text="Show USA Time", command=self.show_usa_time)
        self.btn_usa_time.place(relx=0.6, rely=0.4)

        # Labels for Australia
        self.australia_label = Label(root, text="Australia")
        self.australia_label.place(relx=0.2, rely=0.7)

        self.australia_map = Label(root, image=self.australia_image)
        self.australia_map.place(relx=0.2, rely=0.8)

        self.australia_time_label = Label(root, text="")
        self.australia_time_label.place(relx=0.2, rely=0.9)

        # Button to show time for Australia
        self.btn_australia_time = Button(root, text="Show Australia Time", command=self.show_australia_time)
        self.btn_australia_time.place(relx=0.2, rely=0.6)

        # Labels for Japan
        self.japan_label = Label(root, text="Japan")
        self.japan_label.place(relx=0.6, rely=0.7)

        self.japan_map = Label(root, image=self.japan_image)
        self.japan_map.place(relx=0.6, rely=0.8)

        self.japan_time_label = Label(root, text="")
        self.japan_time_label.place(relx=0.6, rely=0.9)

        # Button to show time for Japan
        self.btn_japan_time = Button(root, text="Show Japan Time", command=self.show_japan_time)
        self.btn_japan_time.place(relx=0.6, rely=0.6)

    def show_india_time(self):
        india_timezone = pytz.timezone('Asia/Kolkata')
        india_time = datetime.now(india_timezone).strftime('%H:%M:%S')
        self.india_time_label.config(text="Time: " + india_time)

    def show_usa_time(self):
        usa_timezone = pytz.timezone('US/Central')
        usa_time = datetime.now(usa_timezone).strftime('%H:%M:%S')
        self.usa_time_label.config(text="Time: " + usa_time)

    def show_australia_time(self):
        australia_timezone = pytz.timezone('Australia/ACT')
        australia_time = datetime.now(australia_timezone).strftime('%H:%M:%S')
        self.australia_time_label.config(text="Time: " + australia_time)

    def show_japan_time(self):
        japan_timezone = pytz.timezone('Japan')
        japan_time = datetime.now(japan_timezone).strftime('%H:%M:%S')
        self.japan_time_label.config(text="Time: " + japan_time)

root = tk.Tk()
app = WorldClockApp(root)
root.mainloop()
