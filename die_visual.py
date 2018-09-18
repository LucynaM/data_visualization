import pygal
from die import Die

# Create a D6
die_1 = Die()
die_2 = Die(10)

# Make some rolls, and store results in a list
results = [die_1.roll() + die_2.roll() for i in range(1000)]

# Analyze the results to find out how many times each value occurs
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result+1)]

# Visualize the results
hist = pygal.Bar()
hist.force_uri_protocol = 'http'

hist.title = "Wynik rzucania dwiema kośćmi D6 tysiąc razy"
hist.x_labels = [str(i) for i in range(2, max_result+1)]
hist.x_title = "Wynik"
hist.y_title = "Częstotliwość występowania wartości"

hist.add('D6 + D10', frequencies)
hist.render_to_file('dice_visual.svg')