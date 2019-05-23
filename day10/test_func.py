import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
  """tests for name_function.py"""
  def test_first_last_name(self):
    """ do names like 'janis joplin' work? """
    formatted_name = get_formatted_name('janis', 'joplin')
    self.assertEqual(formatted_name, 'Janis Joplin')
  def test_first_last_middle(self):
    """ do names like 'xx oo ww' work?"""
    formatted_name = get_formatted_name('xx','oo','ww')
if __name__ == '__main__':
  unittest.main()
