import matplotlib.pyplot as plt
import numpy as np

e = 2.718281828

def fun1(x):
    return 2 * pow(e, x) - x - 1


# plotting the function
x_1 = np.linspace(-2, 2, 400)
y_1 = [fun1(x) for x in x_1]

# plotting points
x_2 = np.array([1, 2, 3, 5, 7])
y_2 = np.array([1, 2, 3, 4, 5])

plt.plot(x_1, y_1, label='2 * e^x - x - 1')
plt.plot(x_2, y_2, label='y = x')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Line plot of the function fun1(x)')
plt.legend()
plt.show()