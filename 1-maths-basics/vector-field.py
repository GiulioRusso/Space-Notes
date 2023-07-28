import numpy as np
import matplotlib.pyplot as plt

# Define the vector field F = (P, Q)
def vector_field(x, y):
    P = -y
    Q = x
    return P, Q

# Create a grid of points in the x-y plane
x = np.linspace(-2, 2, 10)
y = np.linspace(-2, 2, 10)
X, Y = np.meshgrid(x, y)

# Calculate the vector field values at each point in the grid
U, V = vector_field(X, Y)

# Create a quiver plot to visualize the vector field
plt.figure(figsize=(8, 6))
plt.quiver(X, Y, U, V, angles='xy', scale_units='xy', scale=1, color='b', label='Vector Field')

# Set labels and title for the plot
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Vector Field Visualization')

# Add a legend to identify the vectors
plt.legend()

# Show the plot
plt.grid()
plt.show()
