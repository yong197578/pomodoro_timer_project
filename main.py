from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_time():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_mark.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    reps += 1
    # 25 min | 5 min x 4 and long break 20min
    if reps % 8 == 0:
        count_down(long_break)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    # print(count)
    # if count > 0:
    #     window.after(1000, count_down, count - 1)
    # format to 00:00
    # ex. 245 / 60 = 4 min with round 245% 60 = rest of sec
    count_min = math.floor(count / 60)
    # How to make it 5:00 -> if statement and dynamic typing
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = " "
        work_session = math.floor(reps/2)
        for i in range(work_session):
            marks += "✔"

        check_mark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)
# created canvas object and set width/height by image size | highlightthickness removes border
canvas = Canvas(width=200, height=244, bg=YELLOW, highlightthickness=0)
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
timer_label.grid(column=1, row=0)
# using PhotoImage method to recognize the tomato.png
tomato_img = PhotoImage(file="tomato.png")
# using create_image method to set position of x, y coord and attach image
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)
start_button = Button(text="START", highlightthickness=0, highlightbackground=YELLOW, command=start_timer)
start_button.grid(column=0, row=3)

reset_button = Button(text="RESET", highlightthickness=0, highlightbackground=YELLOW, command=reset_time)
reset_button.grid(column=3, row=3)
check_mark = Label(bg=YELLOW, fg=GREEN)
check_mark.grid(column=1, row=4)

window.mainloop()