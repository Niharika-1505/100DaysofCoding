import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PURPLE = "#D47AE8"
YELLOW = "#FFFEA9"
NAVY = "#0F2C67"
BLUE = "#94B3FD"
PINK = "#FD6F96"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer_change = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer_change)
    canvas.itemconfig(timer_text, text="00:00")
    timer.config(text="Timer")
    status.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_Sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_Sec)  # counts in seconds ... if minutes...1 min = 60 sec
        timer.config(text="Break", fg=NAVY)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer.config(text="Break", fg=BLUE)
    else:
        count_down(work_sec)
        timer.config(text="Work", fg=PURPLE)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer_change
    count_min = math.floor(count / 60)
    if count_min < 10:
        count_min = f"0{count_min}"

    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count >= 0:
        # after every 1000milliseconds i.e., 1 sec count_down is called and count value is passed as input
        timer_change = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        total_work_sessions = math.floor(reps / 2)
        for _ in range(total_work_sessions):
            marks += "✔"
        status.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Timer
timer = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=BLUE, bg=YELLOW)
timer.grid(row=0, column=1)

# You can get these values from the image if you open it in pycharm
# highlightthickness helps to remove the image border...remove this and see what happens..
# this can also be used for buttons, labels, etc.,
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
# these values are to adjust the image exactly in the center or adjust accordingly
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 20, "bold"))
canvas.grid(row=1, column=1)

# Start_button
start = Button(text="Start", font=(FONT_NAME, 10, "bold"), fg="black", bg=PINK, command=start_timer)
start.grid(row=2, column=0)

# Reset_button
reset = Button(text="Reset", font=(FONT_NAME, 10, "bold"), fg="black", bg=PINK, command=reset_timer)
reset.grid(row=2, column=2)

# pomodoro status
status = Label(font=(FONT_NAME, 10, "bold"), fg=NAVY, bg=YELLOW)
status.grid(row=3, column=1)

window.mainloop()
