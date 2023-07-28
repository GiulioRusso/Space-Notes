import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

def update(val):
    m = slider_m.val
    b = slider_b.val
    f = m * x + b
    line.set_ydata(f)
    ax.set_title(f"Linear Function f(x) = {m:.2f}x + {b:.2f}")
    fig.canvas.draw_idle()

# Create data for x values
x = np.arange(-5, 5, 0.1)

# Initial values of m and b
initial_m = 1
initial_b = 0

# Create the plot
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)  # Adjust the plot area to accommodate sliders

# Plot the initial linear function
line, = ax.plot(x, initial_m * x + initial_b, linewidth=2)

# Set plot labels and grid
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.grid(True)

# Create sliders
ax_m = plt.axes([0.1, 0.1, 0.65, 0.03], facecolor='lightgoldenrodyellow')
ax_b = plt.axes([0.1, 0.05, 0.65, 0.03], facecolor='lightgoldenrodyellow')

slider_m = Slider(ax_m, 'm', 0, 10, valinit=initial_m, valstep=0.1)
slider_b = Slider(ax_b, 'b', -4, 4, valinit=initial_b, valstep=0.1)

# Update the plot when sliders' values change
slider_m.on_changed(update)
slider_b.on_changed(update)

plt.show()
