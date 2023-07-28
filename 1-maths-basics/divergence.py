import numpy as np
import matplotlib.pyplot as plt

def vector_field(x, y):
    return np.array([x, y])

def divergence(x, y):
    return 1 + 1  # Since ∇ · F = ∂P/∂x + ∂Q/∂y, and P = x, Q = y in our case

# Create a grid of points in the x-y plane
x = np.linspace(-5, 5, 20)
y = np.linspace(-5, 5, 20)
X, Y = np.meshgrid(x, y)

# Calculate the vector field at each point in the grid
U, V = vector_field(X, Y)

# Calculate the divergence at each point in the grid
div = divergence(X, Y)

# Create a quiver plot to visualize the vector field
plt.figure(figsize=(8, 6))
quiver_plot = plt.quiver(X, Y, U, V, div, cmap='coolwarm')

def on_motion(event):
    if event.xdata is not None and event.ydata is not None:
        x, y = event.xdata, event.ydata
        div_value = divergence(x, y)
        plt.title(f'Vector Field and Divergence: Divergence at ({x:.2f}, {y:.2f}): {div_value:.2f}')
        plt.draw()

# Connect the motion event to the function
plt.connect('motion_notify_event', on_motion)

# Set plot limits and labels
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Vector Field and Divergence')

# Show the plot
plt.show()
