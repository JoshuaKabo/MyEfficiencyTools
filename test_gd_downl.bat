@REM curl -s "https://api.github.com/repos/godotengine/godot/releases/latest" | findstr "https://github.com/godotengine/godot/releases/download/*.-stable/Godot_v*.-stable_mono_win64.zip" | 
@REM "https://api.github.com/repos/godotengine/godot/releases/tag/4.2.2-stable" 


@REM repo id for godot: 15634981
@REM https://api.github.com/repos/godotengine/godot/releases

@echo off
setlocal enabledelayedexpansion
set repo=godotengine/godot
for /f "tokens=1,* delims=:" %%A in ('curl -ks https://api.github.com/repos/%repo%/releases/latest ^| find "browser_download_url"') do (
    call :download "%%B"
)
goto :eof

:download
set "url=%~1"
for %%i in (%url%) do set "filename=%%~nxi"
if "%filename:~-9%"=="-x64.exe" (
    curl -kOL %url%
)
goto :eof