import tkinter as tk
from tkinter import *
import math
timer = None


class Application(tk.Frame):
    def __init__(self, master):
        self.master = master
        tk.Frame.__init__(self)
        self.pack()

        self.after_id = None
        self.typing_entry = Text(height=10, width=50, font=('Arial', 12))
        self.typing_entry.place(x=20, y=130)
        self.typing_entry.config(state='disabled')
        self.typing_entry.bind('<Key>', self.handle_wait)

        self.title_label = Label(text='Disappearing Text Writing App', font=('Arial', 12, 'bold'))
        self.title_label.place(x=80, y=0)

        self.start_button = Button(text='Start', command=self.start_timer)
        self.start_button.place(x=50, y=40)
        self.start_button.config(padx=10, pady=10)

        self.time_label = Label(text='Time:', font=('Arial', 12, 'bold'))
        self.time_label.place(x=150, y=40)

        self.time_text = Label(text='2:00', font=('Arial', 12, 'bold'))
        self.time_text.place(x=200, y=40)

        self.reset_button = Button(text='Reset', command=self.reset_timer)
        self.reset_button.place(x=300, y=40)
        self.reset_button.config(padx=10, pady=10)

        self.typing_label = Label(text='Type the words here:', font=('Arial', 12, 'bold'), justify=LEFT)
        self.typing_label.place(x=30, y=90)

        self.type_label = Label(text='', font=('Arial', 12, 'bold'))
        self.type_label.place(x=130, y=330)

    def handle_wait(self, event):
        if self.after_id is not None:
            self.after_cancel(self.after_id)

        self.after_id = self.after(5000, self.clear)

    def count_down(self, count):
        global timer
        count_min = math.floor(count / 60)
        count_sec = count % 60
        if count_sec < 10:
            count_sec = f"0{count_sec}"
        self.time_text.config(text=f'{count_min}:{count_sec}')
        if count > 0:
            timer = self.after(1000, self.count_down, count - 1)
        if count == 0:
            self.typing_entry.config(state='disabled')
            self.type_label.config(text="You're all done!Try again.")

    def start_timer(self):
        self.typing_entry.config(state='normal')
        self.count_down(2 * 60)

    def clear(self):
        self.typing_entry.delete(1.0, END)

    def reset_timer(self):
        self.after_cancel(timer)
        self.time_text.config(text='02:00')
        self.typing_entry.delete(1.0, END)
        self.type_label.config(text='')


root = tk.Tk()
root.minsize(width=640, height=420)
root.config(padx=100, pady=50)
app = Application(root)
app.mainloop()



