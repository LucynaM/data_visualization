import pygal
from die import Die

# Create a D6
die = Die()

# Make some rolls, and store results in a list
results = [die.roll() for i in range(1000)]

# Analyze the results to find out how many times each value occurs
frequencies = [results.count(value) for value in range(1, die.num_sides+1)]

# Visualize the results
hist = pygal.Bar()
hist.force_uri_protocol = 'http'

hist.title = "Wynik rzucania pojedynczą kością D6 tysiąc razy"
hist.x_labels = [str(i) for i in range(1, 7)]
hist.x_title = "Wynik"
hist.y_title = "Częstotliwość występowania wartości"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')