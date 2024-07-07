# Matplotlib

Matplotlib is a comprehensive library for creating static, animated, and interactive
visualizations in Python. Most of the Matplotlib utilities lies under the pyplot module,
and are usually imported under the plt alias.

## Installation of Matplotlib

If you have Python and PIP already installed on a system, then installation of Matplotlib is very easy.

Install it using this command:

```bash
pip install matplotlib
```
The plot() function is used to draw points (markers) in a diagram. This function takes
parameters for specifying points in the diagram. First parameter is an array containing
points on the x-axis and second parameter is an array containing the points on the y-axis. 

For example, to draw a line in a diagram from position (1, 3) to position (8, 10),
we write.

```bash
import matplotlib.pyplot as plt
import numpy as np
xpoints = np.array([1, 8])
ypoints = np.array([3, 10])
plt.plot(xpoints, ypoints)
plt.show()

```

