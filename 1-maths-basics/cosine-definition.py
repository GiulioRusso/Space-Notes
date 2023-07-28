import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from matplotlib.patches import Arc

# Create data for the cosine function
x_cosine = np.linspace(0, 2 * np.pi, 1000)
y_cosine = np.cos(x_cosine)

# Create data for the circumference
theta = np.linspace(0, 2 * np.pi, 1000)
x_circ = np.cos(theta)
y_circ = np.sin(theta)

# Create the plot
fig, (ax_cosine, ax_circ) = plt.subplots(1, 2, figsize=(10, 5))

# Plot the cosine function on the left side
cosine_line, = ax_cosine.plot(x_cosine, y_cosine, 'b-', label='cos(x)')
point_cosine, = ax_cosine.plot(0, 1, 'ro')  # Start the red dot at (0, 1) for the cosine function
proj_line_cosine, = ax_cosine.plot([0, 0], [0, 1], 'r--', label='Projection')  # Vertical line from the x-axis to the red dot for the cosine projection
ax_cosine.set_xlabel('x')
ax_cosine.set_ylabel('cos(x)')
ax_cosine.set_title(f'Cosine Function (cos(x) = {np.cos(0):.2f})')
ax_cosine.grid(True)

# Plot the circumference on the right side
circ_line, = ax_circ.plot(x_circ, y_circ, 'g-', label='Circumference')
point_circ, = ax_circ.plot(1, 0, 'ro')
proj_line_circ, = ax_circ.plot([0, 1], [0, 0], 'r--', label='Projection')  # Horizontal line from the origin to the red dot for the cosine projection on the circumference
radius_line_circ, = ax_circ.plot([0, 0], [0, 0], 'gray', label='Radius')
ax_circ.set_xlabel('x')
ax_circ.set_ylabel('y')
ax_circ.set_title('Circumference')
ax_circ.grid(True)

# Set aspect ratio to equal for the circumference
ax_circ.set_aspect('equal')

# Create the slider for controlling the angle
ax_slider = plt.axes([0.15, 0.03, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slider_angle = Slider(ax_slider, 'Angle (degrees)', 0, 360, valinit=0)

# Function to update the plot when the slider value changes
def update(val):
    angle_degrees = slider_angle.val
    angle_radians = np.radians(angle_degrees)

    # Update the cosine function plot
    point_cosine.set_xdata(angle_radians)
    point_cosine.set_ydata(np.cos(angle_radians))
    ax_cosine.set_title(f'Cosine Function (cos(x) = {np.cos(angle_radians):.2f})')

    # Update the cosine projection on the cosine plot (vertical line)
    proj_line_cosine.set_xdata([angle_radians, angle_radians])
    proj_line_cosine.set_ydata([0, np.cos(angle_radians)])

    # Update the circumference plot
    point_circ.set_xdata(np.cos(angle_radians))
    point_circ.set_ydata(np.sin(angle_radians))
    
    # Calculate the cosine projection on the circumference (horizontal line from the origin to the x-coordinate of the red dot)
    proj_line_circ.set_xdata([0, np.cos(angle_radians)])
    proj_line_circ.set_ydata([0, 0])  # Set y-coordinate to 0

    # Update the radius of the circumference (color: gray)
    radius_line_circ.set_xdata([0, np.cos(angle_radians)])
    radius_line_circ.set_ydata([0, np.sin(angle_radians)])

    # Update the arch of the angle on the circumference (using Arc)
    arc_angle_a = Arc((0, 0), width=0.6, height=0.6, angle=0, theta1=0, theta2=angle_degrees, color='gray', linestyle='dashed', fill=False)
    if len(ax_circ.patches) > 0:
        ax_circ.patches[0].remove()  # Remove the previous Arc
    ax_circ.add_patch(arc_angle_a)

    fig.canvas.draw_idle()

# Attach the update function to the slider
slider_angle.on_changed(update)

# Set plot limits for the slider
ax_slider.set_xlim(0, 360)

plt.show()
