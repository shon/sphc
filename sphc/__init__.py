NO_CONTENT_TAGS = ('br',)

class pats:
    regular = '<%(tagname)s%(attributes)s>%(content)s%(children)s</%(tagname)s>'
    no_content = '<%(tagname)s/>'

class Tag:
    def __call__(self, content='', **attrs):
        self._content = content
        self.attributes = attrs
        return self
    def __init__(self, name):
        self.name = name
        self.pat = pats.regular
        if name.lower() in NO_CONTENT_TAGS:
            self.pat = pats.no_content
        self.children = []
        self.attributes = {}
        self._content = ''
    def __setattr__(self, name, v):
        if name in ['name', 'pat', 'children', 'attributes', '_content']:
            object.__setattr__(self, name, v)
        else:
            if isinstance(v, (tuple, list)):
                ext = ((name, elem) for elem in v)
                self.children.extend(ext)
            else:
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
        if attributes_s: attributes_s = ' ' + attributes_s
        #if children_s: children_s = '\n' + children_s + '\n'
        return self.pat % dict(content=self._content, children=children_s, tagname=self.name, attributes=attributes_s)
    def pretty(self):
        # should try pytidylib
        import xml.dom.minidom

        xml = xml.dom.minidom.parseString(str(self)) # or xml.dom.minidom.parseString(xml_string)
        return  xml.toprettyxml('  ')

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

    html.body.content.atable = atable
    html.body.content.attributes['id'] = 'content_id'

    html = test()
    print(html)
    print(html.pretty())
