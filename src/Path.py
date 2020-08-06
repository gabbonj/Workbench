import numpy as np
from ctypes import c_void_p

from .Shader import Shader
from .transforms import *

from OpenGL.GL import *

class Path:

    # position=[x1, y1, z1, ..., xn, yn, zn] ; rotation = [[Rx1, Ry1, Rz1], ..., [Rxn, Ryn, Rzn]] 
    def __init__(self, position, rotation=None):
        self.loadPath(position)
        
        if rotation:
            assert len(position) == len(rotation) * 3
            self.loadRotation(rotation)
        else:
            self.rotation = 'Pio è un figo'
        

    def loadPath(self, position):
        # compiling shader
        self.path_shader = Shader('src\\shaders\\path\\pathvert.glsl',
                                  'src\\shaders\\path\\pathfrag.glsl').shaderProgram

        # setting path buffer
        self.vertices = position
        self.patharray = glGenVertexArrays(1)
        glBindVertexArray(self.patharray)
        self.lineBuffer = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.lineBuffer)
        glBufferData(GL_ARRAY_BUFFER, np.array(self.vertices, dtype='float32'), GL_STATIC_DRAW)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * 4, c_void_p(0))

    def loadRotation(self, rotation):
        self.rotation = rotation

        # compiling shader
        self.xpath_shader = Shader('src\\shaders\\path\\pathvert.glsl',
                                   'src\\shaders\\path\\xpathfrag.glsl').shaderProgram
        self.ypath_shader = Shader('src\\shaders\\path\\pathvert.glsl',
                                   'src\\shaders\\path\\ypathfrag.glsl').shaderProgram
        self.zpath_shader = Shader('src\\shaders\\path\\pathvert.glsl',
                                   'src\\shaders\\path\\zpathfrag.glsl').shaderProgram

        # setting versors
        self.xvertices = []
        self.yvertices = []
        self.zvertices = []
        for pos in range(len(rotation)):
            xversor = self.getVersorAtTime(np.array([1, 0, 0, 1], dtype='float32'), pos)
            yversor = self.getVersorAtTime(np.array([0, 1, 0, 1], dtype='float32'), pos)
            zversor = self.getVersorAtTime(np.array([0, 0, 1, 1], dtype='float32'), pos)
            
            pos = [self.vertices[pos*3], self.vertices[pos*3 + 1], self.vertices[pos*3 + 2]]
            self.xvertices.extend(pos)
            self.xvertices.extend([xversor[0], xversor[1], xversor[2]])
            self.yvertices.extend(pos)
            self.yvertices.extend([yversor[0], yversor[1], yversor[2]])
            self.zvertices.extend(pos)
            self.zvertices.extend([zversor[0], zversor[1], zversor[2]])

        #setting xline bufer
        self.xpatharray = glGenVertexArrays(1)
        glBindVertexArray(self.xpatharray)
        self.xlineBuffer = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.xlineBuffer)
        glBufferData(GL_ARRAY_BUFFER, np.array(self.xvertices, dtype='float32'), GL_STATIC_DRAW)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * 4, c_void_p(0))

        # setting yline buffer
        self.ypatharray = glGenVertexArrays(1)
        glBindVertexArray(self.ypatharray)
        self.ylineBuffer = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.ylineBuffer)
        glBufferData(GL_ARRAY_BUFFER, np.array(self.yvertices, dtype='float32'), GL_STATIC_DRAW)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * 4, c_void_p(0))

        #setting xline bufer
        self.zpatharray = glGenVertexArrays(1)
        glBindVertexArray(self.zpatharray)
        self.zlineBuffer = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.zlineBuffer)
        glBufferData(GL_ARRAY_BUFFER, np.array(self.zvertices, dtype='float32'), GL_STATIC_DRAW)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * 4, c_void_p(0))

    def getVersorAtTime(self, versor, index):
        r_versor = np.dot(get_rot(self.rotation[index][0], 0), versor)
        r_versor = np.dot(get_rot(self.rotation[index][1], 1), r_versor)
        r_versor = np.dot(get_rot(self.rotation[index][2], 2), r_versor)
        t_versor = np.dot(get_traslation(self.vertices[index*3], self.vertices[index*3 + 1], self.vertices[index*3 + 2]), r_versor)
        return t_versor

    def renderPath(self, camera):
        model = np.identity(4)
        view = camera.view
        proj = camera.proj

        # rendering the path
        glBindVertexArray(self.patharray)
        glUseProgram(self.path_shader)
        modelLocation = glGetUniformLocation(self.path_shader, 'model')
        viewLocation = glGetUniformLocation(self.path_shader, 'view')
        projectionLocation = glGetUniformLocation(self.path_shader, 'projection')
        glUniformMatrix4fv(modelLocation, 1, GL_TRUE, model)
        glUniformMatrix4fv(viewLocation, 1, GL_TRUE, view)
        glUniformMatrix4fv(projectionLocation, 1, GL_FALSE, proj)
        glEnableVertexAttribArray(0)
        glDrawArrays(GL_LINE_STRIP, 0, int(len(self.vertices)/3))
        glDisableVertexAttribArray(0)

        # rendering the xlines
        if self.rotation != 'Pio è un figo':
            glBindVertexArray(self.xpatharray)
            glUseProgram(self.xpath_shader)
            modelLocation = glGetUniformLocation(self.xpath_shader, 'model')
            viewLocation = glGetUniformLocation(self.xpath_shader, 'view')
            projectionLocation = glGetUniformLocation(self.xpath_shader, 'projection')
            glUniformMatrix4fv(modelLocation, 1, GL_TRUE, model)
            glUniformMatrix4fv(viewLocation, 1, GL_TRUE, view)
            glUniformMatrix4fv(projectionLocation, 1, GL_FALSE, proj)
            glEnableVertexAttribArray(0)
            glDrawArrays(GL_LINES, 0, int(len(self.xvertices)/3))
            glDisableVertexAttribArray(0)

            # rendering the ylines
            glBindVertexArray(self.ypatharray)
            glUseProgram(self.ypath_shader)
            modelLocation = glGetUniformLocation(self.ypath_shader, 'model')
            viewLocation = glGetUniformLocation(self.ypath_shader, 'view')
            projectionLocation = glGetUniformLocation(self.ypath_shader, 'projection')
            glUniformMatrix4fv(modelLocation, 1, GL_TRUE, model)
            glUniformMatrix4fv(viewLocation, 1, GL_TRUE, view)
            glUniformMatrix4fv(projectionLocation, 1, GL_FALSE, proj)
            glEnableVertexAttribArray(0)
            glDrawArrays(GL_LINES, 0, int(len(self.xvertices)/3))
            glDisableVertexAttribArray(0)

            # rendering the zlines
            glBindVertexArray(self.zpatharray)
            glUseProgram(self.zpath_shader)
            modelLocation = glGetUniformLocation(self.zpath_shader, 'model')
            viewLocation = glGetUniformLocation(self.zpath_shader, 'view')
            projectionLocation = glGetUniformLocation(self.zpath_shader, 'projection')
            glUniformMatrix4fv(modelLocation, 1, GL_TRUE, model)
            glUniformMatrix4fv(viewLocation, 1, GL_TRUE, view)
            glUniformMatrix4fv(projectionLocation, 1, GL_FALSE, proj)
            glEnableVertexAttribArray(0)
            glDrawArrays(GL_LINES, 0, int(len(self.xvertices)/3))
            glDisableVertexAttribArray(0)
        
