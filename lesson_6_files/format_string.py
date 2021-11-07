name = 'Ivan'
age = 30


# print('I\'m ' + name + '. ' + str(age) + ' years')

# var 1 - %
print('I\'m %s. %d years' % (name, age))

errno = 50159747054
print('%x' % errno)

print('I\'m %(name)s. %(age)d years. %(age)d' % {
    "name": name,
    "age": age
})


# var 2 - format
print('I\'m {}. {} years'.format(name, age))

print('Hey {s_name}, there is a {s_errno:*^20x}!'.format(s_name=name, s_errno=errno))

# var 3 - f-string
print(f'Hey {name}, there is a {errno:*^20x}! {{{name}}}')

# var 4 - template
from string import Template

t = Template('Hey $name, there is a $errno!')

print(t.substitute(name=name, errno=hex(errno)))


sqlSelectQuery = Template('select * from $table_name')
print(sqlSelectQuery.substitute(table_name='users'))