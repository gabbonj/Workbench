import os
import time
import pygame
import numpy as np
import tkinter as tk
import threading as t
from pygame.locals import *
from ctypes import c_void_p


from .Path import Path
from .transforms import *
from .Object import Object
from .Camera import Camera
from .Shader import Shader
from .Context import Context
from .Interface import Interface

from OpenGL.GL import *