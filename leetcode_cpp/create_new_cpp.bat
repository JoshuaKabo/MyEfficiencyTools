@echo off
set filename=%1

@REM check if the command line arg wasn't provided
if "%filename%"=="" (
    set /p filename=Enter the name of the file:
)

copy template.cpp %filename%.cpp