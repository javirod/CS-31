####################################################
# CS 31, Prof. Muldrow
# Name: Javier Rodriguez
# Assignment: Chapter 13 Homework
# Due Date: 23 MAY 2021
####################################################

import tkinter

########## Problem 4, Celsius to Fahrenheit ##########
class TempGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.num_frame = tkinter.Frame(self.main_window)
        self.res_frame = tkinter.Frame(self.main_window)
        self.buttons_frame = tkinter.Frame(self.main_window)

        # widgets for num_frame
        self.num_label = tkinter.Label(self.num_frame, text = 'Enter temperature in Celsius:')
        self.num_entry = tkinter.Entry(self.num_frame, width = 10)
        self.num_label.pack(side = 'left')
        self.num_entry.pack(side = 'left')

        # widgets for res_frame
        self.res_label = tkinter.Label(self.res_frame, text = 'Temperature (Fahrenheit) =')
        self.ans = tkinter.StringVar() # variable that contains result
        self.ans_label = tkinter.Label(self.res_frame, textvariable = self.ans)
        self.res_label.pack(side = 'left')
        self.ans_label.pack(side = 'left')

        # widgets for buttons_frame
        self.calc_button = tkinter.Button(self.buttons_frame, text = 'Convert', command = self.convertTemp)
        self.quit_button = tkinter.Button(self.buttons_frame, text = 'Quit', command = self.main_window.destroy)
        self.calc_button.pack(side = 'left')
        self.quit_button.pack(side = 'left')

        # pack the frames and go into main loop
        self.num_frame.pack()
        self.res_frame.pack()
        self.buttons_frame.pack()

        tkinter.mainloop()

    def convertTemp(self):
        self.num = float(self.num_entry.get())
        self.ans.set((9/5)*(self.num)+32)

tempGUI = TempGUI()