from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
    """Return 2-char code of the state used by Pygal"""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    return None


