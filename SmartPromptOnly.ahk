dir    := "C:\MyStuff\MyEfficiencyTools"
script  = %dir%\CustomPalette.py
; /c closes once done
^!+p::Run, %ComSpec% /c py "%script%"