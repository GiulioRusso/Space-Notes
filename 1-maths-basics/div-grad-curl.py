import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Cursor

# Define the vector field F = (P, Q)
def vector_field(x, y):
    P = -y
    Q = x
    return P, Q

# Calculate the divergence of the vector field at point (x, y)
def divergence(x, y):
    # Placeholder calculation, replace with your formula
    return x + y

# Calculate the curl of the vector field at point (x, y)
def curl(x, y):
    # Placeholder calculation, replace with your formula
    return x - y

def onclick(event):
    if event.inaxes is not None:
        x, y = event.xdata, event.ydata
        div = divergence(x, y)
        c = curl(x, y)
        grad_P = 2*y  # Placeholder gradient calculation, replace with your formula
        grad_Q = 2*x  # Placeholder gradient calculation, replace with your formula
        print(f"Selected Point: ({x:.2f}, {y:.2f})")
        print(f"Divergence at ({x:.2f}, {y:.2f}): {div:.2f}")
        print(f"Curl at ({x:.2f}, {y:.2f}): {c:.2f}")
        print(f"Gradient at ({x:.2f}, {y:.2f}): ({grad_P:.2f}, {grad_Q:.2f})")
        plt.title(f'Divergence at ({x:.2f}, {y:.2f}): {div:.2f}')

        # Clear previous arrows
        if 'curl_arrow' in locals():
            curl_arrow.remove()
        if 'grad_arrow' in locals():
            grad_arrow.remove()

        # Draw the new curl vector and gradient vector
        curl_arrow = plt.quiver(x, y, c, 0, angles='xy', scale_units='xy', scale=1, color='r', label='Curl Vector', pivot='tail')
        grad_arrow = plt.quiver(x, y, grad_P, grad_Q, angles='xy', scale_units='xy', scale=1, color='g', label='Gradient Vector', pivot='tail')

        # Update the legend
        plt.legend([vector_plot, curl_arrow, grad_arrow], ['Vector Field', 'Curl Vector', 'Gradient Vector'])

        plt.draw()  # Redraw the plot to update the curl vector and gradient vector

# Create a grid of points in the x-y plane
x = np.linspace(-2, 2, 10)
y = np.linspace(-2, 2, 10)
X, Y = np.meshgrid(x, y)

# Calculate the vector field values at each point in the grid
U, V = vector_field(X, Y)

# Create a quiver plot to visualize the vector field
plt.figure(figsize=(8, 6))
vector_plot = plt.quiver(X, Y, U, V, angles='xy', scale_units='xy', scale=1, color='b', label='Vector Field')

# Set labels and title for the plot
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Vector Field Visualization')

# Add a legend to identify the vectors
plt.legend([vector_plot], ['Vector Field'])

# Add cursor to the plot
cursor = Cursor(plt.gca(), useblit=True, color='red', linewidth=1)

# Register the onclick event
plt.gcf().canvas.mpl_connect('button_press_event', onclick)

# Show the plot
plt.grid()
plt.show()
