from tkinter import *


window = Tk()
window.geometry("500x500")
window.title("Temperature Converter")

# Title label
title_label = Label(window, text="Temperature Converter",font=('Times New Roman',27,"bold"))
title_label.pack()

# Entry box for temperature input

entry_temp = Entry(window, bg="light pink", fg="black",font=('Times New Roman',16),width=10)
entry_temp.pack(padx=5,pady=15)

# Label for showing the result

result_label = Label(window, text="", font=('Arial', 25,"bold"), fg="pink",)
result_label.place(x=200, y=150)

# Function to convert to Celsius

def to_celsius():
    try:
      f=  float(entry_temp.get())
      c= (f-32)*5/9
      result_label.configure(text=str(round(c, 2))+"°C")
    except ValueError:
     result_label.configure(text="Invalid input")

# Function to convert to Fahrenheit

def to_fahrenheit():
    try:
      c=  float(entry_temp.get())
      f= (c * 9/5) + 32
      result_label.configure(text=str(round(f, 2))+"°F")
    except ValueError:
     result_label.configure(text="Invalid input")







# Buttons (connected to functions)

Celsius_button = Button(window,text="Celsius",font=('Arial',18), command=to_celsius)
Celsius_button.place(x=130,y=100)

Fahrenheit_button = Button(window,text="Fahrenheit",font=('Arial',18),command=to_fahrenheit)
Fahrenheit_button.place(x=250,y=100)








window.mainloop()

