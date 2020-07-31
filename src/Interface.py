import tkinter as tk
import numpy as np
from .Context import Context

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
button_side = 2
d_sens = 1

class Interface(tk.Frame):

    def __init__(self, ctx, master=None):
        assert isinstance(ctx, Context)
        self.context = ctx

        tk.Frame.__init__(self, master)
        master.resizable(False, False)

        row = 0
        
        tk.Label(self, text='Workbench', font=title_font, fg='red').grid(row=row)
        
        row += 1
        
        control_frame = tk.LabelFrame(self, text='CONTROLS', bg='#eee', relief='ridge', bd=1)
        control_frame.grid(row=row)

        translate_frame = tk.LabelFrame(control_frame, text='TRANSLATE', bg='#eee', relief='ridge', bd=1)
        translate_frame.grid(column=0)

        up_ctlr = tk.Button(translate_frame, text=' ↑ ', fg='green', bg='#fff', bd=1, height=button_side, width=button_side)
        up_ctlr.grid(row=0, column=1)
        up_ctlr.bind('<ButtonPress-1>', self.moveUp)
        down_ctlr = tk.Button(translate_frame, text=' ↓ ', fg='green', bg='#fff', bd=1, height=button_side, width=button_side)
        down_ctlr.grid(row=1, column=1)
        down_ctlr.bind('<ButtonPress-1>', self.moveDown)
        right_ctlr = tk.Button(translate_frame, text=' → ', fg='blue', bg='#fff', bd=1, height=button_side, width=button_side)
        right_ctlr.grid(row=1, column=2)
        right_ctlr.bind('<ButtonPress-1>', self.moveRight)
        left_ctlr = tk.Button(translate_frame, text=' ← ', fg='blue', bg='#fff', bd=1, height=button_side, width=button_side)
        left_ctlr.grid(row=1, column=0)
        left_ctlr.bind('<ButtonPress-1>', self.moveLeft)
        fwd_ctrl = tk.Button(translate_frame, text=' > ', fg='red', bg='#fff', bd=1, height=button_side, width=button_side)
        fwd_ctrl.grid(row=0, column=2)
        fwd_ctrl.bind('<ButtonPress-1>', self.moveFwd)
        back_ctrl = tk.Button(translate_frame, text=' < ', fg='red', bg='#fff', bd=1, height=button_side, width=button_side)
        back_ctrl.grid(row=0, column=0)
        back_ctrl.bind('<ButtonPress-1>', self.moveBack)

        self.translate_sens = tk.Entry(translate_frame, width=5)
        self.translate_sens.grid(row=2, column=1)
        self.translate_sens.insert(tk.END, d_sens)

        self.pack()

    def moveUp(self, useless):
        newpos = self.context.camera.position + np.array([0, float(self.translate_sens.get()), 0])
        self.context.camera.setCameraPosition(newpos)

    def moveDown(self, useless):
        newpos = self.context.camera.position + np.array([0, -float(self.translate_sens.get()), 0])
        self.context.camera.setCameraPosition(newpos)

    def moveRight(self, useless):
        newpos = self.context.camera.position + np.array([0, 0, float(self.translate_sens.get())])
        self.context.camera.setCameraPosition(newpos)

    def moveLeft(self, useless):
        newpos = self.context.camera.position + np.array([0, 0, -float(self.translate_sens.get())])
        self.context.camera.setCameraPosition(newpos)

    def moveFwd(self, useless):
        newpos = self.context.camera.position + np.array([float(self.translate_sens.get()), 0, 0])
        self.context.camera.setCameraPosition(newpos)
        
    def moveBack(self, useless):
        newpos = self.context.camera.position + np.array([-float(self.translate_sens.get()), 0, 0])
        self.context.camera.setCameraPosition(newpos)