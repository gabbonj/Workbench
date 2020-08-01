from logging import currentframe
import tkinter as tk
from tkinter import Label
import numpy as np
from numpy.lib.shape_base import column_stack

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

        pitch_up_ctlr = tk.Button(rotate_frame, text=' ↑ ', fg='red', bg='#fff', bd=1, height=button_side, width=button_side)
        pitch_up_ctlr.grid(row=0, column=1)
        pitch_up_ctlr.bind('<ButtonPress-1>', self.pitchUp)
        pitch_down_ctlr = tk.Button(rotate_frame, text=' ↓ ', fg='red', bg='#fff', bd=1, height=button_side, width=button_side)
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


        numeric_controll_frame = tk.LabelFrame(self, text='NUMERIC CONTROLS', bg='#eee', relief='ridge', bd=1)
        numeric_controll_frame.grid(row=row, column=1)
        
        n_translate_frame = tk.LabelFrame(numeric_controll_frame, text='TRANSLATE', bg='#eee', relief='ridge', bd=1)
        n_translate_frame.grid(row=0, column=0)

        tk.Label(n_translate_frame, text='x:', font=text_font, fg='red').grid(row=0, column=0)
        tk.Label(n_translate_frame, text='y:', font=text_font, fg='green').grid(row=1, column=0)
        tk.Label(n_translate_frame, text='z:', font=text_font, fg='blue').grid(row=2, column=0)
        
        self.x_pos = tk.Entry(n_translate_frame, width=15)
        self.x_pos.grid(row=0, column=1)
        self.x_pos.insert(tk.END, 0)
        self.y_pos = tk.Entry(n_translate_frame, width=15)
        self.y_pos.grid(row=1, column=1)
        self.y_pos.insert(tk.END, 0)
        self.z_pos = tk.Entry(n_translate_frame, width=15)
        self.z_pos.grid(row=2, column=1)
        self.z_pos.insert(tk.END, 0)
        tk.Label(n_translate_frame, text=' units ', font=text_font).grid(row=0, column=2)
        tk.Label(n_translate_frame, text=' units ', font=text_font).grid(row=1, column=2)
        tk.Label(n_translate_frame, text=' units ', font=text_font).grid(row=2, column=2)
        t_update = tk.Button(n_translate_frame, text=' UPDATE ', fg='black', bg='#fff', bd=1, width=10)
        t_update.grid(row=0, column=3)
        t_update.bind('<ButtonPress-1>', self.updateCoordinates)
        t_reset = tk.Button(n_translate_frame, text=' RESET ', fg='black', bg='#fff', bd=1, width=10)
        t_reset.grid(row=1, column=3)
        t_reset.bind('<ButtonPress-1>', self.resetCoordinates)
        t_move = tk.Button(n_translate_frame, text='MOVE TO', fg='black', bg='#fff', bd=1, width=10)
        t_move.grid(row=2, column=3)
        t_move.bind('<ButtonPress-1>', self.moveToCoordinates)

        n_rotate_frame = tk.LabelFrame(numeric_controll_frame, text='ROTATE', bg='#eee', relief='ridge', bd=1)
        n_rotate_frame.grid(row=0, column=1)

        tk.Label(n_rotate_frame, text='pitch:', font=text_font, fg='red').grid(row=0, column=0)
        tk.Label(n_rotate_frame, text='yaw:', font=text_font, fg='blue').grid(row=1, column=0)

        self.c_pitch = tk.Entry(n_rotate_frame, width=15)
        self.c_pitch.grid(row=0, column=1)
        self.c_pitch.insert(tk.END, 0)
        self.c_yaw = tk.Entry(n_rotate_frame, width=15)
        self.c_yaw.grid(row=1, column=1)
        self.c_yaw.insert(tk.END, 0)
        tk.Label(n_rotate_frame, text=' deg ', font=text_font).grid(row=0, column=2)
        tk.Label(n_rotate_frame, text=' deg ', font=text_font).grid(row=1, column=2)
        r_update = tk.Button(n_rotate_frame, text=' UPDATE ', fg='black', bg='#fff', bd=1, width=10)
        r_update.grid(row=0, column=3)
        r_update.bind('<ButtonPress-1>', self.updateAngles)
        r_reset = tk.Button(n_rotate_frame, text=' RESET ', fg='black', bg='#fff', bd=1, width=10)
        r_reset.grid(row=1, column=3)
        r_reset.bind('<ButtonPress-1>', self.resetAngles)
        r_rotate = tk.Button(n_rotate_frame, text=' ROTATE ', fg='black', bg='#fff', bd=1, width=10)
        r_rotate.grid(row=2, column=3)
        r_rotate.bind('<ButtonPress-1>', self.rotateByAngles)

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
    
    def updateCoordinates(self, useless):
        current_position = self.context.camera.position
        self.x_pos.delete(0, tk.END)
        self.y_pos.delete(0, tk.END)
        self.z_pos.delete(0, tk.END)
        self.x_pos.insert(tk.END, current_position[0])
        self.y_pos.insert(tk.END, current_position[1])
        self.z_pos.insert(tk.END, current_position[2])

    def resetCoordinates(self, useless):
        self.x_pos.delete(0, tk.END)
        self.y_pos.delete(0, tk.END)
        self.z_pos.delete(0, tk.END)
        self.x_pos.insert(tk.END, 0)
        self.y_pos.insert(tk.END, 0)
        self.z_pos.insert(tk.END, 0)

    def moveToCoordinates(self, useless):
        newpos = [float(self.x_pos.get()), float(self.y_pos.get()), float(self.x_pos.get())]
        self.context.camera.setCameraPosition(newpos)

    def updateAngles(self, useless):
        self.c_pitch.delete(0, tk.END)
        self.c_yaw.delete(0, tk.END)
        self.c_pitch.insert(tk.END, int(rad_to_deg(self.context.camera.pitch)))
        self.c_yaw.insert(tk.END, int(rad_to_deg(self.context.camera.yaw)))

    def resetAngles(self, useless):
        self.c_pitch.delete(0, tk.END)
        self.c_yaw.delete(0, tk.END)
        self.c_pitch.insert(tk.END, 0)
        self.c_yaw.insert(tk.END, 0)

    def rotateByAngles(self, useless):
        newpitch = deg_to_rad(float(self.c_pitch.get()))
        newyaw = deg_to_rad(float(self.c_yaw.get()))
        self.context.camera.roateCamera(newpitch, newyaw)
