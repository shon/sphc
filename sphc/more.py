import sphc
tf = sphc.TagFactory()

def gen_jquery_urls(jquery_version='1.6.2', jquery_ui_version='1.8.14'):
    return [ ('https://ajax.googleapis.com/ajax/libs/jquery/%s/jquery.min.js' % jquery_version),
        ('http://ajax.googleapis.com/ajax/libs/jqueryui/%s/jquery-ui.min.js' % jquery_ui_version) ]

class HTML5Page(object):
    """
    Common case HTML5 template
    Mostly based on HTML5 Boilerplate
    """
    doctype = "<!doctype html>"
    jslibs = gen_jquery_urls()
    title = "Common case HTML5 template"

    def head(self):
        head = tf.HEAD()
        head.title = tf.TITLE(self.title)
        head.jslibs = [tf.SCRIPT(src=path) for path in self.jslibs]
        return head

    def header(self):
        return tf.HEADER()

    def footer(self):
        return tf.FOOTER()

    def main(self):
        return tf.DIV(id="main", role="main")

    def render(self):
        html = tf.HTML()
        html.head = self.head()
        html.body = tf.BODY()
        html.body.container = tf.DIV(id="container")
        html.body.container.header = self.header()
        html.body.container.main = self.main()
        html.body.footer = self.footer()
        return self.doctype + str(html)

def test():
    page = HTML5Page()
    print(page.render())
