#!G:\python27\python.exe
from distutils.core import setup
import py2exe

setup(
    console=['main.py'],
    options={
        'py2exe':{
            'packages':['PyQt5', 'numpy', 'cv2', 'pyttsx', 'autocomplete', 'winsound']
        }
    }
)
