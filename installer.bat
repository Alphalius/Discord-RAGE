@echo off
cls
title Installer
:a
pip install pyautogui
pip install webbrowser
pip install time
:x
cls
echo.
set /p x = Installation succesfull, press enter to exit
