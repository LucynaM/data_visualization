import unittest
from country_codes import get_country_code

class CountryCodeTestCase(unittest.TestCase):
    """Test for country_codes.py"""

    def test_country_code(self):
        cc = get_country_code('Andorra')
        self.assertEqual(cc, 'ad')

unittest.main()