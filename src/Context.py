import time 
import pygame
import numpy as np
from pygame.locals import *

from .Shader import Shader
from .Camera import Camera
from .Object import Object
from .transforms import *
from .Path import Path

from OpenGL.GL import *


class Context:

    def __init__(self, height, width, eyeposition=[1.0, 1.0, 1.0], objects=[], first_person=True):
        self.first_person = first_person
        self.display = (height, width)
        self.centre = (self.display[0]/2, self.display[1]/2)
        for obj in objects:
            assert isinstance(obj, Object) 
        self.objects = objects
        # Pygame init
        pygame.init()
        pygame.display.set_mode(self.display, DOUBLEBUF|OPENGL)
        pygame.mouse.set_pos(self.centre)
        pygame.mouse.set_visible(not self.first_person)

        # OpenglProcess
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_CULL_FACE)
        glCullFace(GL_FRONT)
        glFrontFace(GL_CW);
        glPointSize(5)
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
        self.grid = {
            'render' : False,
            'gridArrayObject' : glGenVertexArrays(1),
            'gridVertexArray' : glGenBuffers(1),
            'vertpath' : 'src\shaders\grid\gridvert.glsl',
            'fragpath' :'src\shaders\grid\gridfrag.glsl',
            'gridprogram' : None,
            'size' : 0
        }

        eyeposition = np.array(eyeposition)
        eyefwd = np.array([0, 0, 1])
        self.camera = Camera(self.display, eyeposition, eyefwd, .1, 300)

    def addObject(self, objectt):
        self.objects.append(objectt)

    def loadObjFile(self, obj_path, vertex_path, frag_path, attribs, modeldata, texture=None):
        f = open(obj_path, 'r')
        vertices_position = []
        vertices_texture = []
        indices = []
        for line in f.readlines():
            if line[:2] == 'v ':
                vertices_position.extend(line[2:-1].split(' '))
            if line[:2] == 'f ':
                vs = line[2:-1].split(' ')
                if len(vs) == 3:
                    for face in vs:
                        indices.append(face.split('/')[0])
                elif len(vs) == 4:
                    ii = [face.split('/')[0] for face in vs]
                    indices.extend([ii[0], ii[1], ii[3], ii[3], ii[1], ii[2]])
            if line[:3] == 'vt ':
                vertices_texture.extend(line[3:-1].split(' '))

        vertices = []
        for v in range(int(len(vertices_position)/3)):
            for x in range(3):
                vertices.append(vertices_position[v*3+x])
            try:    
                for x in range(2):
                    vertices.append(vertices_texture[v*2+x])
            except:
                vertices.extend([0, 0])

        for x in range(len(indices)):
            indices[x] = int(indices[x]) -1
        
        imported = Object(vertices, indices, vertex_path, frag_path, attribs, modeldata)
        imported.loadTexture(texture)
        self.addObject(imported)

    def initGrid(self, size):
        # generate lines
        self.grid['render'] = True
        lines = []
        
        for x in range(0, size + 1, 3):
            upvertex = [x - size/2, 0, size - size/2]
            lines.extend(upvertex)
            downvertex = [x - size/2, 0, 0 - size/2]
            lines.extend(downvertex)
            leftvertex = [size - size/2, 0, x - size/2]
            lines.extend(leftvertex)
            rightvertex = [0 - size/2, 0, x- size/2]
            lines.extend(rightvertex)



        self.grid['size'] = len(lines)
        lines = np.array(lines, dtype='float32')
        
        # load buffer on gpu
        glBindVertexArray(self.grid['gridArrayObject'])
        glBindBuffer(GL_ARRAY_BUFFER, self.grid['gridVertexArray'])
        glBufferData(GL_ARRAY_BUFFER, lines, GL_STATIC_DRAW)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * 4, None)

        # generate shader
        gridshader = Shader(self.grid['vertpath'], self.grid['fragpath'])
        self.grid['gridprogram'] = gridshader.shaderProgram

    def renderGrid(self):
        glBindVertexArray(self.grid['gridArrayObject'])
        glBindBuffer(GL_ARRAY_BUFFER, self.grid['gridVertexArray'])

        model = np.identity(4, dtype='float32')
        view = self.camera.view
        proj = self.camera.proj
        glUseProgram(self.grid['gridprogram'])
        modelLocation = glGetUniformLocation(self.grid['gridprogram'], 'model')
        viewLocation = glGetUniformLocation(self.grid['gridprogram'], 'view')
        projectionLocation = glGetUniformLocation(self.grid['gridprogram'], 'projection')
        glUniformMatrix4fv(modelLocation, 1, GL_TRUE, model)
        glUniformMatrix4fv(viewLocation, 1, GL_TRUE, view)
        glUniformMatrix4fv(projectionLocation, 1, GL_FALSE, proj)
        
        glEnableVertexAttribArray(0)
        glDrawArrays(GL_LINES, 0, self.grid['size']-1)
        glDisableVertexAttribArray(0)

    def renderObjects(self):
        for obj in self.objects:
            if isinstance(obj, Object):
                obj.renderObject(self.camera)
            elif isinstance(obj, Path):
                obj.renderPath(self.camera)


    def update(self):
        t = time.time()
        # Opengl update
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        if self.grid['render']:
            self.renderGrid()
        self.renderObjects()
        dt = time.time() - t

        ## draw the scen
        # Pygame update
        newpos = np.array(self.camera.position)
        newpitch = self.camera.pitch
        newyaw = self.camera.yaw

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYUP:
                if event.key==K_LESS:
                    self.first_person = not self.first_person
                    pygame.mouse.set_visible(not self.first_person)
            if event.type == pygame.MOUSEMOTION and self.first_person:
                mouse_position = pygame.mouse.get_pos()
                dx, dy = (0, 0)
                dx = mouse_position[0] - self.centre[0]
                dy = mouse_position[1] - self.centre[1]
                if (dx, dy) != 0:
                    newpitch -= dy * self.camera.sensitivity
                    newyaw +=  dx * self.camera.sensitivity
                    self.camera.roateCamera(newpitch, newyaw)
                pygame.mouse.set_pos(self.centre)


        keys = pygame.key.get_pressed()

        if self.first_person:
            if keys[pygame.K_w]:
                newpos += self.camera.speed * self.camera.forward
            if keys[pygame.K_s]:
                newpos -= self.camera.speed * self.camera.forward
            if keys[pygame.K_a]:
                newpos -= normalize(np.cross(self.camera.forward, self.camera.up)) * self.camera.speed
            if keys[pygame.K_d]:
                newpos += normalize(np.cross(self.camera.forward, self.camera.up)) * self.camera.speed
            if keys[pygame.K_LSHIFT]:
                newpos[1] += self.camera.speed
            if keys[pygame.K_LCTRL]:
                newpos[1] -= self.camera.speed
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            quit()

        self.camera.setCameraPosition(newpos)
        
        pygame.display.flip()
        pygame.time.wait(10)
            