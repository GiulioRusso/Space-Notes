import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Define the 2x2 matrix A
A = np.array([[2, 1],
              [1, 3]])

# Calculate the eigenvalues and eigenvectors of A
eigenvalues, eigenvectors = np.linalg.eig(A)

# Separate the eigenvalues and eigenvectors
lambda1, lambda2 = eigenvalues
eigenvector1, eigenvector2 = eigenvectors[:, 0], eigenvectors[:, 1]

# Create a plot
fig, ax = plt.subplots(figsize=(8, 6))
plt.subplots_adjust(left=0.1, right=0.7, bottom=0.3)

# Define initial values for the original vector
x0, y0 = 1, 1

# Plot the original vector v
vector_artist_original = ax.quiver(0, 0, x0, y0, angles='xy', scale_units='xy', scale=1, color='blue', label='Original Vector v')

# Plot the transformed vector Av
transformed_v = np.dot(A, np.array([x0, y0]))
vector_artist_transformed = ax.quiver(0, 0, transformed_v[0], transformed_v[1], angles='xy', scale_units='xy', scale=1, color='red', label='Transformed Vector Av')

# Plot the eigenvectors scaled by their eigenvalues
eigenvector_artist1 = ax.quiver(0, 0, lambda1 * eigenvector1[0], lambda1 * eigenvector1[1], angles='xy', scale_units='xy', scale=1, color='green', label='λ1 * Eigenvector1')
eigenvector_artist2 = ax.quiver(0, 0, lambda2 * eigenvector2[0], lambda2 * eigenvector2[1], angles='xy', scale_units='xy', scale=1, color='purple', label='λ2 * Eigenvector2')

# Create sliders for controlling x and y coordinates
ax_x = plt.axes([0.1, 0.2, 0.65, 0.03], facecolor='lightgoldenrodyellow')
ax_y = plt.axes([0.1, 0.15, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slider_x = Slider(ax_x, 'X Coordinate', -5, 5, valinit=x0)
slider_y = Slider(ax_y, 'Y Coordinate', -5, 5, valinit=y0)

# Text boxes to display matrix A and eigenvalues
ax_textbox = plt.axes([0.8, 0.3, 0.15, 0.4], frameon=False)
ax_textbox.set_xticks([])
ax_textbox.set_yticks([])
matrix_text = f"Matrix A:\n{A}\n\nEigenvalues:\nλ1 = {lambda1:.2f}\nλ2 = {lambda2:.2f}"
ax_textbox.text(0, 0, matrix_text, ha='left', va='top', fontsize=10)

# Function to draw the ellipse formed by λ1 * eigenvector1 and λ2 * eigenvector2
def draw_ellipse():
    t = np.linspace(0, 2 * np.pi, 100)
    ellipse = lambda1 * np.outer(np.cos(t), eigenvector1) + lambda2 * np.outer(np.sin(t), eigenvector2)
    ax.plot(ellipse[:, 0], ellipse[:, 1], color='orange', linestyle='dashed', label='Ellipse')

# Update function for sliders
def update(val):
    x = slider_x.val
    y = slider_y.val
    vector_artist_original.set_UVC(x, y)

    # Calculate the transformed vector Av
    transformed_v = np.dot(A, np.array([x, y]))
    vector_artist_transformed.set_UVC(transformed_v[0], transformed_v[1])

    # Draw the ellipse
    draw_ellipse()

    # Redraw the plot
    plt.draw()

# Add an observer to the sliders
slider_x.on_changed(update)
slider_y.on_changed(update)

# Set plot limits and labels
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_aspect('equal')
ax.grid(True)
ax.legend()

# Draw the initial ellipse
draw_ellipse()

# Show the plot
plt.show()
