Simple Pythonic HTML Creator
============================

 - *Very alpha yet* but works
 - Compatible with Python3/ 2.x

 - Source: `<https://github.com/shon/sphc>`_
 - Any suggestions/issues | `<https://github.com/shon/sphc/issues>`
 - Critisism or if you feel such thing already implemented feel free to write Authour.

As simple as below::

    >> import sphw

    >> tf = sphw.TagFactory()

    >> html = tf.HTML()
    >> html.head = tf.HEAD()
    >> html.body = tf.BODY()
    >> html.body.content = tf.DIV("Some Text here.", Class='content')
    >> html.body.content.br = tf.BR()
    >> html.body.content.br = tf.BR()
    >> html.footer = tf.FOOTER()

    >> data = [('One', '1'), ('Two', '2'), ('Three', '3')]
    >> atable = tf.TABLE()
    >> for element in data:
    >>     row = tf.TR()
    >>     row.cells = [tf.TD(element[0]), tf.TD(element[1])]
    >>     atable.row = row

    >> more_cells = [tf.TD('Four'), tf.TD('4')]
    >> row = tf.TR()
    >> row.cells = more_cells

    >> atable.row = row

    >> html.body.content.atable = atable
    >> html.body.content.attributes['id'] = 'content_id'

    >> print(html.pretty())


Similar packages
================
    - http://pypi.python.org/pypi/html # Inspiration. It uses __getattr__ trick whereas this package is mostly a __setattr__ tric, aiming sharing of blocks.
    - http://karrigell.sourceforge.net/en/htmltags.html

TODO
====
 - To add more tests
 - A document class ?
