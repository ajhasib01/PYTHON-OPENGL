import glfw
from OpenGL.GL import *
import math

# Function to set up the GLFW window
def window_setup():
    # Initialize GLFW
    if not glfw.init():
        return None
    
    # Set window resizable
    glfw.window_hint(glfw.RESIZABLE, glfw.TRUE)
    
    # Create a window
    window = glfw.create_window(800, 600, "RECTANGLE WITH LINE AND CIRCLE", None, None)
    if not window:
        glfw.terminate()
        return None
    
    # Make the window's context current
    glfw.make_context_current(window)
    return window

# Function to set up OpenGL
def setup_opengl():
    # Set the projection matrix
    glMatrixMode(GL_PROJECTION)
     # Load the identity matrix into the current matrix (initialize to identity)
    glLoadIdentity()
    # Define a 2D orthographic projection matrix
    # Parameters: left, right, bottom, top, near, far
    glOrtho(-12, 12, -6, 6, -6, 6)
    
    # Set the modelview matrix
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
    # Clear the temporary color buffer
    glClear(GL_COLOR_BUFFER_BIT)
    
    # Set line width for better visibility
    glLineWidth(4.0)

# Function to draw a rectangle
def Rectangle(x1, y1, x2, y2, x3, y3, x4, y4):
    glBegin(GL_QUADS)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glVertex2f(x3, y3)
    glVertex2f(x4, y4)
    glEnd()

# Function to draw a line parallel to X-axis
def Rec_X_line(x1, x2, x3, x4):
    glBegin(GL_LINES)
    glColor3f(0.0, 0.0, 0.0)  # Set color to black
    glVertex2f(x1, x2)
    glVertex2f(x3, x4)
    glEnd()

# Function to draw a line parallel to Y-axis
def Rec_Y_line(y1, y2, y3, y4):
    glBegin(GL_LINES)
    glColor3f(0.0, 0.0, 0.0)  # Set color to black
    glVertex2f(y1, y2)
    glVertex2f(y3, y4)
    glEnd()

# Function to draw colored lines
def Rec_color_Lines(x1, y1, x2, y2, x3, y3, x4, y4):
    glBegin(GL_LINES)
    # Green lines
    glColor3f(0.0, 1.0, 0.0)  # Set color to green
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)

    # Blue lines
    glColor3f(0.0, 0.0, 1.0)  # Set color to blue
    glVertex2f(x3, y3)
    glVertex2f(x4, y4)
    glEnd()

# Function to draw arrowheads
def Rec_arrows(x1, y1, x2, y2, x3, y3):
    glBegin(GL_TRIANGLES)
    glColor3f(0.0, 0.0, 0.0)  # Set color to black
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glVertex2f(x3, y3)
    glEnd()

# Function to draw a circle
def draw_circle(center_x, center_y, radius, num_segments):
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(center_x, center_y)  # Center of the circle
    for i in range(num_segments + 1):
        angle = 2 * math.pi * i / num_segments
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        glVertex2f(x, y)
    glEnd()

# Main function
def main():
    # Set up the window
    window = window_setup()
    if not window:
        return

    while not glfw.window_should_close(window):
        # Set up OpenGL
        setup_opengl()
        width, height = glfw.get_framebuffer_size(window)
        glViewport(0, 0, width, height)

        # Draw the first rectangle with associated lines and circle
        glColor3f(1.0, 1.0, 1.0)  # Set color to white
        Rectangle(-8, 1, -4, 1, -4, -1, -8, -1)
        Rec_X_line(-4, 0, -8, 0)
        Rec_Y_line(-6, 1, -6, -1)
        Rec_color_Lines(-7.7, 1, -4, -0.2, -6.3, 1, -4, -0.65)
        Rec_arrows(-3.96, 0, -4.2, 0.1, -4.2, -0.1)
        Rec_arrows(-6, 1.04, -5.9, 0.8, -6.1, 0.8)
        glColor3f(1.0, 0.0, 0.0)  # Set color to red
        draw_circle(-5.1, 0.17, 0.08, 100)

        # Draw the second rectangle with associated lines and circle
        glColor3f(0.0, 1.0, 1.0)  # Set color to cyan
        Rectangle(2, 1, -2, 1, -2, -1, 2, -1)
        Rec_X_line(2, 0, -2, 0)
        Rec_Y_line(0, 1, 0, -1)
        Rec_color_Lines(-2, 0.8, 2, -0.1, -0.2, 1, 2, -0.4)
        Rec_arrows(0, 1.04, 0.1, 0.8, -0.1, 0.8)
        Rec_arrows(2.04, 0, 1.8, -0.1, 1.8, 0.1)
        glColor3f(1.0, 0.0, 0.0)  # Set color to red
        draw_circle(1.3, 0.08, 0.08, 100)

        # Draw the third rectangle with associated lines and circle
        glColor3f(1.0, 1.0, 0.0)  # Set color to yellow
        Rectangle(8, 1, 4, 1, 4, -1, 8, -1)
        Rec_X_line(4, 0, 8, 0)
        Rec_Y_line(6, 1, 6, -1)
        Rec_color_Lines(4, 0.4, 8, 0.4, 4, 0.6, 8, 0.6)
        Rec_arrows(8.04, 0, 7.8, 0.1, 7.8, -0.1)
        Rec_arrows(6, 1.04, 5.9, 0.8, 6.1, 0.8)

        # Swap buffers and poll events
        glfw.swap_buffers(window)
        glfw.poll_events()

    # Terminate GLFW
    glfw.terminate()

if __name__ == "__main__":
    main()
