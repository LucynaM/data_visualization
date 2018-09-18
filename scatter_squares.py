import matplotlib.pyplot as plt


# display point chart

x_values = list(range(1, 5001))
y_values = [i**3 for i in range(1,5001)]


# for colormaps see https://matplotlib.org/examples/color/colormaps_reference.html
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.PiYG, edgecolor='none', s=20)


# Set chart title and label axes
plt.title("Sześciany liczb", fontsize=24)
plt.xlabel("Wartość", fontsize=14)
plt.ylabel("Sześciany wartości", fontsize=14)

# Set size of tick labels
plt.tick_params(axis='both', which='major', labelsize=14)

# Set range for each axis
plt.axis = ([0, 5100, 0, 125000000])


plt.show()



