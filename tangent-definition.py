import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from matplotlib.patches import Arc

# Create data for the tangent function
x_tangent = np.linspace(0, 2 * np.pi, 1000)
y_tangent = np.tan(x_tangent)

# Create data for the circumference
theta = np.linspace(0, 2 * np.pi, 1000)
x_circ = np.cos(theta)
y_circ = np.sin(theta)

# Create the plot
fig, (ax_tangent, ax_circ) = plt.subplots(1, 2, figsize=(10, 5))

# Plot the tangent function on the left side
tangent_line, = ax_tangent.plot(x_tangent, y_tangent, 'b-', label='tan(x)')
point_tangent, = ax_tangent.plot(0, 0, 'ro')
proj_line_tangent, = ax_tangent.plot([0, 0], [0, 0], 'r--', label='Projection')
ax_tangent.set_xlabel('x')
ax_tangent.set_ylabel('tan(x)')
ax_tangent.set_title(f'Tangent Function (tan(x) = {np.tan(0):.2f})')
ax_tangent.grid(True)
ax_tangent.set_ylim(-5, 5)  # Limit the y-axis for the left plot

# Plot the circumference on the right side
circ_line, = ax_circ.plot(x_circ, y_circ, 'g-', label='Circumference')
point_circ, = ax_circ.plot(1, 0, 'ro')
proj_line_circ, = ax_circ.plot([0, 0], [0, 0], 'r--', label='Projection')
radius_line_circ, = ax_circ.plot([0, 0], [0, 0], 'gray', label='Radius')
extra_red_dot, = ax_circ.plot(0, 0, 'ro')  # Red dot at the end of extended radius
extra_gray_line, = ax_circ.plot([0, 0], [0, 0], 'gray', linestyle='dashed')  # Additional gray line
ax_circ.set_xlabel('x')
ax_circ.set_ylabel('y')
ax_circ.set_title('Circumference')
ax_circ.grid(True)
ax_circ.set_xlim(-5, 5)  # Limit the x-axis for the right plot
ax_circ.set_ylim(-5, 5)  # Limit the y-axis for the right plot
ax_circ.set_aspect('equal')

# Create the slider for controlling the angle
ax_slider = plt.axes([0.15, 0.03, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slider_angle = Slider(ax_slider, 'Angle (degrees)', 0, 360, valinit=0)

# Function to update the plot when the slider value changes
def update(val):
    angle_degrees = slider_angle.val
    angle_radians = np.radians(angle_degrees)

    # Update the tangent function plot
    point_tangent.set_xdata(angle_radians)
    point_tangent.set_ydata(np.tan(angle_radians))
    ax_tangent.set_title(f'Tangent Function (tan(x) = {np.tan(angle_radians):.2f})')

    # Update the tangent projection on the left plot
    proj_line_tangent.set_xdata([angle_radians, angle_radians])
    proj_line_tangent.set_ydata([0, np.tan(angle_radians)])

    # Update the circumference plot
    point_circ.set_xdata(np.cos(angle_radians))
    point_circ.set_ydata(np.sin(angle_radians))

    # Update the projection on the right plot
    proj_line_circ.set_xdata([1, 1])
    proj_line_circ.set_ydata([0, np.tan(angle_radians)])

    # Update the radius of the circumference (color: gray)
    radius_line_circ.set_xdata([0, np.cos(angle_radians)])
    radius_line_circ.set_ydata([0, np.sin(angle_radians)])

    # Calculate the y-coordinate of the red dot over the circumference
    y_circ_red_dot = np.tan(angle_radians)

    # Update the extra red dot at the end of the extended radius
    extra_red_dot.set_xdata([1])
    extra_red_dot.set_ydata([y_circ_red_dot])

    # Update the additional gray line from (0,0) to the extra_red_dot
    extra_gray_line.set_xdata([0, 1])
    extra_gray_line.set_ydata([0, y_circ_red_dot])

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
