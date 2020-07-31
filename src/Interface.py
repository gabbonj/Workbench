import tkinter as tk
import numpy as np

from .transforms import *
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
button_side = 3
d_sens_step = 1
d_sens_rot = 20

class Interface(tk.Frame):

    def __init__(self, ctx, master=None):
        assert isinstance(ctx, Context)
        self.context = ctx

        tk.Frame.__init__(self, master)
        #master.resizable(False, False)

        row = 0
        
        tk.Label(self, text='Workbench', font=title_font, fg='red').grid(row=row)
        
        row += 1
        
        button_control_frame = tk.LabelFrame(self, text='BUTTON CONTROLS', bg='#eee', relief='ridge', bd=1)
        button_control_frame.grid(row=row)


        translate_frame = tk.LabelFrame(button_control_frame, text='TRANSLATE', bg='#eee', relief='ridge', bd=1)
        translate_frame.grid(row=0, column=0)

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

        tk.Label(translate_frame, text='step:', font=text_font, fg='black').grid(row=2, column=0)
        self.translate_sens = tk.Entry(translate_frame, width=5)
        self.translate_sens.grid(row=2, column=1)
        self.translate_sens.insert(tk.END, d_sens_step)
        tk.Label(translate_frame, text=' unit', font=text_font, fg='black').grid(row=2, column=2)


        rotate_frame = tk.LabelFrame(button_control_frame, text='Rotate', bg='#eee', relief='ridge', bd=1)
        rotate_frame.grid(row=0, column=1)

        pitch_up_ctlr = tk.Button(rotate_frame, text=' ↑ ', fg='green', bg='#fff', bd=1, height=button_side, width=button_side)
        pitch_up_ctlr.grid(row=0, column=1)
        pitch_up_ctlr.bind('<ButtonPress-1>', self.pitchUp)
        pitch_down_ctlr = tk.Button(rotate_frame, text=' ↓ ', fg='green', bg='#fff', bd=1, height=button_side, width=button_side)
        pitch_down_ctlr.grid(row=1, column=1)
        pitch_down_ctlr.bind('<ButtonPress-1>', self.pitchDown)
        yaw_up_ctlr = tk.Button(rotate_frame, text=' → ', fg='blue', bg='#fff', bd=1, height=button_side, width=button_side)
        yaw_up_ctlr.grid(row=1, column=2)
        yaw_up_ctlr.bind('<ButtonPress-1>', self.yawUp)
        yaw_down_ctlr = tk.Button(rotate_frame, text=' ← ', fg='blue', bg='#fff', bd=1, height=button_side, width=button_side)
        yaw_down_ctlr.grid(row=1, column=0)
        yaw_down_ctlr.bind('<ButtonPress-1>', self.yawDown)

        tk.Label(rotate_frame, text='step:', font=text_font, fg='black').grid(row=2, column=0)
        self.rotate_sens = tk.Entry(rotate_frame, width=5)
        self.rotate_sens.grid(row=2, column=1)
        self.rotate_sens.insert(tk.END, d_sens_rot)
        tk.Label(rotate_frame, text=' deg ', font=text_font, fg='black').grid(row=2, column=2)

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

    def pitchUp(self, useless):
        newpitch = self.context.camera.pitch + deg_to_rad(float(self.rotate_sens.get()))
        self.context.camera.roateCamera(newpitch, self.context.camera.yaw)

    def pitchDown(self, useless):
        newpitch = self.context.camera.pitch - deg_to_rad(float(self.rotate_sens.get()))
        self.context.camera.roateCamera(newpitch, self.context.camera.yaw)

    def yawUp(self, useless):
        newyaw = self.context.camera.yaw + deg_to_rad(float(self.rotate_sens.get()))
        self.context.camera.roateCamera(self.context.camera.pitch, newyaw)

    def yawDown(self, useless):
        newyaw = self.context.camera.yaw - deg_to_rad(float(self.rotate_sens.get()))
        self.context.camera.roateCamera(self.context.camera.pitch, newyaw)
