

# QT CORE
# Change for PySide Or PyQt
# ///////////////////////// WARNING: ////////////////////////////
# Remember that changing to PyQt too many modules will have 
# problems because some classes have different names like: 
# Property (pyqtProperty), Slot (pyqtSlot), Signal (pyqtSignal)
# among others.
# ///////////////////////////////////////////////////////////////
import pyperclip
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtSvgWidgets import *
import os, sys


def install():
    os.system(
        'python.exe -m pip install --upgrade pip --user --trusted-host pypi.org --trusted-host files.pythonhosted.org')
    os.system(
        'python.exe -m pip install webbrowser --user --trusted-host pypi.org --trusted-host files.pythonhosted.org')
    os.system('python.exe -m pip install pyside6 --user --trusted-host pypi.org --trusted-host files.pythonhosted.org')
    os.system(
        'python.exe -m pip install pyperclip --user --trusted-host pypi.org --trusted-host files.pythonhosted.org')


key = 's94546'
result = os.getlogin()
print(result)
if result == "arjun":
    print(key, "found su")
elif result == '2019asharma':
    print(key, "found su")
elif result == '2019jdandison':
    print(key, "found su")

elif result == 'admin':
    print('get a life')
else:
    print(result, "No key")
    exit(123)
