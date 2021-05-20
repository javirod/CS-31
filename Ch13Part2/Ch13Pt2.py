# Week 15, ICA 2
import tkinter
import tkinter.messagebox

class MathGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.num1_frame = tkinter.Frame(self.main_window)
        self.num2_frame = tkinter.Frame(self.main_window)
        self.op_frame = tkinter.Frame(self.main_window)
        self.res_frame = tkinter.Frame(self.main_window)
        self.cb_frame = tkinter.Frame(self.main_window)
        self.buttons_frame = tkinter.Frame(self.main_window)

        # widgets for num1_frame
        self.num1_label = tkinter.Label(self.num1_frame, text = 'Enter first number:')
        self.num1_entry = tkinter.Entry(self.num1_frame, width = 10)
        self.num1_label.pack(side = 'left')
        self.num1_entry.pack(side = 'left')

        # widgets for num1_frame
        self.num2_label = tkinter.Label(self.num2_frame, text = 'Enter second number:')
        self.num2_entry = tkinter.Entry(self.num2_frame, width = 10)
        self.num2_label.pack(side = 'left')
        self.num2_entry.pack(side = 'left')

        # widgets for op_frame
        self.rb_var = tkinter.IntVar()
        self.rb_var.set(0)
        self.add_rb = tkinter.Radiobutton(self.op_frame, text = 'Add', variable = self.rb_var, value = 1, command = self.add)
        self.sub_rb = tkinter.Radiobutton(self.op_frame, text = 'Subtract', variable = self.rb_var, value = 2, command = self.subtract)
        self.mult_rb = tkinter.Radiobutton(self.op_frame, text = 'Multiply', variable = self.rb_var, value = 3, command = self.multiply)
        self.add_rb.pack(side = 'left')
        self.sub_rb.pack(side = 'left')
        self.mult_rb.pack(side = 'left')

        # widgets for res_frame
        self.res_label = tkinter.Label(self.res_frame, text = 'Answer =')
        self.ans = tkinter.StringVar() # variable that contains result
        self.ans_label = tkinter.Label(self.res_frame, textvariable = self.ans)
        self.res_label.pack(side = 'left')
        self.ans_label.pack(side = 'left')

        # widgets for cb_frame
        self.cb1_var = tkinter.IntVar()
        self.cb1_var.set(0)
        self.cb2_var = tkinter.IntVar()
        self.cb2_var.set(0)
        self.cb1 = tkinter.Checkbutton(self.cb_frame, text = 'Monty Python', variable = self.cb1_var)
        self.cb2 = tkinter.Checkbutton(self.cb_frame, text = 'Star Trek', variable = self.cb2_var)
        self.cb1.pack(side='left')
        self.cb2.pack(side='left')

        # widgets for buttons_frame
        self.calc_button = tkinter.Button(self.buttons_frame, text = 'Go!', command = self.whatever)
        self.quit_button = tkinter.Button(self.buttons_frame, text = 'Quit', command = self.main_window.destroy)
        self.calc_button.pack(side = 'left')
        self.quit_button.pack(side = 'left')

        # pack the frames and go into main loop
        self.num1_frame.pack()
        self.num2_frame.pack()
        self.op_frame.pack()
        self.res_frame.pack()
        self.cb_frame.pack()
        self.buttons_frame.pack()

        tkinter.mainloop()

    def add(self):
        self.num1 = int(self.num1_entry.get())
        self.num2 = int(self.num2_entry.get())
        self.ans.set(self.num1 + self.num2)

    def subtract(self):
        self.num1 = int(self.num1_entry.get())
        self.num2 = int(self.num2_entry.get())
        self.ans.set(self.num1 - self.num2)

    def multiply(self):
        self.num1 = int(self.num1_entry.get())
        self.num2 = int(self.num2_entry.get())
        self.ans.set(self.num1 * self.num2)

    def whatever(self):
        self.quote = 'Quote of the day:\n'
        if self.cb1_var.get() == 1:
            self.quote += 'And now for something completely different!\n'
        if self.cb2_var.get() == 1:
            self.quote += 'I cannot perform miracles captain! I need more time!\n'
        tkinter.messagebox.showinfo('Whatever', self.quote)

mathGUI = MathGUI()