# FOR PYTHON < 3.3
# for WINDOWS
# pip install virtualenv
# pip install virtualenvwrapper-win

# LINUX and iOS
# pip install virtualenv
# pip install virtualenvwrapper


# COMMAND
# mkvirtualenv *envNAME*        - создать новое окружение
# workon                        - вывести список виртуальных окружений
# workon *envNAME*              - переключится на определенное виртуальное окружение
# deactivate                    - выход из виртуального окружение
# rmvirtualenv *envNAME*        - удаляет указанное окружение




import numpy as np

z = np.zeros(10)
print(z)
print(type(z))