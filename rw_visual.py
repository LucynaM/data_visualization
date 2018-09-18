import matplotlib.pyplot as plt

from random_walk import RandomWalk


# Keep making new walks, as long as the program is active
while True:

    # Make a random walk, and plot the points.
    rw = RandomWalk()
    rw.fill_walk()

    plt.scatter(rw.x_values, rw.y_values, s=15)
    plt._show()

    keep_running = input("Utworzyć kolejny wykres? (t/n)")
    if keep_running == 'n':
        break