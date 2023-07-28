import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from mpl_toolkits.mplot3d import Axes3D

# Define the scalar function f(x, y)
def scalar_function(x, y):
    return x**2 + y**2

# Calculate the gradient of the scalar function at point (x, y)
def gradient(x, y):
    df_dx = 2 * x
    df_dy = 2 * y
    return df_dx, df_dy

# Create a grid of points in the x-y plane
x = np.linspace(-4, 4, 100)
y = np.linspace(-4, 4, 100)
X, Y = np.meshgrid(x, y)

# Calculate the scalar function values at each point in the grid
Z = scalar_function(X, Y)

# Create a separate window for the 3D plot of the scalar function
fig_3d = plt.figure()
ax_3d = fig_3d.add_subplot(111, projection='3d')

# Plot the scalar function as a surface in 3D
surface_3d = ax_3d.plot_surface(X, Y, Z, cmap='viridis')

# Set labels and title for the 3D plot
ax_3d.set_xlabel('X')
ax_3d.set_ylabel('Y')
ax_3d.set_zlabel('Z')
ax_3d.set_title('Scalar Function in 3D')

# Show the 3D plot
plt.show()

# Create a plot for the scalar function (2D plot)
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)

# Plot the scalar function with a colorbar
contour = ax.contourf(X, Y, Z, cmap='viridis')
cbar = plt.colorbar(contour)

# Create sliders for controlling the x and y coordinates
ax_x = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor='lightgoldenrodyellow')
ax_y = plt.axes([0.25, 0.05, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slider_x = Slider(ax_x, 'X', -4, 4, valinit=0)
slider_y = Slider(ax_y, 'Y', -4, 4, valinit=0)

# Create a quiver plot to visualize the gradient vector
quiver_plot = ax.quiver([], [], [], [], color='red', scale=30)

def update(val):
    x = slider_x.val
    y = slider_y.val
    df_dx, df_dy = gradient(x, y)
    
    # Update the quiver plot
    quiver_plot.set_UVC(df_dx, df_dy)
    quiver_plot.set_offsets(np.array([[x, y]]))
    
    # Redraw the plot
    fig.canvas.draw_idle()

# Add an observer to the sliders
slider_x.on_changed(update)
slider_y.on_changed(update)

# Set labels and title for the 2D plot
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Scalar Function and Gradient')

# Show the 2D plot
plt.show()
