import glfw
from OpenGL.GL import *


def window_setup(): # Create a Function Called Window Setup.

    if not glfw.init():  # If Graphics Library Framework is not initialized, it will return None.
        return None 
    
    glfw.window_hint(glfw.RESIZABLE, glfw.TRUE)  # This function allows the window size to be resizable.

    window = glfw.create_window(800, 600, "TRIANGLE", None, None)  # Create the window with the specified width, height, and title.

    # If the window creation fails, it will return None.
    if not window:
        glfw.terminate()
        return None

    # Make this window the current context.
    glfw.make_context_current(window)