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


def setup_opengl(): #Create a funtion to setup OpenGL

    # Set the current matrix mode to GL_PROJECTION
    glMatrixMode(GL_PROJECTION)
    
    # Load the identity matrix into the current matrix (initialize to identity)
    glLoadIdentity()
    
    # Define a 2D orthographic projection matrix
    # Parameters: left, right, bottom, top, near, far
    glOrtho(-4, 4, -3, 3, -1, 1)
    
    # Set the current matrix mode to GL_MODELVIEW
    glMatrixMode(GL_MODELVIEW)
    
    # Load the identity matrix into the current matrix (initialize to identity)
    glLoadIdentity()
    
    # Clear the color buffer with the specified clear color
    glClear(GL_COLOR_BUFFER_BIT)
