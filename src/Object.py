import pygame
import numpy as np
from ctypes import c_void_p

from .Shader import Shader
from .Script import Script
from .transforms import *

from OpenGL.GL import *

class Object:

    # attribs syntax : [ [size, stride, pointer_offset] ... ]
    # model data syntax: [x, y, z, rx, ry, rz, sx, sy, sz]
    def __init__(self, verteces, tris, vertex_path, frag_path, attribs, modeldata, scripts=[]):
        # stores the informations
        self.shader = Shader(vertex_path, frag_path).shaderProgram
        self.vertices = verteces
        self.tris = tris
        self.modeldata = modeldata
        self.attribs = attribs
        self.scripts = scripts

        # loads on gpu
        self.vertexArray = glGenVertexArrays(1)
        glBindVertexArray(self.vertexArray)

        self.triangleBuffer = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.triangleBuffer)
        glBufferData(GL_ARRAY_BUFFER, np.array(self.vertices, dtype='float32'), GL_STATIC_DRAW)
        for x in range(len(attribs)):
            glVertexAttribPointer(x, attribs[x][0], GL_FLOAT, GL_FALSE, attribs[x][1], attribs[x][2])

        self.indicesBuffer = glGenBuffers(1)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.indicesBuffer)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, np.array(tris, dtype='uint32'), GL_STATIC_DRAW)

        for s in scripts:
            assert isinstance(s, Script)
            s.object = self
            if s.startScript:
                s.startScript()

    def loadScript(self, script):
        script.object = self
        self.scripts.append(script)

    def loadTexture(self, texture_path):
        glBindVertexArray(self.vertexArray)
        self.texture = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, self.texture)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)	
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        textureSurface = pygame.image.load(texture_path)
        textureData = pygame.image.tostring(textureSurface, "RGBA", 1)
        width = textureSurface.get_width()
        height = textureSurface.get_height()
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, textureData)

    def scriptUpdate(self):
        for s in self.scripts:
            if s.updateScript:
                s.updateScript()

    def renderObject(self, camera):
        glUseProgram(self.shader)
        glBindVertexArray(self.vertexArray)
        glBindBuffer(GL_ARRAY_BUFFER, self.triangleBuffer)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.indicesBuffer)

        rotMatrix = np.dot( get_rot(self.modeldata[3], 0), get_rot(self.modeldata[4], 1))
        rotMatrix = np.dot(rotMatrix, get_rot(self.modeldata[5], 2))
        model = np.dot(get_traslation(self.modeldata[0],self.modeldata[1], self.modeldata[2]), rotMatrix)
        scale_matrix = get_scale(self.modeldata[6], self.modeldata[7], self.modeldata[8])
        view = camera.view
        proj = camera.proj
        modelLocation = glGetUniformLocation(self.shader, 'model')
        viewLocation = glGetUniformLocation(self.shader, 'view')
        projectionLocation = glGetUniformLocation(self.shader, 'projection')
        scaleLocation = glGetUniformLocation(self.shader, 'scale')
        glUniformMatrix4fv(modelLocation, 1, GL_TRUE, model)
        glUniformMatrix4fv(viewLocation, 1, GL_TRUE, view)
        glUniformMatrix4fv(projectionLocation, 1, GL_FALSE, proj)
        glUniformMatrix4fv(scaleLocation, 1, GL_FALSE, scale_matrix)

        for x in range(len(self.attribs)):
            glEnableVertexAttribArray(x)
        glDrawElements(GL_TRIANGLES, len(self.tris), GL_UNSIGNED_INT, None)
        for x in range(len(self.attribs)):
            glDisableVertexAttribArray(x)


        