# Workbench
Workbench is lightweight graphics engine written in Python with PyOpenGL

## Content:
- Get started
    - Install dependences
    - The init file
    - Commands
    - the GUI
- Classes
    - Context
    - Camera
    - Shader
    - Script
    - Object
    - Empty *(not implemented yet LMAO)*
    - Path
- Examples
    - Load an Object
    - Load a path

# Get started

## Install dependences
You can install all the dependences with the following command:  
```bash
pip install -r requirements.txt
```
Then the you have to run this command to start the engine:
```bash
python3 init.py
```

## The init file
The <font>init.py</font> file allows you to control the engine by adding objects to the context or loading scripts. In order to interact with the engine you have to write code in the **startEngine()** method that is structured in the following way:
```python
def startEngine():
    # Makes the context variable visible in the global scope
    global context
    context = Context(width, height) # Creating the context
    context.initGrid(size) # Creating the grid

    ...

    while True:

        ...

        context.update() # Updating the context
```
At first it creates a PyOpenGL context where is specified the width and height of the window and then creates a grid a specified size (this optional, but it helps to visualize the scene in an intuitive way).<br>
In the following space you have to write code to setup the engine for the actual use, here you can add objects to the context, load scripts and customize the engine settings.<br>
At the and end of the method the is a while loop everything that is written here will be called every frame.

You can also write your own startEngine() function and set it as the target of the *"engine_thread"* thread.

## Commands
The commands to navigate space in the engine are very simple, the **W/A/S/D** keys move the camera **forward/left/backwards/right** relative to its position, the **shift/ctrl** keys mone the camera **up/down** in the $Y$ direction. The camera orientation is controlled by mouse, unless you press the **<** key that toggles the *first person* control mode and so you can move freely the mouse acrooss the screen.