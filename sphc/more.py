import os
import string
import sphc

from sphc import tf


class Page(object):
    def __init__(self, data={}):
        self.data = data

class HTML5Page(Page):
    doctype = "<!DOCTYPE html>"
    jslibs = []
    css_links = []
    title = "HTML5 template"
    script = None
    nav_menu = None

    def head(self):
        head = tf.HEAD()
        head.encoding = tf.META(charset="utf-8")
        head.title = tf.TITLE(self.title)
        head.jslibs = [tf.SCRIPT(src=path) for path in self.jslibs]
        head.csslinks = [tf.LINK(rel="stylesheet", href=path) for path in self.css_links]
        style = self.style()
        if style:
            head.style = tf.STYLE(style)
        return head

    def style(self):
        return None

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

    def render(self, data={}):
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
        if self.script:
            html.body.script = tf.SCRIPT(open(self.script).read(), escape=False, type="text/javascript", language="javascript")
        out = string.Template(str(html)).safe_substitute(data)
        return (self.doctype + out)


    def write(self, outpath, data={}):
        """
        outpath: file where output is to be written. If intermediate directories do not exist these would be created.
        data: String interpolation is attempted on output of render(). This is useful in builds.
        """
        outdir = os.path.dirname(outpath)
        if not os.path.exists(outdir): os.makedirs(outdir)
        open(outpath, 'w').write(self.render(data))
        return True


def script_fromfile(path):
    return tf.SCRIPT(open(path).read(), escape=False, type="text/javascript", language="javascript")

def css_fromfile(path):
    return tf.STYLE(open(path).read())


class FieldContainer(object):
    default_attrs = {}

    def __init__(self, classes=[], **attrs):
        self.classes = classes
        self.attrs = {}
        self.attrs.update(self.default_attrs)
        self.attrs.update(attrs)
        self.fields = []
        self.btns = []

    def add(self, elem):
        self.fields.append(elem)
        return elem

    def add_field(self, label='', input=None, fhelp=None, container_classes=[]):
        """
        Adds common field to form.
        label: field label
        fhelp: help text for the field
        css classes used
        ----------------
        field container div: field-box
        label: field-label
        input: field-input
        help: field-help
        """
        assert bool(input), 'input must be Tag object'
        field_box = tf.DIV(Class="field")
        field_box.add_classes(container_classes)
        field_box.label_box = tf.DIV(Class='field-label')
        if label:
            # if input is not provided, generate input id for linking input with label
            input_id = input.attributes.get('id') or ""
            if not input_id:
                if 'name' in input.attributes:
                    input_id = (self.attrs.get('id', 'form') + '-' + input.attributes['name'])
            if not 'id' in input.attributes:
                input.attributes['id'] = input_id
            field_box.label_box.label = tf.LABEL(label, For=input_id)
        field_box.input_box = tf.DIV(Class="field-input")
        field_box.input_box.input = input
        if 'required' in input.nv_attributes:
            field_box.input_box.c = tf.C(' *')
        if fhelp:
            field_box.fhelp = tf.SPAN(fhelp, Class='field-help')
        self.fields.append(field_box)

    def add_buttons(self, *btns):
        self.btns = btns

    def build(self):
        form = getattr(tf, self.tagname)(**self.attrs)
        if self.classes:
            form.add_classes(self.classes)
        form.fields = [(isinstance(field, Fieldset) and field.build() or field) for field in self.fields]
        if self.btns:
            form.status = tf.DIV(Class='action-status')
            buttons = tf.DIV(Class='buttons')
            buttons.btns = self.btns
            form.buttons = buttons
        return form

class Form(FieldContainer):
    """
    classes: list of css class to assign
    attrs: more form tag properties. optional
    """
    tagname = 'FORM'
    default_attrs = dict(method='POST')


class Fieldset(FieldContainer):
    tagname = 'FIELDSET'
