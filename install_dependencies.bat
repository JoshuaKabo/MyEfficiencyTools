@REM elevates to admin and installs the python dependencies necessary
powershell -command "Start-Process cmd -ArgumentList '/c cd /d %CD% && pip install -r requirements.txt' -Verb runas"