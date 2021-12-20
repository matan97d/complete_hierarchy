@echo off
echo %1 %2
start /b frida -U "%1" -l "complete_class_hierarchy.js" -> %2
python Kill_Frida.py %2
python Results_Filter.py %2 filter some other filter

