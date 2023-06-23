# PassBlast

You input text into a field and click 'blast'. The app counts-down from 3, and then blasts that text out of your keyboard controller as if you were typing it.

Handy for getting past UAC or login windows that do not allow copy/paste (especially when using RDP/Teamviewer/providing remote support).

## Requirements

The [App](App/) folder contains a packaged version of this app called `PassBlast.exe`

Just run the .exe! It's self-contained and fully portable (take it out of the repo if you want).

There is also an older version of the app I made as an experiment with the `customtkinter` library. You can find that if you like in [Legacy](Legacy/)

## Source Code:

If you want to build the app from the [source code](Source/), you will need:
```
pip install pynput
```
and if you want to build the legacy version that used `customtkinter`:
```
pip install customtkinter
```
