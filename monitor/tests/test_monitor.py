import sys
import os
sys.path.append('..')
sys.path.append(os.path.join(sys.path[0], '..'))

import unittest
from expecter import expect

class TestMySanity(unittest.TestCase):
  def test_truthiness(self):
    expect(True) == True
