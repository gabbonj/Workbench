import tkinter as tk

colours = {
    'white': (255, 255, 255),
    'black': (0, 0, 0),
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255)
}

title_font = ("Courier", 20)
section_font = ("Courier", 15)
text_font = ("Courier", 10)


class Interface(tk.Frame):

    def __init__(self, ctx, master=None):
        self.context = ctx
        
        tk.Frame.__init__(self, master)
        master.resizable(False, False)

        row = 0

        title = tk.Label(self, text='Workbench', font=title_font, fg='red')
        title.grid(row=row)


        self.pack()