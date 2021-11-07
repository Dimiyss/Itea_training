import shutil


# shutil.copyfileobj()
# print(shutil.copyfile('./fs.py', './new_fs.py'))
# shutil.copymode()
# shutil.copystat('./new_fs.py', './fs.py')
# shutil.copy()
# shutil.copy2()

def f_ignore(current_path, contents):
    ignore_obj = []
    for path in contents:
        if path.startswith('_'):
            ignore_obj.append(path)
    return ignore_obj


shutil.copytree('./new_fs.py', './fs.py', ignore=f_ignore)
