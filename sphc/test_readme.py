import sys
sys.path.append('.')
import unittest
import sphc
from sphc import tf
import sphc.more

class TestReadme(unittest.TestCase):
    def test_hello_world(self):
        tf = sphc.TagFactory()
        header = tf.H1("Hello World!")
        self.assertEqual(str(header), "<H1>Hello World!</H1>")

    def test_constructing_a_page(self):
        tf = sphc.TagFactory()
        doc = tf.HTML()
        doc.body.content = tf.H1("The content")
        self.assertEqual(str(doc), "<HTML><BODY><H1>The content</H1></BODY></HTML>")

    def test_using_lists_of_tags(self):
        tf = sphc.TagFactory()
        data = [('One', '1'), ('Two', '2'), ('Three', '3')]
        atable = tf.TABLE()
        for element in data:
            row = tf.TR()
            row.cells = [tf.TD(element[0]), tf.TD(element[1])]
            atable.row = row
        print(atable)
        expected = '<TABLE><TR><TD>One</TD><TD>1</TD></TR><TR><TD>Two</TD><TD>2</TD></TR><TR><TD>Three</TD><TD>3</TD></TR></TABLE>'
        self.assertEqual(str(atable), expected)

    def test_wrapping_content(self):
        tf = sphc.TagFactory()
        block1 = tf.DIV(tf.DIV("content", Class="inner"), Class="outer")
        self.assertEqual(str(block1), '<DIV Class="outer"><DIV Class="inner">content</DIV></DIV>')
        block2 = tf.DIV([tf.DIV(), tf.DIV()], Class="outer")
        self.assertEqual(str(block2), '<DIV Class="outer"><DIV></DIV><DIV></DIV></DIV>')
        content = tf.DIV([block1, block2])
        self.assertEqual(str(content), '<DIV><DIV Class="outer"><DIV Class="inner">content</DIV></DIV><DIV Class="outer"><DIV></DIV><DIV></DIV></DIV></DIV>')

    def test_chaining_methods(self):
        tf = sphc.TagFactory()
        form = tf.FORM()
        form.username = tf.INPUT(name="username").set_required()
        self.assertEqual(str(form), '<FORM><INPUT name="username" required/></FORM>')

    def test_properties_with_no_value(self):
        tf = sphc.TagFactory()
        c = tf.INPUT(None, 'checked', type='checkbox', value='foo')
        self.assertEqual(str(c), '<INPUT type="checkbox" value="foo" checked/>')

    def test_escaping_content(self):
        tf = sphc.TagFactory()
        self.assertEqual(str(tf.C(' >> ')), '<C> &gt;&gt; </C>')
        self.assertEqual(str(tf.C(' >> ', escape=False)), '<C> >> </C>')

    def test_hello_sphc_more(self):
        tf = sphc.TagFactory()
        class MyPage(sphc.more.HTML5Page):
            def footer(self):
                return tf.FOOTER("Footer text")
        my_page = MyPage()
        output = my_page.render()
        self.assertTrue(output.startswith('<!DOCTYPE html>'))
        self.assertIn('<FOOTER>Footer text</FOOTER>', output)

    def test_building_a_form(self):
        tf = sphc.TagFactory()
        form = sphc.more.Form(classes=['vform'])
        form.add_field('Username', tf.INPUT(type="TEXT", id='username', name="username").set_required())
        form.add_field('Password', tf.INPUT(type="password", id='password', name="password"))
        form.add_buttons(tf.BUTTON("Log In", id='login-btn', type='button'))
        expected = '<FORM method="POST" Class="vform"><DIV Class="field"><DIV Class="field-label"><LABEL For="username">Username</LABEL></DIV><DIV Class="field-input"><INPUT type="TEXT" id="username" name="username" required/><C> *</C></DIV></DIV><DIV Class="field"><DIV Class="field-label"><LABEL For="password">Password</LABEL></DIV><DIV Class="field-input"><INPUT type="password" id="password" name="password"/></DIV></DIV><DIV Class="action-status"></DIV><DIV Class="buttons"><BUTTON id="login-btn" type="button">Log In</BUTTON></DIV></FORM>'
        self.assertEqual(str(form.build()), expected)

    def test_forms_with_fieldsets(self):
        form = sphc.more.Form()
        about = form.add(sphc.more.Fieldset())
        about.add(sphc.tf.LEGEND('About'))
        about.add_field('Name', sphc.tf.INPUT(name='name', type='text'))
        contact = form.add(sphc.more.Fieldset())
        contact.add(sphc.tf.LEGEND('Contact'))
        contact.add_field('Email', sphc.tf.INPUT(name='email', type='email'))
        expected = '<FORM method="POST"><FIELDSET><LEGEND>About</LEGEND><DIV Class="field"><DIV Class="field-label"><LABEL For="form-name">Name</LABEL></DIV><DIV Class="field-input"><INPUT name="name" type="text" id="form-name"/></DIV></DIV></FIELDSET><FIELDSET><LEGEND>Contact</LEGEND><DIV Class="field"><DIV Class="field-label"><LABEL For="form-email">Email</LABEL></DIV><DIV Class="field-input"><INPUT name="email" type="email" id="form-email"/></DIV></DIV></FIELDSET></FORM>'
        self.assertEqual(str(form.build()), expected)

    def test_forms_with_fieldsets(self):
        form = sphc.more.Form()
        about = form.add(sphc.more.Fieldset())
        about.add(sphc.tf.LEGEND('About'))
        about.add_field('Name', sphc.tf.INPUT(name='name', type='text'))
        contact = form.add(sphc.more.Fieldset())
        contact.add(sphc.tf.LEGEND('Contact'))
        contact.add_field('Email', sphc.tf.INPUT(name='email', type='email'))
        expected = '<FORM method="POST"><FIELDSET><LEGEND>About</LEGEND><DIV Class="field"><DIV Class="field-label"><LABEL For="form-name">Name</LABEL></DIV><DIV Class="field-input"><INPUT name="name" type="text" id="form-name"/></DIV></DIV></FIELDSET><FIELDSET><LEGEND>Contact</LEGEND><DIV Class="field"><DIV Class="field-label"><LABEL For="form-email">Email</LABEL></DIV><DIV Class="field-input"><INPUT name="email" type="email" id="form-email"/></DIV></DIV></FIELDSET></FORM>'
        self.assertEqual(str(form.build()), expected)

if __name__ == "__main__":
    unittest.main()
