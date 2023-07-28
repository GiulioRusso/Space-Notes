import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

def f(x):
    return np.sin(x)  # Define your function here

def derivative(x, h):
    if h == 0:
        return np.cos(x)
    else:
        return (f(x + h) - f(x)) / h

def tangent_line(x):
    return np.cos(x) * (x_vals - x) + f(x)

def update(val):
    x = slider_x.val
    h = slider_h.val
    slope = derivative(x, h)

    line.set_ydata(f(x_vals))
    point_x.set_data(x, f(x))
    point_x_plus_h.set_data(x + h, f(x + h))

    # Compute the tangent line using the derivative at x when h is 0
    tangent_y_vals = tangent_line(x) if h == 0 else f(x) + slope * (x_vals - x)
    tangent_line_plot.set_data(x_vals, tangent_y_vals)

    # Update the title based on h value
    if h == 0:
        ax.set_title(f"Sine Function: x = {x:.2f}, Derivative = {slope:.2f}")
    else:
        ax.set_title(f"Sine Function: x = {x:.2f}")

    fig.canvas.draw_idle()

# Create data for x values
x_vals = np.linspace(0, 2 * np.pi, 1000)

# Create the plot
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)  # Adjust the plot area to accommodate sliders

# Plot the sine function
line, = ax.plot(x_vals, f(x_vals), label='Sine Function')
point_x, = ax.plot(0, 0, 'ro', label='f(x)')
point_x_plus_h, = ax.plot(0, 0, 'bo', label="f(x + h)")
tangent_line_plot, = ax.plot([], [], 'g--', label='Tangent Line')

# Set plot labels and grid
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.grid(True)
ax.legend()

# Set the x and y axis limits
plt.xlim(0, 2 * np.pi)
plt.ylim(-1.5, 1.5)

# Create sliders for controlling the x-coordinate of the point and the h distance
ax_slider_x = plt.axes([0.15, 0.1, 0.65, 0.03], facecolor='lightgoldenrodyellow')
ax_slider_h = plt.axes([0.15, 0.05, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slider_x = Slider(ax_slider_x, 'x-coordinate', 0, 2 * np.pi, valinit=0)
slider_h = Slider(ax_slider_h, 'h', -1, 1, valinit=0)

# Update the plot when the slider values change
slider_x.on_changed(update)
slider_h.on_changed(update)

plt.show()
