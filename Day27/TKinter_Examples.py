from tkinter import *

window = Tk()
window.title("First TKinter program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="I am a Label", font=("Arial", 20, "bold"))
my_label.pack(side="top")  # left, bottom, right, top
# my_label["text"] = "New Text"  # Two ways to configure labels
my_label.config(text="New Text")  # Two ways to configure labels


def button_clicked():
    my_label["text"] = "You clicked the button and so the text in the text box is: " + inputs.get()


# Button
button = Button(text="Button", command=button_clicked)  # command calls the button_clicked method
button.pack(side="top")

# Entry
inputs = Entry(width=30)
inputs.insert(END, string="Some text to begin with.")
inputs.pack()

# Text - used to create Multiline Textbox
text = Text(height=5, width=30)
text.focus()  # To place the cursor here by default
text.insert(END, "Example of multi-line text entry")
print(text.get("1.0", END))
text.pack()


# Spinbox or a dropdown
def spinbox_used():
    print("Spinbox", spinbox.get())  # Gets current value from spinbox


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


# Scale
def scale_used(value):
    print("Scale ", value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


# Checkbutton
def checkbutton_used():
    # Prints 1 if On button checked, otherwise 0.
    print("Check box: ", checked_state.get())


# variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()


# Radiobutton
def radio_used():
    print("Radio button ", radio_state.get())


# Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


# Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print("Listbox ", listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop()
