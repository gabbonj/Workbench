from OpenGL.GL import *

class Shader:

    def __init__(self, vertpath, fragpath):
        vertshader = self.loadShader(vertpath, GL_VERTEX_SHADER)
        fragshader = self.loadShader(fragpath, GL_FRAGMENT_SHADER)
        self.shaderProgram = glCreateProgram()
        glAttachShader(self.shaderProgram, vertshader)
        glAttachShader(self.shaderProgram, fragshader)
        glLinkProgram(self.shaderProgram)

    def loadShader(self, path, shadertype):
        shaderData = None
        f = open(path, 'r')
        shaderData = f.read()
        shader = glCreateShader(shadertype)
        glShaderSource(shader, shaderData)
        glCompileShader(shader)
        return shader
