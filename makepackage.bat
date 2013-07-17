@echo off
7z a -tzip -x!makepackage.bat -x!.git -x!*.sublime-project -x!*.sublime-workspace "Solarized Toggle.sublime-package" *
