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
    Mostly based on HTML5 Boilerplate

    nav: list eg. [('Home', '/', None), ('About Us', '/about', None)]
        Also supports higly flexible navigation options such as
        >>> home_opts = [tf.A('Home Option 1', href='/home/opt_1'), tf.A('Home Option 2', href='/home/opt_2')]
        >>> profile_opts = [tf.A('Profile Option 1', href='/profile/opt_1'), tf.A('Profile Option 2', href='/profile/opt_2')]
        >>> nav_links = [
            ('Home', '#home', home_opts),
            ('Invoicing', '#home', profile_opts)
            ]
    """
    doctype = "<!doctype html>"
    jslibs = gen_jquery_urls()
    css_links = css_links
    title = "Common case HTML5 template"
    nav_links = []

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

    def main(self):
        return ''

    def nav(self):
        nav = tf.NAV()
        nav.links_container = tf.UL()
        nav.link_opts = tf.DIV(Class='link_opts')
        c = itertools.count()
        for label, url, opt in self.nav_links:
            link_id = c.next()
            li = tf.LI()
            li.link = tf.A(label, Class="navlink", id=('navlink-%s' % link_id), href=url)
            nav.links_container.li = li
            if opt:
                opt_container = tf.DIV(Class="navlink-opt", id=('navlink_opt-%s' % link_id))
                opt_container.opt = opt
                nav.link_opts.opt_container = opt_container
        return nav

    def render(self):
        html = tf.HTML()
        html.head = self.head()
        html.body = tf.BODY()
        html.body.nav = self.nav()
        html.body.container = tf.DIV(id="container")
        html.body.container.header = self.header()
        html.body.container.main = tf.DIV(id="main", role="main")
        html.body.container.main.main = self.main()
        html.body.footer = self.footer()
        return self.doctype + str(html)

    def write(self, outpath):
        outdir = os.path.dirname(outpath)
        if not os.path.exists(outdir): os.makedirs(outdir)
        open(outpath, 'w').write(self.render())
        return True
