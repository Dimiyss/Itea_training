#
import os
print(os.name)

# os.mkdir('./test_folder')
# os.rmdir('./test_folder')
# os.rename()
# os.remove()

# print(os.path.exists('./fs.py'))
# print(os.path.isdir('./fs.py'))
# print(os.path.isfile('./fs.py'))


# print(os.listdir('../'))
for _path in os.listdir('../'):
    if os.path.isfile('../' + _path):
        print(_path)