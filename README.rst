Simple Pythonic HTML Creator
============================

 - *Very alpha yet* but works
 - Only on Python3/ 2.x
 - To add more tests

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


TODO
====
 - escape support
