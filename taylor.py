import numpy as np
import matplotlib.pyplot as plt

# Define the sine function
def sine(x):
    return np.sin(x)

# Define the Taylor approximations
def taylor_approximation(x, order):
    if order == 1:
        return x
    elif order == 2:
        return x - (x**3) / 6
    elif order == 3:
        return x - (x**3) / 6 + (x**5) / 120

# Generate x values from -4*pi to 4*pi
x = np.linspace(-4*np.pi, 4*np.pi, 100)

# Compute y values for sine function
y_sine = sine(x)

# Compute y values for Taylor approximations of different orders
y_approx_1st_order = taylor_approximation(x, 1)
y_approx_2nd_order = taylor_approximation(x, 2)
y_approx_3rd_order = taylor_approximation(x, 3)

# Plot the sine function and Taylor approximations
plt.plot(x, y_sine, label='Sine Function')
plt.plot(x, y_approx_1st_order, '--', label='1st Order Approximation')
plt.plot(x, y_approx_2nd_order, '--', label='2nd Order Approximation')
plt.plot(x, y_approx_3rd_order, '--', label='3rd Order Approximation')

# Set the y-axis limits to -4 and 4
plt.ylim(-4, 4)

# Add grid
plt.grid(True)

# Add labels and title to the plot
plt.xlabel('x')
plt.ylabel('y')
plt.title('Sine Function and Taylor Approximations')

# Add a legend
plt.legend()

# Display the plot
plt.show()
