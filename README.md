# Simple Pythonic HTML Creator (sphc) 🐍✨

A super simple and *Pythonic* way to create HTML, for Python 3.

- ✅ Ultra simple and it just works!
- 🐍 Pythonic syntax you'll love.
- 🚀 Modern and built for Python 3.

```python
>>> from sphc import tf
>>> adiv = tf.DIV("Hello World!", id="header_1", Class="header")
>>> print(adiv)
<DIV id="header_1" Class="header">Hello World!</DIV>
```

## 📖 It's super easy to learn!

### Hello World!

```python
>>> import sphc
>>> tf = sphc.TagFactory()
>>> header = tf.H1("Hello World!")
>>> print(header)
<H1>Hello World!</H1>
```

### Constructing a Page 📄

```python
>>> doc = tf.HTML()
>>> doc.body.content = tf.H1("The content")
>>> print(doc)
<HTML><BODY><H1>The content</H1></BODY></HTML>
```

### Using Lists of Tags 📋

Especially useful for constructing tables and select options.

```python
>>> data = [('One', '1'), ('Two', '2'), ('Three', '3')]
>>> atable = tf.TABLE()
>>> for element in data:
...     row = tf.TR()
...     row.cells = [tf.TD(element[0]), tf.TD(element[1])]
...     atable.row = row
>>> print(atable)
<TABLE><TR><TD>One</TD><TD>1</TD></TR><TR><TD>Two</TD><TD>2</TD></TR><TR><TD>Three</TD><TD>3</TD></TR></TABLE>
```

### Wrapping Content 🎁

```python
>>> block1 = tf.DIV(tf.DIV("content", Class="inner"), Class="outer")
>>> block2 = tf.DIV([tf.DIV(), tf.DIV()], Class="outer")
>>> content = tf.DIV([block1, block2])
```

### Chaining Methods ⛓️

The `set_required` method sets the `required` property on a Tag object AND returns the Tag object, so you can chain calls.

```python
>>> form = tf.FORM()
>>> form.username = tf.INPUT(name="username").set_required()
>>> print(form)
<FORM><INPUT name="username" required/></FORM>
```

### Properties with No Value ☑️

```python
>>> c = tf.INPUT(None, 'checked', type='checkbox', value='foo')
>>> print(c)
<INPUT type="checkbox" value="foo" checked/>
```

### Escaping Content 🔓

By default, content is escaped to prevent XSS attacks.

```python
>>> print(tf.C(' >> ')) # Default
<C> &gt;&gt; </C>

>>> print(tf.C(' >> ', escape=False))
<C> >> </C>
```

## 🚀 More Experimental Stuff

Ready for more? Let's dive into some advanced features in `sphc.more`.

### Hello `sphc.more` 👋

```python
>>> import sphc.more
>>> tf = sphc.TagFactory()
>>> class MyPage(sphc.more.HTML5Page):
...     def footer(self):
...         return tf.FOOTER("Footer text")
>>> my_page = MyPage()
>>> my_page.render()
```
This will return a complete HTML5 page as a string, just like you'd expect.

### Building a Form 📝

```python
>>> import sphc
>>> import sphc.more
>>>
>>> tf = sphc.TagFactory()
>>>
>>> form = sphc.more.Form(classes=['vform'])
>>> form.add_field('Username', tf.INPUT(type="TEXT", id='username', name="username").set_required())
>>> form.add_field('Password', tf.INPUT(type="password", id='password', name="password"))
>>> form.add_buttons(tf.BUTTON("Log In", id='login-btn', type='button'))
>>> print(form.build())
<FORM method="POST" Class="vform"><DIV Class="field"><DIV Class="field-label"><LABEL For="username">Username</LABEL></DIV><DIV Class="field-input"><INPUT type="TEXT" id="username" name="username" required/><C> *</C></DIV></DIV><DIV Class="field"><DIV Class="field-label"><LABEL For="password">Password</LABEL></DIV><DIV Class="field-input"><INPUT type="password" id="password" name="password"/></DIV></DIV><DIV Class="action-status"></DIV><DIV Class="buttons"><BUTTON id="login-btn" type="button">Log In</BUTTON></DIV></FORM>
```

### Forms with Fieldsets 🗂️

```python
>>> form = sphc.more.Form()
>>>
>>> about = form.add(sphc.more.Fieldset())
>>> about.add(sphc.tf.LEGEND('About'))
>>> about.add_field('Name', sphc.tf.INPUT(name='name', type='text'))
>>>
>>> contact = form.add(sphc.more.Fieldset())
>>> contact.add(sphc.tf.LEGEND('Contact'))
>>> contact.add_field('Email', sphc.tf.INPUT(name='email', type='email'))
>>> print(form.build())
<FORM method="POST"><FIELDSET><LEGEND>About</LEGEND><DIV Class="field"><DIV Class="field-label"><LABEL For="form-name">Name</LABEL></DIV><DIV Class="field-input"><INPUT name="name" type="text" id="form-name"/></DIV></DIV></FIELDSET><FIELDSET><LEGEND>Contact</LEGEND><DIV Class="field"><DIV Class="field-label"><LABEL For="form-email">Email</LABEL></DIV><DIV Class="field-input"><INPUT name="email" type="email" id="form-email"/></DIV></DIV></FIELDSET></FORM>
```

## 💻 Source

Find the source code on GitHub:
[https://github.com/shon/sphc](https://github.com/shon/sphc)

## 🛠️ Building from Source

For instructions on how to build and distribute the package from source, please see [BUILD.md](BUILD.md).

---

## 🚀 Performance

A small, informal benchmark was conducted to compare `sphc` with some other popular template/html generation libraries. The benchmark generates a 100-row HTML table 1000 times. The results below show the time taken in seconds (lower is better).

Please note that these benchmarks are not comprehensive and your results may vary depending on the specific use case and hardware.

| Library      | Time (seconds) | Chart (longer is slower)                                   |
|--------------|----------------|------------------------------------------------------------|
| [Mako]       | 1.81           | `████`                                                     |
| [Jinja2]     | 4.08           | `█████████`                                                |
| [sphc]       | 11.33          | `██████████████████████████`                                 |
| [dominate]   | 17.26          | `████████████████████████████████████████`                   |

*These results were generated on a generic cloud instance and should be taken with a grain of salt.*

[Mako]: https://www.makotemplates.org/
[Jinja2]: https://jinja.palletsprojects.com/
[dominate]: https://github.com/Knio/dominate
[sphc]: https://github.com/shon/sphc
