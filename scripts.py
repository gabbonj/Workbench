from src import *


###########################################################

def load_path(this):
    assert isinstance(this, Script)

    pp, rr = [], []
    for x in range(1, 30, 1):
        pp.extend([np.sin(x) / 3 + x / 20 * 10, np.log(x) * 10, x / 10 * 10])
        rr.append([x /10, 2 * x /10, x /10])
    papthy = Path(pp, rr)
    this.context.addObject(papthy)

###########################################################

def load_textured_obj(this):
    assert isinstance(this, Script)
    this.context.loadObjFile('models\\lucy.obj',
                             'src\shaders\default\defaultvert.glsl',
                             'src\shaders\default\defaultfrag.glsl',
                             [ [ 3, 5 * 4, c_void_p(0) ], [2, 5 * 4, c_void_p(3 * 4)] ],
                             [1, 1, 1, 0, 0, 0, 1, 1, 1],
                             texture = 'textures\\brick.jpg')

###########################################################

def rotate_s(this):
    assert isinstance(this, Script)
    this.object.modeldata[4] = this.context.time % 6.28


def load_rotating_obj(this):
    assert isinstance(this, Script)
    rotate_script = Script(this.context, update_script=rotate_s)
    this.context.loadObjFile('models\\lucy.obj',
                             'src\shaders\default\defaultvert.glsl',
                             'src\shaders\default\defaultfrag.glsl',
                             [ [ 3, 5 * 4, c_void_p(0) ], [2, 5 * 4, c_void_p(3 * 4)] ],
                             [1, 1, 1, 0, 0, 0, 1, 1, 1],
                             texture = 'textures\\brick.jpg',
                             scripts=[rotate_script])

###########################################################