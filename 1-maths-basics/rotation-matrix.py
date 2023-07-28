import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

def plot_vector(ax, vector, label, color):
    return ax.quiver(0, 0, vector[0], vector[1], angles='xy', scale_units='xy', scale=1, color=color, label=label)

# Declare vector_artist_rotated and matrix_textbox outside the function
vector_artist_original = None
vector_artist_rotated = None
matrix_textbox = None

def update_rotation(val):
    global vector_artist_original, vector_artist_rotated, matrix_textbox  # Use the global variables
    # Get the rotation angle from the slider
    theta = np.radians(slider_theta.val)
    cos_theta = np.cos(theta)
    sin_theta = np.sin(theta)

    # Update the rotation matrix
    rotation_matrix[0, 0] = cos_theta
    rotation_matrix[0, 1] = -sin_theta
    rotation_matrix[1, 0] = sin_theta
    rotation_matrix[1, 1] = cos_theta

    # Calculate the rotated vector
    rotated_vector = np.dot(rotation_matrix, vector)

    # Update the original vector plot
    if vector_artist_original is None:
        vector_artist_original = plot_vector(ax, vector, "Original Vector", color='blue')
    else:
        vector_artist_original.set_UVC(vector[0], vector[1])

    # Update the rotated vector plot
    if vector_artist_rotated is None:
        vector_artist_rotated = plot_vector(ax, rotated_vector, "Rotated Vector", color='red')
    else:
        vector_artist_rotated.set_UVC(rotated_vector[0], rotated_vector[1])

    # Update the legend
    ax.legend()

    # Update the matrix textbox
    matrix_textbox.set_text("Rotation Matrix:\n" + str(rotation_matrix))

    # Draw the updated plot
    plt.draw()

if __name__ == "__main__":
    # Create the figure and axes
    fig, ax = plt.subplots(figsize=(6, 6))
    plt.subplots_adjust(left=0.1, right=0.7, bottom=0.3)

    # Initial vector coordinates
    vector = np.array([1, 0])

    # Plot the original vector
    vector_artist_original = plot_vector(ax, vector, "Original Vector", color='blue')

    # Create a slider for the rotation angle with specific values
    ax_theta = plt.axes([0.1, 0.1, 0.65, 0.03], facecolor='lightgoldenrodyellow')
    slider_theta = Slider(ax_theta, 'Rotation Angle (deg)', 0, 360, valinit=0, valstep=90)

    # Initialize the rotation matrix
    rotation_matrix = np.array([[1, 0], [0, 1]])

    # Add an observer to the slider
    slider_theta.on_changed(update_rotation)

    # Set plot limits and add grid lines
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.grid(True)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')

    # Create a textbox for displaying the rotation matrix
    matrix_textbox = fig.text(0.8, 0.4, "Rotation Matrix:\n" + str(rotation_matrix), fontsize=10, bbox=dict(facecolor='lightgoldenrodyellow', edgecolor='gray', boxstyle='round,pad=0.3'))

    # Show the plot
    plt.show()
