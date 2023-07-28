import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from matplotlib.patches import Arc

# Create data for the circumference
theta = np.linspace(0, 2 * np.pi, 1000)
x_circ = np.cos(theta)
y_circ = np.sin(theta)

# Create the plot
fig, (ax_left_rad, ax_left_deg, ax_right) = plt.subplots(1, 3, figsize=(16, 6), gridspec_kw={'width_ratios': [1, 1, 2]})
plt.subplots_adjust(bottom=0.2)  # Adjust the plot area to accommodate sliders

# Plot the circumference on the right side
circ_line, = ax_right.plot(x_circ, y_circ, 'g-', label='Circumference')
red_dot, = ax_right.plot(1, 0, 'ro')  # Red dot at the end of radius
radius_line, = ax_right.plot([0, 1], [0, 0], 'gray', label='Radius')
ax_right.set_xlabel('x')
ax_right.set_ylabel('y')
ax_right.set_title('Circumference')
ax_right.grid(True)
ax_right.set_aspect('equal')

# Function to update the plot when the slider value changes
def update(val):
    angle_degrees = slider_angle.val
    angle_radians = np.radians(angle_degrees)

    # Update the red dot representing the angle on the right side
    red_dot.set_xdata(np.cos(angle_radians))
    red_dot.set_ydata(np.sin(angle_radians))

    # Update the radius of the circumference (color: gray)
    radius_line.set_xdata([0, np.cos(angle_radians)])
    radius_line.set_ydata([0, np.sin(angle_radians)])

    # Update the arch of the angle on the circumference (using Arc)
    arc_angle_a = Arc((0, 0), width=0.6, height=0.6, angle=0, theta1=0, theta2=angle_degrees, color='gray', linestyle='dashed', fill=False)
    if len(ax_right.patches) > 0:
        ax_right.patches[0].remove()  # Remove the previous Arc
    ax_right.add_patch(arc_angle_a)

    # Update the red dot on the left plots
    red_dot_rad.set_xdata(angle_radians)
    red_dot_deg.set_xdata(angle_degrees)

    # Update the titles of the left plots
    ax_left_rad.set_title(f'Angle in Radians: {angle_radians:.2f}')
    ax_left_deg.set_title(f'Angle in Degrees: {angle_degrees:.2f}')

    fig.canvas.draw_idle()

# Create the slider for controlling the angle
ax_slider = plt.axes([0.15, 0.03, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slider_angle = Slider(ax_slider, 'Angle (degrees)', 0, 360, valinit=0)

# Attach the update function to the slider
slider_angle.on_changed(update)

# Set plot limits for the right side
ax_right.set_xlim(-1.2, 1.2)
ax_right.set_ylim(-1.2, 1.2)

# Create data for x values in radians
x_radians = np.linspace(0, 2 * np.pi, 1000)

# Plot the axes on the left side for radians
ax_left_rad.plot(x_radians, np.zeros_like(x_radians), 'b-')  # x-axis in radians
red_dot_rad, = ax_left_rad.plot(0, 0, 'ro')  # Red dot at specified angle in radians
ax_left_rad.set_xlabel('Radians')
ax_left_rad.set_title('Angle in Radians')
ax_left_rad.grid(True)

# Create data for x values in degrees
x_degrees = np.linspace(0, 360, 1000)

# Plot the axes on the left side for degrees
ax_left_deg.plot(x_degrees, np.zeros_like(x_degrees), 'g-')  # x-axis in degrees
red_dot_deg, = ax_left_deg.plot(0, 0, 'ro')  # Red dot at specified angle in degrees
ax_left_deg.set_xlabel('Degrees')
ax_left_deg.set_title('Angle in Degrees')
ax_left_deg.grid(True)

# Set plot limits for the left side
ax_left_rad.set_xlim(0, 2 * np.pi)
ax_left_rad.set_ylim(-1, 1)

ax_left_deg.set_xlim(0, 360)
ax_left_deg.set_ylim(-1, 1)

plt.show()
