import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

def update(val):
    a = slider_a.val
    b = slider_b.val
    c = slider_c.val
    f = a * x**2 + b * x + c
    line.set_ydata(f)
    ax.set_title(f"Quadratic Function f(x) = {a:.2f}x^2 + {b:.2f}x + {c:.2f}")
    fig.canvas.draw_idle()

# Create data for x values
x = np.arange(-5, 5, 0.1)

# Initial values of a, b, and c
initial_a = 1
initial_b = 0
initial_c = 0

# Create the plot
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)  # Adjust the plot area to accommodate sliders

# Plot the initial quadratic function
line, = ax.plot(x, initial_a * x**2 + initial_b * x + initial_c, linewidth=2)

# Set plot labels and grid
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.grid(True)

# Set the x and y axis limits
plt.xlim(-5, 5)
plt.ylim(-10, 10)

# Create sliders
ax_a = plt.axes([0.1, 0.1, 0.65, 0.03], facecolor='lightgoldenrodyellow')
ax_b = plt.axes([0.1, 0.05, 0.65, 0.03], facecolor='lightgoldenrodyellow')
ax_c = plt.axes([0.1, 0.15, 0.65, 0.03], facecolor='lightgoldenrodyellow')

slider_a = Slider(ax_a, 'a', -10, 10, valinit=initial_a, valstep=0.1)
slider_b = Slider(ax_b, 'b', -10, 10, valinit=initial_b, valstep=0.1)
slider_c = Slider(ax_c, 'c', -10, 10, valinit=initial_c, valstep=0.1)

# Update the plot when sliders' values change
slider_a.on_changed(update)
slider_b.on_changed(update)
slider_c.on_changed(update)

plt.show()
