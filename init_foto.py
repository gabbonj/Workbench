from src import *
from scripts import *

if __name__ == "__main__":
    context = Context(1280, 720, eyeposition=[0, 0, 0])    
    context.loadObjFile('models\\plane.obj',
                        'src\shaders\default\defaultvert.glsl',
                        'src\shaders\default\defaultfrag.glsl',
                        [ [ 3, 5 * 4, c_void_p(0) ], [2, 5 * 4, c_void_p(3 * 4)] ],
                        [0, 0, 0, 0, 0, 0, 100, 100, 100],
                        texture = 'out.png')
    pp, rr = [], []
    for x in range(1, 30, 1):
        pp.extend([np.sin(x) / 3 + x / 20 * 10, np.log(x) * 10, x / 10 * 10])
        rr.append([x /10, 2 * x /10, x /10])
    papthy = Path(pp, rr)
    context.addObject(papthy)
    
    

    while True:
        context.update()