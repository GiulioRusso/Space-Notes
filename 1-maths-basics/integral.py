import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import matplotlib.patches as patches

def f(x):
    return -(x - 5)**2 + 20

def riemann_sum(n):
    a, b = 0, 10
    dx = (b - a) / n
    x_vals = np.linspace(a, b, n + 1)
    y_vals = f(x_vals)

    integral_sum = 0
    for i in range(n):
        integral_sum += dx * y_vals[i]

    return integral_sum

# Create the plot
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)  # Adjust the plot area to accommodate the slider

# Plot the concave down curve
x_vals = np.linspace(0, 10, 1000)
y_vals = f(x_vals)
ax.plot(x_vals, y_vals, label='Concave Down Curve', linewidth=2)

# Set plot labels and grid
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.grid(True)
ax.legend()

# Set the x and y axis limits
plt.xlim(0, 10)
plt.ylim(0, 25)

# Create a slider for controlling the number of rectangles
ax_slider = plt.axes([0.15, 0.1, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slider = Slider(ax_slider, 'Number of Rectangles', 1, 100, valinit=5, valstep=1)

# Function to update the plot when the slider value changes
def update(val):
    n = int(slider.val)
    integral_value = riemann_sum(n)
    ax.set_title(f"Integral Estimate = {integral_value:.2f}")

    # Clear previous rectangles
    for patch in ax.patches:
        patch.remove()

    # Draw rectangles
    a, b = 0, 10
    dx = (b - a) / n
    for i in range(n):
        rect = patches.Rectangle((a + i * dx, 0), dx, f(a + i * dx), linewidth=1, edgecolor='blue', facecolor='lightblue')
        ax.add_patch(rect)

    fig.canvas.draw_idle()

# Attach the update function to the slider
slider.on_changed(update)

plt.show()
