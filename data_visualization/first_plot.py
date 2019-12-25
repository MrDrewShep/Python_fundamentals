
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2, 100)

plt.plot(x, x, label="linear", color="purple")
plt.plot(x, x**2, label="quadratic", marker="*")
plt.plot(x, x**3, label="cubic")

plt.xlabel("x label")
plt.ylabel("y label")
plt.title("Drew's Simple Plot")

plt.legend()

plt.show()
