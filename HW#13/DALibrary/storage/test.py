from jinja2 import Template

INSERT_TEMPLATE = Template("""insert into {{ table_name }} values {{ insert_list }}""")
SELECT_TEMPLATE = Template("""select {{ field_list }} from {{ table_name }} where {{ condition }}""")
BOOK_VALUES = Template("""({{ title }}, {{ author }}, {{ published_year }}, {{ genre }}, {{ reader_id }})""")

dict = {
    'title': 'Book #1',
    'author': 'Author #1',
    'published_year': 2021,
    'genre': 'Doc',
    'reader_id': 222
}

print(BOOK_VALUES.render(dict))

dict_1 = {
    'title': 'Book #1',
    'author': 'Author #1',
    'published_year': 2021,
    'genre': 'Doc'
}

if not dict_1.get('reader_id'):
    print('Added null')
    dict_1['reader_id'] = 'null'

print(BOOK_VALUES.render(dict_1))

insrt_val_list = ['dsddssds', 'uuuuuu']
insrt_val = ','.join(insrt_val_list)

print(insrt_val)