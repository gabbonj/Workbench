from src import *
from scripts import *

def srt(this):
    assert isinstance(this, Script)
    this.object.modeldata[4] = this.context.time % 6.28

def startEngine():
    global context
    context = Context(1280, 720)
    context.initGrid(1000)

    path_script = Script(context, start_script=load_path)
    path_script.startScript()

    scri = Script(context)
    scri.loadScripts(lambda x : None, srt)

    context.loadObjFile('models\\lucy.obj',
                        'src\shaders\default\defaultvert.glsl',
                        'src\shaders\default\defaultfrag.glsl',
                        [ [ 3, 5 * 4, c_void_p(0) ], [2, 5 * 4, c_void_p(3 * 4)] ],
                        [1, 1, 1, 0, 0, 0],
                        texture = 'textures\\brick.jpg', 
                        scripts=[scri])

    while True:
        context.update()

def startGui():
    app = QtWidgets.QApplication(sys.argv)
    Worckbanch = QtWidgets.QMainWindow()
    ui = Ui_Worckbanch()
    ui.setupUi(Worckbanch)
    ui.connectUI(context)
    Worckbanch.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    engine_thread = t.Thread(name='engine', target=startEngine, daemon=True)
    engine_thread.start()
    time.sleep(1)
    
    startGui()
