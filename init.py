from src import *
from scripts import *



def startEngine():
    global context
    context = Context(1280, 720)
    context.initGrid(1000)

    #path_script = Script(context, start_script=load_path)
    #path_script.startScript()
    tex_script = Script(context, start_script=load_rotating_obj)
    tex_script.startScript()
        

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
