# Building QPanda3D project using pyinstaller
## Disclaimer
When building an executable file using QPanda3D, please be aware of the GPL3 licence implications.


You must understand that the fact that QPanda3D uses PyQt forces us to have a GPL licence as a direct consequence to the GPL contamination. This means that your application is also contaminated with the GPL licence and you are obliged to provide the source code of your application in addition to the executable.

We are aware of the constraints that this licence can cause for some use cases. But it is the rule of licences, take it or leave it.
In next versions of QPanda3D, we will move to Pyside and change the licence to MIT to be more flexible as we do beleive that the library shouldn't impose the licence to be used by the final application. MIT licence ensures that QPanda3D stays opensource and be presented with code source link, but do not impose on the application to be contaminated by this fact. 


This being said. If you accept those conditions, we can build our exe. For the current version, your app will be under GPL licence until we completely move to PySide2 and change the licence to MIT. This means, you should provide a visible link to the users of your app to both your app source code, QPanda3D code, as well as PyQt source code.

## Preparations
PyInstaller is a pain in the a** when it comes to custom libraries or complex ones that embed several layers of imports and other metadata. Developer augasur has asked for help since pyinstaller seems to have trouble dealing with panda3d library. So We decided to add special hook for qpanda3d to help building executables.

If you simply run for example:
```bash
pyinstaller Examples/simple_QPanda3D_example.py
```
Chances are, it will build the executable, but when you try to execute it, it will crush and show this message:
```bash
:display(warning): Unable to load libpandagl.so: Module not found
Known pipe types:
(all display modules loaded.)
Traceback (most recent call last):
  File "simple_QPanda3D_example.py", line 42, in <module>
  File "direct\showbase\ShowBase.py", line 766, in openWindow
  File "direct\showbase\ShowBase.py", line 746, in <lambda>
  File "direct\showbase\ShowBase.py", line 818, in _doOpenWindow
  File "direct\showbase\ShowBase.py", line 647, in makeDefaultPipe
  File "direct\directnotify\Notifier.py", line 130, in error
Exception: No graphics pipe is available!
Your Config.prc file must name at least one valid panda display
library via load-display or aux-display.
```
Obviously something is missing. By default PyInstaller didn't neither copy the etc/ nor the models directories to the project nor did it copy the libpandagl.dll (on windows or libpandagl.so on linux). 

We've added a pyinstaller hook that enables building qpanda3d apps without any trouble.
To use this hook, just use this command instead:
```bash
pyinstaller.exe .\Examples\simple_QPanda3D_example.py --additional-hooks-dir=./pyinstaller_hooks
```

You can also use --windowed to remove the console that apears with the window.
```bash
pyinstaller.exe .\Examples\simple_QPanda3D_example.py --additional-hooks-dir=./pyinstaller_hooks --windowed
```

Enjoy !