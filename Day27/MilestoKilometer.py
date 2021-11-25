from tkinter import *

window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=100, height=100)

# Entry
inputs = Entry(width=30)
inputs.grid(row=0, column=1)

# Label
miles = Label(text="Miles")
miles.grid(row=0, column=2)

# Label
is_equal_to = Label(text="is equal to")
is_equal_to.grid(row=1, column=0)

# Label
solution_label = Label(text="0")
solution_label.grid(row=1, column=1)

# Label
kilometer = Label(text="Km")
kilometer.grid(row=1, column=2)


def button_clicked():
    solution_label["text"] = float(inputs.get()) * 1.61


# Button
button = Button(text="Calculate", command=button_clicked)  # command calls the button_clicked method
button.grid(row=2, column=1)

window.mainloop()
