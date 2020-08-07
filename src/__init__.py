import os
import sys
import time
import pygame
import numpy as np
import threading as t
from pygame.locals import *
from ctypes import c_void_p


from .Path import Path
from .transforms import *
from .Object import Object
from .Script import Script
from .Camera import Camera
from .Shader import Shader
from .Context import Context
from .GUI.Gui import Ui_Worckbanch

from OpenGL.GL import *
from PyQt5 import QtCore, QtGui, QtWidgets