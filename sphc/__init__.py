from html import escape


TAGS_UNFRIENDLY_WITH_SELF_CLOSING = ('DIV', 'SELECT', 'TEXTAREA', 'SCRIPT', 'A', 'LABEL')
TAGS_WITH_NO_CLOSING = ('META', 'LINK', 'INPUT', 'IMG', 'BR', 'HR', 'DOCTYPE')


class pats:
    regular = '<%(tagname)s%(attributes)s>%(content)s%(children)s</%(tagname)s>'
    no_content = '<%(tagname)s%(attributes)s/>'
    no_end = '<%(tagname)s%(attributes)s/>'


class Tag(object):
    def __call__(self, content='', *nv_attrs, **attrs):
        should_escape = attrs.pop('escape', True)
        if isinstance(content, (Tag, list, tuple)):
            self.child = content  # this calls __setattr__ we dont't want to append directly to self.children
            _content = ''
        else:
            _content = (escape(content) if should_escape else content) if content else ''
        self._content = _content
        self.attributes = attrs
        if 'data_bind' in self.attributes:
            self.attributes['data-bind'] = self.attributes.pop('data_bind')
        self.nv_attributes = list(nv_attrs)
        return self

    def __init__(self, name):
        self._name = name.upper()
        self.children = []
        self.children_names = []
        self.attributes = {}
        self.nv_attributes = []
        self._content = ''

    def add_classes(self, class_names):
        if not class_names:
            return
        if 'Class' in self.attributes:
            self.attributes['Class'] = self.attributes['Class'] + ' ' + (' '.join(class_names))
        else:
            self.attributes['Class'] = ' '.join(class_names)
    #TODO: remove class(es)

    def set_required(self):
        self.nv_attributes.append('required')
        return self

    def add_child(self, name, value):
        self.children_names.append(name)
        self.children.append(value)

    def __setattr__(self, name, v):
        if name in ['_name', 'nv_attributes', 'children_names', 'children', 'attributes', '_content']:
            object.__setattr__(self, name, v)
        else:
            if isinstance(v, (tuple, list)):
                for i, elem in enumerate(v):
                    name = '%s-%d' % (name, i)
                    self.add_child(name, elem)
            else:
                assert isinstance(v, (str, Tag)), "Not a Tag/String object or list/tuple of such objects"
                self.add_child(name, v)

    def __getattr__(self, name):
        children_names = object.__getattribute__(self, 'children_names')
        if name in children_names:
            children = object.__getattribute__(self, 'children')
            ret = children[children_names.index(name)]
        else:
            try:
                ret = object.__getattribute__(self, name)
            except AttributeError:
                ret = Tag(name)
                setattr(self, name, ret)
        return ret

    def __str__(self):
        children_s = "".join(map(str, self.children))

        attrs = []
        if self.attributes:
            attrs.extend(['%s="%s"' % kv for kv in self.attributes.items()])
        if self.nv_attributes:
            attrs.extend(self.nv_attributes)

        attributes_s = ' '.join(attrs)

        if attributes_s: attributes_s = ' ' + attributes_s

        if self._name.upper() in TAGS_WITH_NO_CLOSING:
            return pats.no_end % dict(tagname=self._name, attributes=attributes_s)
        else:
            return pats.regular % dict(content=self._content, children=children_s, tagname=self._name, attributes=attributes_s)


class TagFactory:

    def __getattr__(self, tagname):
        return Tag(tagname)


tf = TagFactory()
