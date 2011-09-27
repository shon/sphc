import cgi

ESCAPE_DEFAULT = True
TAGS_UNFRIENDLY_WITH_SELF_CLOSING = ('DIV', 'SELECT', 'TEXTAREA', 'SCRIPT', 'A', 'LABEL')

class pats:
    regular = '<%(tagname)s%(nv_attributes)s%(attributes)s>%(content)s%(children)s</%(tagname)s>'
    no_content = '<%(tagname)s%(nv_attributes)s%(attributes)s/>'

class Tag(object):
    def __call__(self, content='', nv_attrs=(), escape=ESCAPE_DEFAULT, **attrs):
        if isinstance(content, (Tag, list, tuple)):
            self.child = content # this calls __setattr__ we dont't want to append directly to self.children
            _content = ''
        else:
            _content = (cgi.escape(content) if escape else content) if content else ''
        self._content = _content.replace('%', '%%')
        self.attributes = attrs
        self.nv_attributes = nv_attrs
        return self
    def __init__(self, name):
        self._name = name
        self.children = []
        self.attributes = {}
        self.nv_attributes = []
        self._content = ''
    def add_classes(self, class_names):
        if 'Class' in self.attributes:
            self.attributes['Class'] = self.attributes['Class'] + ' ' + (' '.join(class_names))
        else:
            self.attributes['Class'] = ' '.join(class_names)
    #TODO: remove class(es)
    def __setattr__(self, name, v):
        if name in ['_name', 'nv_attributes', 'children', 'attributes', '_content']:
            object.__setattr__(self, name, v)
        else:
            if isinstance(v, (tuple, list)):
                ext = ((name, elem) for elem in v)
                self.children.extend(ext)
            else:
                assert isinstance(v, (basestring,Tag)), "Not a Tag object"
                self.children.append((name, v))
    def __getattr__(self, name):
        children = object.__getattribute__(self, 'children')
        children_names = [c[0] for c in children]
        if name in children_names:
            ret = [v[1] for v in children if v[0] == name]
            if len(ret) == 1:
                ret = ret[0]
        else:
            ret = object.__getattribute__(self, name)
        return ret
    def __str__(self):
        children_s = ''
        for child_name, child in self.children:
            children_s += str(child)
        attributes_s = ' '.join('%s="%s"' % kv for kv in self.attributes.items())
        nv_attributes_s = ' '.join(self.nv_attributes)

        if attributes_s: attributes_s = ' ' + attributes_s
        if nv_attributes_s: nv_attributes_s = ' ' + nv_attributes_s
        if children_s: children_s = ' ' + children_s

        #if self.name.upper() in TAGS_UNFRIENDLY_WITH_SELF_CLOSING or self._content or children_s:
        return pats.regular % dict(content=self._content, children=children_s, tagname=self._name, attributes=attributes_s, nv_attributes=nv_attributes_s)
        return pats.no_content % dict(tagname=self._name, attributes=attributes_s, nv_attributes=nv_attributes_s)

    def pretty(self):
        from tidylib import tidy_document
        options = { "output-xhtml": 0,     # XHTML instead of HTML4
            "indent": 1,           # Pretty; not too much of a performance hit
            "tidy-mark": 0,        # No tidy meta tag in output
            "wrap": 0,             # No wrapping
            "alt-text": "",        # Help ensure validation
            }
        document, errors = tidy_document(str(self), options=options)
        #print(errors)
        return document

        #import xml.dom.minidom
        #xml = xml.dom.minidom.parseString(str(self)) # or xml.dom.minidom.parseString(xml_string)
        #return  xml.toprettyxml('  ')

class TagFactory:
    def __getattr__(self, tagname):
        return Tag(tagname)

tf = TagFactory()

def test():
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

    c = tf.INPUT(None, 'checked', type='checkbox', value='foo')

    html.body.content.c = c
    html.body.content.atable = atable
    html.body.content.attributes['id'] = 'content_id'

    print(html)
    #print(html.pretty())
