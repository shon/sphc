import timeit

# Common data for the templates
table_data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10} for _ in range(100)]

def run_sphc():
    from sphc import tf
    table = tf.TABLE()
    for row_data in table_data:
        row = tf.TR()
        row.cells = [tf.TD(str(row_data[key])) for key in sorted(row_data.keys())]
        table.row = row
    return str(table)

def run_jinja2():
    from jinja2 import Environment
    env = Environment()
    template = env.from_string("""
        <table>
            {% for row in table_data %}
            <tr>
                {% for key in row.keys()|sort %}
                <td>{{ row[key] }}</td>
                {% endfor %}
            </tr>
            {% endfor %}
        </table>
    """)
    return template.render(table_data=table_data)

def run_mako():
    from mako.template import Template
    template = Template("""
        <table>
            % for row in table_data:
            <tr>
                % for key in sorted(row.keys()):
                <td>${row[key]}</td>
                % endfor
            </tr>
            % endfor
        </table>
    """)
    return template.render(table_data=table_data)

def run_bottle():
    from bottle import SimpleTemplate
    template = SimpleTemplate("""
        <table>
            % for row in table_data:
            <tr>
                % for key in sorted(row.keys()):
                <td>{{row[key]}}</td>
                % end
            </tr>
            % end
        </table>
    """)
    return template.render(table_data=table_data)

if __name__ == '__main__':
    # Increase the number for more accurate results
    number = 1000

    print("Running benchmarks...")
    print("Number of iterations:", number)

    # Measure execution time for each template engine
    sphc_time = timeit.timeit(run_sphc, number=number)
    jinja2_time = timeit.timeit(run_jinja2, number=number)
    mako_time = timeit.timeit(run_mako, number=number)
    bottle_time = timeit.timeit(run_bottle, number=number)

    print("\nResults (lower is better):")
    print("sphc:   ", sphc_time)
    print("Jinja2: ", jinja2_time)
    print("Mako:   ", mako_time)
    print("Bottle: ", bottle_time)
