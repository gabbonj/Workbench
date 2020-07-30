from src import *

if __name__ == "__main__":

    context = Context(1280, 720)
    context.initGrid(1000)

    pp, rr = [], []
    for x in range(1, 30, 1):
        pp.extend([np.sin(x) / 3 + x / 20 * 10, np.log(x) * 10, x / 10 * 10])
        rr.append([x /100, 2 * x /100, x /100])
    papthy = Path(pp, rr)
    context.addObject(papthy)

    while True:
        context.update()