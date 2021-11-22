import json


a = json.dumps({'11':'kffks'})

print(a)

b = json.loads(a)

print(b)
print(b['11'])
print(type(b))