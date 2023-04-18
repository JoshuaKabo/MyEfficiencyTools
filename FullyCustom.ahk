#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
#Warn  ; Recommended for catching common errors.
SetCapsLockState, AlwaysOff

WinState := GetKeyState("#")
if (WinState)
    Gui, Add, Text,, Some text to display.
    return

; disable the original keys
; Up::return
; Down::return
; Left::return
; Right::return

; Home::return
; PgDn::return
; End::return
; PgUp::return

; Del::return

; TODO: disable windows lock by traditional input

; ------------- enable new behavior -------------

; 
;   i     =>       up
; j k l   =>  left dwn right
; 
CapsLock & j::Send, {blind}{Left}
CapsLock & k::Send, {blind}{Down}
CapsLock & l::Send, {blind}{Right}
CapsLock & i::Send, {blind}{Up}

; H ===> Backspace
CapsLock & h::Send, {blind}{Backspace}
; T ===> Backspace
CapsLock & t::Send, {blind}{Backspace}

; 
; esdf hasn't worked out for me. The problem isn't muscle memory, it's modifier keys!
; full control of caps + shift + ctrl with the pinky becomes impossible when the rest
; the hand is in home row position
;   w     =>       pgup
; a s d   =>  home pgdwn end
; 
CapsLock & a::Send, {blind}{Home}
CapsLock & s::Send, {blind}{PgDn}
CapsLock & d::Send, {blind}{End}
CapsLock & w::Send, {blind}{PgUp}

; C ===> True Capslock
CapsLock & c::Send, {blind}{CapsLock}

; G ===> Delete
CapsLock & g::Send, {blind}{Del}

; R ===> Return
CapsLock & r::Send, {blind}{Enter}

; e ===> Escape
CapsLock & e::Send, {blind}{Esc}

; Caps + 1-(=/+ key) => function keys
CapsLock & 1::Send, {blind}{F1}
CapsLock & 2::Send, {blind}{F2}
CapsLock & 3::Send, {blind}{F3}
CapsLock & 4::Send, {blind}{F4}
CapsLock & 5::Send, {blind}{F5}
CapsLock & 6::Send, {blind}{F6}
CapsLock & 7::Send, {blind}{F7}
CapsLock & 8::Send, {blind}{F8}
CapsLock & 9::Send, {blind}{F9}
CapsLock & 0::Send, {blind}{F10}
CapsLock & -::Send, {blind}{F11}
CapsLock & =::Send, {blind}{F12}

; TODO: caps + q for toggle function layer
; TODO: caps + z? for swap ijkl and wasd
; consider swapping alt and caps?? So alt now triggers the alternate layer...
; consider swapping wasd and ijkl??