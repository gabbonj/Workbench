import os
import pygame
import numpy as np
import threading as t
from pygame.locals import *
from ctypes import c_void_p

from .Camera import Camera
from .Context import Context
from .Object import Object
from .Path import Path
from .Shader import Shader
from .transforms import *

from OpenGL.GL import *