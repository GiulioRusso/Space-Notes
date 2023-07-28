import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from matplotlib.patches import Arc

def update_complex_number(val):
    a = slider_a.val
    b = slider_b.val
    complex_number = complex(a, b)
    point.set_data(np.real(complex_number), np.imag(complex_number))
    magnitude_line.set_data([0, np.real(complex_number)], [0, np.imag(complex_number)])
    text.set_text(f'Complex Number: {a:.2f} + {b:.2f}i\nMagnitude: {np.abs(complex_number):.2f}\nPhase: {np.angle(complex_number):.2f} radians')

    # Update projections of a and b from the origin to the real and imaginary axes
    projection_a.set_data([0, complex_number.real], [0, 0])
    projection_b.set_data([0, 0], [0, complex_number.imag])

    # Update phase arc
    phase_angle = np.angle(complex_number)
    phase_arc.theta2 = np.degrees(phase_angle)

    plt.draw()

# Create a plot
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, right=0.7, bottom=0.35)

# Set plot limits and labels
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_aspect('equal')  # Set aspect ratio to be equal
ax.set_xlabel('Real')
ax.set_ylabel('Imaginary')
ax.grid(True)

# Create sliders for controlling a and b values
ax_a = plt.axes([0.25, 0.2, 0.65, 0.03], facecolor='lightgoldenrodyellow')
ax_b = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slider_a = Slider(ax_a, 'Real (a)', -10, 10, valinit=0)
slider_b = Slider(ax_b, 'Imaginary (b)', -10, 10, valinit=0)

# Initial complex number with a=0 and b=0
initial_complex_number = complex(0, 0)

# Plot the initial complex number as a point on the complex plane
point, = ax.plot(np.real(initial_complex_number), np.imag(initial_complex_number), 'ro')

# Draw projections of a and b from the origin to the real and imaginary axes
projection_a, = ax.plot([0, initial_complex_number.real], [0, 0], 'b--', label='a Projection')
projection_b, = ax.plot([0, 0], [0, initial_complex_number.imag], 'g--', label='b Projection')

# Draw the magnitude of the complex number as a line connecting the origin to the red dot
magnitude_line, = ax.plot([0, initial_complex_number.real], [0, initial_complex_number.imag], 'gray', label='Magnitude')

# Add an observer to the sliders
slider_a.on_changed(update_complex_number)
slider_b.on_changed(update_complex_number)

# Add a text to display the complex number, its magnitude, and phase in the title
text = ax.set_title(f'Complex Number: {initial_complex_number.real:.2f} + {initial_complex_number.imag:.2f}i\nMagnitude: {np.abs(initial_complex_number):.2f} Phase: {np.angle(initial_complex_number):.2f} radians')

# Draw phase arc
phase_arc = Arc((0, 0), 2, 2, angle=0, theta1=0, theta2=0, color='purple', label='Phase')
ax.add_patch(phase_arc)

# Add legend
ax.legend()

# Show the plot
plt.show()
