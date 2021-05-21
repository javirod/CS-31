####################################################
# CS 31, Prof. Muldrow
# Name: Javier Rodriguez
# Assignment: Chapter 13 Homework
# Due Date: 23 MAY 2021
####################################################

import tkinter
import tkinter.messagebox

########## Problem 6, Joe's Automotive ##########
class AutoServiceGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.main_window)
        self.cb_frame = tkinter.Frame(self.main_window)
        self.buttons_frame = tkinter.Frame(self.main_window)

        # widgets for top_frame
        self.top_frame_label1 = tkinter.Label(self.top_frame, text = "Welcome to Joe's Automotive.")
        self.top_frame_label2 = tkinter.Label(self.top_frame, text = "Please select from our services below.")
        self.top_frame_label1.pack(side = 'top')
        self.top_frame_label2.pack(side = 'top')

        # widgets for cb_frame
        self.cb1_var = tkinter.IntVar()
        self.cb1_var.set(0)
        self.cb2_var = tkinter.IntVar()
        self.cb2_var.set(0)
        self.cb3_var = tkinter.IntVar()
        self.cb3_var.set(0)
        self.cb4_var = tkinter.IntVar()
        self.cb4_var.set(0)
        self.cb5_var = tkinter.IntVar()
        self.cb5_var.set(0)
        self.cb6_var = tkinter.IntVar()
        self.cb6_var.set(0)
        self.cb7_var = tkinter.IntVar()
        self.cb7_var.set(0)
        self.cb1 = tkinter.Checkbutton(self.cb_frame, text = 'Oil change', variable = self.cb1_var)
        self.cb2 = tkinter.Checkbutton(self.cb_frame, text = 'Lube job', variable = self.cb2_var)
        self.cb3 = tkinter.Checkbutton(self.cb_frame, text = 'Radiator flush', variable = self.cb3_var)
        self.cb4 = tkinter.Checkbutton(self.cb_frame, text = 'Transmission flush', variable = self.cb4_var)
        self.cb5 = tkinter.Checkbutton(self.cb_frame, text = 'Inspection', variable = self.cb5_var)
        self.cb6 = tkinter.Checkbutton(self.cb_frame, text = 'Muffler replacement', variable = self.cb6_var)
        self.cb7 = tkinter.Checkbutton(self.cb_frame, text = 'Tire rotation', variable = self.cb7_var)
        self.cb1.pack(side='left')
        self.cb2.pack(side='left')
        self.cb3.pack(side='left')
        self.cb4.pack(side='left')
        self.cb5.pack(side='left')
        self.cb6.pack(side='left')
        self.cb7.pack(side='left')

        # widgets for buttons_frame
        self.calc_button = tkinter.Button(self.buttons_frame, text = 'Get Total', command = self.serviceTotal)
        self.quit_button = tkinter.Button(self.buttons_frame, text = 'Quit', command = self.main_window.destroy)
        self.calc_button.pack(side = 'left')
        self.quit_button.pack(side = 'left')

        # pack the frames and go into main loop
        self.top_frame.pack()
        self.cb_frame.pack()
        self.buttons_frame.pack()

        tkinter.mainloop()

    def serviceTotal(self):
        self.total = 0
        if self.cb1_var.get() == 1:
            self.total += 30
        if self.cb2_var.get() == 1:
            self.total += 20
        if self.cb3_var.get() == 1:
            self.total += 40
        if self.cb4_var.get() == 1:
            self.total += 100
        if self.cb5_var.get() == 1:
            self.total += 35
        if self.cb6_var.get() == 1:
            self.total += 200
        if self.cb7_var.get() == 1:
            self.total += 20
        tkinter.messagebox.showinfo("Joe's Automotive", f'Total Cost: ${self.total:.2f}')

autoGUI = AutoServiceGUI()