@echo off
echo %1
frida -U "%1" -l "complete_class_method_hierarchy.js" -> CBSclassesMethods.txt

