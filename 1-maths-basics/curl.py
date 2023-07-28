import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the vector field F = (P, Q, R)
def vector_field(x, y, z):
    P = y**2
    Q = x**2
    R = 0
    return P, Q, R

# Calculate the curl of the vector field at point (x, y, z)
def curl(x, y, z):
    dQ_dy = 2 * y
    dP_dx = 2 * x
    dR_dx = 0
    dQ_dx = 0
    dR_dy = 0
    dP_dy = 0
    return dR_dy - dQ_dx, dP_dx - dR_dx, 0  # Set the z-components to zero

# Create a grid of points in the x-y plane
x = np.linspace(-2, 2, 10)
y = np.linspace(-2, 2, 10)
X, Y = np.meshgrid(x, y)

# Calculate the vector field values at each point in the grid
U, V, W = vector_field(X, Y, 0)

# Calculate the curl of the vector field at each point in the grid
curl_U, curl_V, curl_W = curl(X, Y, 0)

# Create a 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the plane at z=0 in light blue
ax.plot_surface(X, Y, np.zeros_like(X), color='lightblue', alpha=0.5)

# Plot the vector field lying on the xy-plane (z=0)
ax.quiver(X, Y, np.zeros_like(X), U, V, np.zeros_like(X), length=0.1, normalize=True, color='b', label='Vector Field', pivot='tail')

# Plot the curl vectors at each point on the xy-plane (z=0)
ax.quiver(X, Y, np.zeros_like(X), curl_U, curl_V, np.zeros_like(X), length=0.1, normalize=True, color='r', label='Curl', pivot='tail')

# Set labels and title for the plot
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Vector Field and Curl in the xy-Plane')

# Add a legend to identify the vectors
ax.legend()

# Show the plot
plt.show()
