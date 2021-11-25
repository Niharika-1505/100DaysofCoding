from tkinter import *


def button_clicked():
    print("I got clicked")
    new_text = inputs.get()
    my_label.config(text=new_text)


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
# my_label.place(x=-100, y=-200)  # Places label in certain position by taking x and y axis
my_label.config(padx=50, pady=50)

# Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=1, row=0)

# Entry
inputs = Entry(width=10)
print(inputs.get())
inputs.grid(column=0, row=1)

window.mainloop()
