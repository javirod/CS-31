####################################################
# CS 31, Prof. Muldrow
# Name: Javier Rodriguez
# Assignment: Chapter 13 Homework
# Due Date: 23 MAY 2021
####################################################

import tkinter
import tkinter.messagebox

########## Problem 7, Long-Distance Calls ##########
class LongDistanceGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.minutes_frame = tkinter.Frame(self.main_window)
        self.op_frame = tkinter.Frame(self.main_window)
        self.buttons_frame = tkinter.Frame(self.main_window)

        # widgets for minutes_frame
        self.minutes_label = tkinter.Label(self.minutes_frame, text = 'Enter number of minutes:')
        self.minutes_entry = tkinter.Entry(self.minutes_frame, width = 10)
        self.minutes_label.pack(side = 'left')
        self.minutes_entry.pack(side = 'left')

        # widgets for op_frame
        self.rb_var = tkinter.IntVar()
        self.rb_var.set(0)
        self.daytime_rb = tkinter.Radiobutton(self.op_frame, text = 'Daytime (6:00 am through 5:59 pm)', variable = self.rb_var, value = 1)
        self.evening_rb = tkinter.Radiobutton(self.op_frame, text = 'Evening (6:00 pm through 11:59 pm)', variable = self.rb_var, value = 2)
        self.offpeak_rb = tkinter.Radiobutton(self.op_frame, text = 'Off-Peak (midnight through 5:59 am)', variable = self.rb_var, value = 3)
        self.daytime_rb.pack(side = 'left')
        self.evening_rb.pack(side = 'left')
        self.offpeak_rb.pack(side = 'left')

        # widgets for buttons_frame
        self.calc_button = tkinter.Button(self.buttons_frame, text = 'Calculate', command = self.rate)
        self.quit_button = tkinter.Button(self.buttons_frame, text = 'Quit', command = self.main_window.destroy)
        self.calc_button.pack(side = 'left')
        self.quit_button.pack(side = 'left')

        # pack the frames and go into main loop
        self.minutes_frame.pack()
        self.op_frame.pack()
        self.buttons_frame.pack()

        tkinter.mainloop()

    def rate(self):
        self.mins = int(self.minutes_entry.get())
        if self.rb_var.get() == 1:
            self.cost = float(self.mins * .07)
        elif self.rb_var.get() == 2:
            self.cost = float(self.mins * .12)
        elif self.rb_var.get() == 3:
            self.cost = float(self.mins * .05)

        tkinter.messagebox.showinfo('Long-Distance Calls', f'Cost of the call: ${self.cost:.2f}')        

callGUI = LongDistanceGUI()