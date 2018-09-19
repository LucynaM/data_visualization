import json
from pygal.maps.world import World
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS
from country_codes import get_country_code


# Load the data into a list
filename = 'population_data.json'
with open(filename) as f:
    population_data = json.load(f)


cc_populations = {}


# Build a dictionary of population data in 2010.
for pop_dict in population_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population

# Store countries in 3 groups according to population number
cc_pops1, cc_pops2, cc_pops3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops1[cc] = pop
    elif pop < 1000000000:
        cc_pops2[cc] = pop
    else:
        cc_pops3[cc] = pop

wm_style = RS('#336699', base_style=LCS)
wm = World(style=wm_style)
wm.force_uri_protocol = 'http'
wm.title = 'Populacja na świecie w 2010 r. (dane dla poszczególnych państw)'
wm.add('0-10 mln', cc_pops1)
wm.add('10 mln - 1 mld', cc_pops2)
wm.add('> 1 mld', cc_pops3)

wm.render_to_file('world_population.svg')

