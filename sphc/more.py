import os
import itertools
import sphc

tf = sphc.TagFactory()

def gen_jquery_urls(jquery_version='1.6.2', jquery_ui_version='1.8.14'):
    return [ ('https://ajax.googleapis.com/ajax/libs/jquery/%s/jquery.min.js' % jquery_version),
        ('http://ajax.googleapis.com/ajax/libs/jqueryui/%s/jquery-ui.min.js' % jquery_ui_version) ]

css_links = [ 'https://github.com/thatcoolguy/gridless-boilerplate/raw/master/assets/css/main.css' ]

class HTML5Page(object):
    """
    Common case HTML5 template
    Loosely based on HTML5 Boilerplate

    nav_menu: list eg. [('Home', '/', None), ('About Us', '/about', None)]
        Also supports higly flexible navigation options as shown in example below
        >>> home_opts = [tf.A('Home Option 1', href='/home/opt_1'), tf.A('Home Option 2', href='/home/opt_2')]
        >>> profile_opts = [tf.A('Profile Option 1', href='/profile/opt_1'), tf.A('Profile Option 2', href='/profile/opt_2')]
        >>> nav_menu = [
            ('Home', '#home', home_opts),
            ('Invoicing', '#home', profile_opts) ]
    """
    doctype = "<!DOCTYPE html>"
    jslibs = gen_jquery_urls()
    css_links = css_links
    title = "Common case HTML5 template"
    nav_menu = []
    current_nav = ""

    def head(self):
        head = tf.HEAD()
        head.title = tf.TITLE(self.title)
        head.jslibs = [tf.SCRIPT(src=path) for path in self.jslibs]
        head.csslinks = [tf.LINK(rel="stylesheet", href=path) for path in self.css_links]
        return head

    def header(self):
        return tf.HEADER()

    def footer(self):
        return tf.FOOTER()

    def topbar(self):
        return ''

    def bottombar(self):
        return ''

    def main(self):
        return ''

    def nav(self):
        if not self.nav_menu: return ''
        nav = tf.NAV()
        menu = []
        for label, url, opts in self.nav_menu:
            header = tf.H2()
            header.link = tf.A(label, href=url)
            opts_box = tf.DIV(Class="nav-opt")
            if opts:
                for opt in opts:
                    opt_box = tf.DIV(Class="nav-opt-item")
                    opt_box.opt = opt
                    opts_box.opt_box = opt_box
            if label == self.current_nav:
                header.add_classes(["nav-current"])
                opts_box.add_classes(["nav-opt-current"])
            menu.extend([header, opts_box])
        nav.menu = menu
        return nav

    def render(self):
        html = tf.HTML()
        html.head = self.head()
        html.body = tf.BODY()
        html.body.topbar = self.topbar()
        html.body.container = tf.DIV(Class="container")
        html.body.container.nav = self.nav()
        html.body.container.header = self.header()
        html.body.container.main = tf.DIV(id="main", role="main")
        html.body.container.main.main = self.main()
        html.body.container.footer = self.footer()
        html.body.bottombar = self.bottombar()
        return self.doctype + str(html)

    def write(self, outpath, data={}):
        """
        outpath: file where output is to be written. If intermediate directories do not exist these would be created.
        data: String interpolation is attempted on output of render(). This is useful in builds.
        """
        outdir = os.path.dirname(outpath)
        if not os.path.exists(outdir): os.makedirs(outdir)
        open(outpath, 'w').write(self.render() % data)
        return True

def clear():
    return tf.BR(style="clear:both") # TODO: Use class clear/clearfix
