from src import *

def startEngine():
    global context
    context = Context(1280, 720)
    context.initGrid(1000)

    pp, rr = [], []
    for x in range(1, 30, 1):
        pp.extend([np.sin(x) / 3 + x / 20 * 10, np.log(x) * 10, x / 10 * 10])
        rr.append([x /10, 2 * x /10, x /10])
    papthy = Path(pp, rr)
    context.addObject(papthy)
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
