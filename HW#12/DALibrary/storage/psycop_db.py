import psycopg2
from contextlib import closing

from psycopg2.extras import DictCursor, NamedTupleCursor


with closing(psycopg2.connect(dbname='postgres',
                              user='postgres',
                              password='pgpwd4habr',
                              host='localhost',
                              port='5432')) as conn:
    conn.autocommit = True

    with conn.cursor(cursor_factory=NamedTupleCursor) as cursor:
        cursor.execute('create table if not exists books('
                       'id int4 not null, '
                       'title text notnull,'
                       'author text notnull,'
                       'published_date notnull,'
                       'genre text notnull,'
                       'reader_id int'
                       'primary key("id"))')


