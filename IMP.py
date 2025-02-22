# -*- coding: utf-8 -*-

# A simple setup script to create an executable using Tkinter. This also
# demonstrates the method for creating a Windows executable that does not have
# an associated console.
#
# SimpleTkApp.py is a very simple type of Tkinter application
#
# Run the build process by running the command 'python setup.py build'
#
# If everything works well you should find a subdirectory in the build
# subdirectory that contains the files needed to run the application

import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

executables = [
    Executable('Server.py', base=base, icon = "S.ico")
]

setup(name='Simple HTTP Server',
      version='0.1',
      description='Shares the content in the same network ',
      #options={"build_exe":{"packages":["Encryptor"],"include_files":['download.jpg']},
      executables=executables
      )
