### https://towardsdatascience.com/generate-easily-reproducible-scientific-figures-with-pylustrator-9426292e07a4



import matplotlib.pyplot as plt
import numpy as np
import pylustrator
import scienceplots

# Use scientific plot style
#plt.style.use('scientific')
plt.style.use('science')

# Create dummy data

x = np.linspace(0, 4*np.pi, 200)
y1 = np.sin(x)
y2 = np.cos(x)

#pylustrator.start()


# Create panelled figure

fig = plt.figure()
ax1 = fig.add_subplot(311)
ax2 = fig.add_subplot(312)
ax3 = fig.add_subplot(313)


# Plot data
# Subplot 1

ax1.plot(x, y1, label = 'y1')
ax1.plot(x, y2, label = 'y2')
ax1.legend()

# Subplot 2
ax2.plot(x, y1)

# Subplot 3
ax3.plot(x, y2)


#% start: automatic generated code from pylustrator
plt.figure(1).ax_dict = {ax.get_label(): ax for ax in plt.figure(1).axes}
import matplotlib as mpl
getattr(plt.figure(1), '_pylustrator_init', lambda: ...)()
plt.figure(1).axes[0].set_xticks([2., 4., 6., 8., 12.], ['', '', '', '', ''], minor=True)
plt.figure(1).axes[0].set(position=[0.111, 0.6881, 0.3314, 0.2769])
plt.figure(1).axes[1].set_xticks([2., 4., 6., 8., 12.], ['', '', '', '', ''], minor=True)
plt.figure(1).axes[1].set(position=[0.111, 0.2655, 0.3383, 0.3007])
plt.figure(1).axes[2].set_xticks([2., 4., 6., 8., 12.], ['', '', '', '', ''], minor=True)
plt.figure(1).axes[2].set(position=[0.5295, 0.2655, 0.3383, 0.3007])
#% end: automatic generated code from pylustrator
plt.show()