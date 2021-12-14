from jinja2 import Template

CREATE_BOOK_TABLE = """create table if not exists book(
                       id serial not null,
                       title text not null,
                       author text not null,
                       published_year int2 not null,
                       genre text not null,
                       reader_id int4,
                       primary key("id"))
                       """
CREATE_READER_TABLE = """create table if not exists reader(
                         id serial not null,
                         first_name text not null,
                         second_name text not null,
                         age int2 not null,
                         is_active bool not null,
                         primary key("id"))
                         """
BOOK_COLUMNS = '(title, author, published_year, genre, reader_id)'
READER_COLUMNS = '(first_name, second_name, age, is_active)'
INSERT_TEMPLATE = Template("""insert into {{ table_name }} {{ columns }} values {{ insert_values }}""")
SELECT_TEMPLATE = Template("""select {{ field_list }} from {{ table_name }} where {{ condition }}""")
BOOK_VALUES = Template("""('{{ title }}', '{{ author }}', {{ published_year }}, '{{ genre }}', {{ reader_id }})""")
READER_VALUES = Template("""('{{ first_name }}', '{{ second_name }}', {{ age }}, {{ is_active }})""")
UPDATE_TEMPLATE = Template("""update book set reader_id = {{ reader_id }} where id = {{ book_id }}""")
DELETE_TEMPLATE = Template("""delete from {{ table_name }} where {{ condition }}""")