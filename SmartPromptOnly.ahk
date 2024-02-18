dir    := "C:\Users\joshk\dev\Tools\MyEfficiencyTools"
script  = %dir%\CustomPalette.py
; /c closes once done
^!+p::Run, %ComSpec% /c py "%script%"