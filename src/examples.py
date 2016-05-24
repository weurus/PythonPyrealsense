import time
import matplotlib.pyplot as plt
import pyrealsense as pyrs
pyrs.start()
time.sleep(2)

cm = pyrs.get_colour_map()
plt.imshow(cm)
plt.show()