============================
Simple Pythonic HTML Creator
============================

 - Ultra simple and works
 - Compatible with Python3/ 2.x

 - *Pythonic*
    ::
    
        >>> adiv = tf.DIV("Hello World!", id="header_1", Class="header")
        >>> print (adiv)
        <DIV id="header_1" class="header">Hello World</DIV>

.. contents:: It's super easy to learn :-)

Examples
========

Hello World!
------------
::

    >>> import sphc
    >>> tf = sphc.TagFactory()
    >>> header = tf.H1("Hello World!")
    >>> print(header)
    <H1>Hello World</H1>


Constructing a page
-------------------
::

    >>> doc = tf.HTML()
    >>> doc.body = tf.BODY()
    >>> doc.body.content = tf.H1("The content")
    >>> print(doc)
    <HTML>
        <BODY>
            <H1>The content</H1>
        </BODY>
    </HTML>


Using list of Tag objects
-------------------------
Especially usefule for constructing tables and select options::

    >>> data = [('One', '1'), ('Two', '2'), ('Three', '3')]
    >>> atable = tf.TABLE()
    >>> for element in data:
    >>>     row = tf.TR()
    >>>     row.cells = [tf.TD(element[0]), tf.TD(element[1])]
    >>>     atable.row = row

Wrapping
--------
    >>> block1 = tf.DIV(tf.DIV("content", Class="inner"), Class="outer")
    >>> block2 = tf.DIV([tf.DIV(), tf.DIV()], Class="outer")
    >>> content = tf.DIV([block1, block2])

Piping 
------
set_required method below sets required property on Tag object AND returns Tag object::

    >>> form = tf.FORM()
    >>> form.username = tf.INPUT(name="username").set_required()
    >>> print(form)
    <FORM>
        <INPUT name="username" required/>
    </FORM>


Properties with no value required
---------------------------------
::

   >>> c = tf.INPUT(nv_attrs=['checked'], type='checkbox', value='foo')
   >>> print(c)
   <INPUT checked type="checkbox", value="foo"/>

Escaping
--------
::

    >>> print(tf.C(' >> ')) # Default
    >>> <C> &gt;&gt; </C>

    >>> print(tf.C(' >> ', escape=False))
    >>> <C> >> </C>


More
====
Well since you reached here time to show some experimental stuff.

Hello sphc.more
---------------
(loosely based on html5boilerplate.com templates)::

    >>> import sphc.more
    >>> tf = sphc.TagFactory()
    >>> class MyPage(sphc.more.HTML5Page):
            def footer(self):
                return tf.FOOTER("Footer text")
    >>> my_page = MyPage()
    >>> my_page.render()

This will return a string that would contain html exactly like what you have expected

Building a form
---------------
::

    >>> import sphc
    >>> import sphc.more
    >>> 
    >>> tf = sphc.TagFactory()
    >>> 
    >>> form = sphc.more.Form(classes=['vform'])
    >>> form.add_field('Username', tf.INPUT(type="TEXT", id='username', name="username", placeholder="Username").set_required())
    >>> form.add_field('Password', tf.INPUT(type="password", id='password', name="password", placeholder="Password"))
    >>> form.add_buttons(tf.BUTTON("Log In", id='login-btn', type='button'))
    >>> print form.build()

    <FORM method="POST" Class="vform"> 
        <DIV Class="field">
            <DIV Class="field-label"> <LABEL For="username">Username</LABEL></DIV>
            <DIV Class="field-input"> 
                <INPUT required placeholder="Username" type="TEXT" name="username" id="username"></INPUT><C>*</C>
            </DIV>
        </DIV>
        <DIV Class="field"> 
            <DIV Class="field-label"> <LABEL For="password">Password</LABEL></DIV>
            <DIV Class="field-input">
                <INPUT placeholder="Password" type="password" name="password" id="password"></INPUT>
            </DIV>
        </DIV>
        <DIV Class="action-status"></DIV>
        <DIV Class="buttons"> 
            <BUTTON type="button" id="login-btn">Log In</BUTTON>
        </DIV>
    </FORM>


Finally
=======

 - Source: `<https://github.com/shon/sphc>`_
 - Any suggestions/issues | `<https://github.com/shon/sphc/issues>`_
 - Critisism or if you feel such thing already implemented feel free to write Authour.


Similar packages
----------------
    - http://shpaml.webfactional.com/ # Just awesome
    - http://pypi.python.org/pypi/html # Inspiration. It uses __getattr__ trick whereas this package is mostly a __setattr__ trick, aiming sharing of blocks.
    - http://karrigell.sourceforge.net/en/htmltags.html

TODO
----
 - To add more tests
 - A document class ?
