import sphc
import sphc.more

import unittest
import re

class TestSPHC(unittest.TestCase):

    def test_textarea(self):
        ta = sphc.TEXAREA()
        textarea_pat = ''
        self.assertEqual(bool(re.match(textarea_pat, str(ta))), True)

if __name__ == "__main__":
    unittest.main()
