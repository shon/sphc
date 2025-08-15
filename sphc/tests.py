import sys
sys.path.append('.')
import re
import unittest

from sphc import tf


class TestSPHC(unittest.TestCase):

    def test_textarea(self):
        ta = tf.TEXTAREA()

        textarea_pat = '<TEXTAREA[ ]*>[ ]*</TEXTAREA[ ]*>'
        ta_s = str(ta)
        self.assertEqual(bool(re.match(textarea_pat, ta_s)), True)

    def test_nvattrs(self):
        # No values attributes
        chkbox = tf.CHECKBOX('content', 'checked')
        expected = '<CHECKBOX checked>content</CHECKBOX>'
        self.assertEqual(str(chkbox), expected)

    def test_dot_tag_generation(self):
        outer = tf.OUTER()
        outer.middle.inner = tf.DIV(Class='inner')
        expected = '<OUTER><MIDDLE><DIV Class="inner"></DIV></MIDDLE></OUTER>'
        self.assertEqual(str(outer), expected)

    def test_bigdoc(self):
        html = tf.HTML()
        html.head = tf.HEAD()
        html.body = tf.BODY()
        html.body.content = tf.DIV("Some Text here.", Class='content')
        html.body.content.br = tf.BR()
        html.body.content.br = tf.BR()
        html.body.content.empty_div = tf.DIV()
        html.footer = tf.FOOTER()

        data = [('One', '1'), ('Two', '2'), ('Three', '3')]
        atable = tf.TABLE()
        for element in data:
            row = tf.TR()
            row.cells = [tf.TD(element[0]), tf.TD(element[1])]
            atable.row = row

        more_cells = [tf.TD('Four'), tf.TD('4')]
        row = tf.TR()
        row.cells = more_cells

        atable.row = row

        c = tf.INPUT(None, 'checked', type='checkbox')

        html.body.content.c = c
        html.body.content.atable = atable

        expected = '<HTML><HEAD></HEAD><BODY><DIV Class="content">Some Text here.<BR/><BR/><DIV></DIV><INPUT type="checkbox" checked/><TABLE><TR><TD>One</TD><TD>1</TD></TR><TR><TD>Two</TD><TD>2</TD></TR><TR><TD>Three</TD><TD>3</TD></TR><TR><TD>Four</TD><TD>4</TD></TR></TABLE></DIV></BODY><FOOTER></FOOTER></HTML>'
        assert str(html) == expected

if __name__ == "__main__":
    unittest.main()
