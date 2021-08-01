from tkinter import *


def miles_to_km():
    mile_value = float(input.get())
    km_value = mile_value*1.60934
    calculate_label.config(text=f'{round(km_value, 2)}')


### Window ###
window = Tk()
window.title('Miles to Km Converter')
window.config(padx=20, pady=20)


### Label ###
equality_label = Label(text='is equal to', font=('Arial', 12))
equality_label.grid(column=0, row=1)

calculate_label = Label(text=0, font=('Arial', 12))
calculate_label.grid(column=1, row=1)

miles_label = Label(text='Miles', font=('Arial', 12))
miles_label.grid(column=2, row=0)

km_label = Label(text='Km', font=('Arial', 12))
km_label.grid(column=2, row=1)


### Button ###
calculate_button = Button(text='Calculate', command=miles_to_km)
calculate_button.grid(column=1, row=2)


### Entry ###
input = Entry(width=10)
input.grid(column=1, row=0)


window.mainloop()