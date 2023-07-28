import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc

# Create the plot
fig, ax = plt.subplots()

# Angle value for the triangle (30 degrees)
angle_degrees_a = 30

# Length of the sides of the right triangle
adjacent_side = 4

# Convert the angle from degrees to radians
angle_radians_a = np.radians(angle_degrees_a)

# Calculate the lengths of opposite side and hypotenuse
opposite_side_a = adjacent_side * np.tan(angle_radians_a)
hypotenuse_a = np.sqrt(adjacent_side**2 + opposite_side_a**2)

# Create the right triangle plots
triangle_hypotenuse, = ax.plot([0, adjacent_side], [0, opposite_side_a], 'k-', color='blue', label='Hypotenuse')
triangle_opposite, = ax.plot([adjacent_side, adjacent_side], [0, opposite_side_a], 'k-', color='red', label='Opposite Side')
triangle_adjacent, = ax.plot([0, adjacent_side], [0, 0], 'k-', color='green', label='Adjacent Side')

# Set plot labels and grid
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.grid(True)

# Set aspect ratio to equal, so the triangle looks proportional
ax.set_aspect('equal')

# Set the title for the plot
ax.set_title(f"Right Triangle with {angle_degrees_a}° Angle")

# Draw the angle reference circle inside the triangle from 0 to 30 degrees
#angle_circle = plt.Circle((0, 0), 0.6, color='gray', fill=True)
#ax.add_patch(angle_circle)

# Draw the arc of the angle reference circle from 0 to 30 degrees
arc_angle_a = Arc((0, 0), width=1.2, height=1.2, angle=0, theta1=0, theta2=angle_degrees_a, color='gray', linestyle='dashed', fill=False)
ax.add_patch(arc_angle_a)

# Show the legend
ax.legend()

# Set plot limits
plt.xlim(-1, 6)
plt.ylim(-1, 3)

# Show the plot
plt.show()
