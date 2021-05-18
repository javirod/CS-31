# Week 15, ICA 1
import tkinter
import tkinter.messagebox

class GUI:
    def __init__(self):
        # Create the main window widget
        self.main_window = tkinter.Tk()

        # Create two frames, one for the top of the
        # window, and one for the bottom.
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Create a Label widget containing text
        self.label1 = tkinter.Label(self.top_frame, text = 'Javier Rodriguez')
        self.label2 = tkinter.Label(self.bottom_frame, text = 'LBCC')
        self.label3 = tkinter.Label(self.bottom_frame, text = 'Computer Science')

        # Call the Label widget's pack method
        self.label1.pack()
        self.label2.pack(side = 'left')
        self.label3.pack(side = 'left')

        # Call the Frame widget's pack method
        self.top_frame.pack()
        self.bottom_frame.pack()

        self.button1 = tkinter.Button(self.main_window, text = 'Click Here', command = self.display)
        self.button2 = tkinter.Button(self.main_window, text = 'Quit', command = self.main_window.destroy)

        self.button1.pack(side = 'left')
        self.button2.pack(side = 'right')

        # Enter the tkinter main loop
        tkinter.mainloop()

    def display(self):
        tkinter.messagebox.showinfo('Success!',"That's the end of the ICA!")


# Create an instance of the MyGUI class
my_gui = GUI()