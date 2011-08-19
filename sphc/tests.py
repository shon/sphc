import sys

sys.path.insert(0, '../sphc/')

import sphc
import sphc.more

import unittest
import re

class TestSPHC(unittest.TestCase):

    def setUp(self):
        self.tf = sphc.TagFactory()

    def test_textarea(self):
        ta = self.tf.TEXTAREA()

        textarea_pat = '<TEXTAREA[ ]*>[ ]*</TEXTAREA[ ]*>'
        ta_s = str(ta)
        self.assertEqual(bool(re.match(textarea_pat, ta_s)), True)

if __name__ == "__main__":
    unittest.main()
