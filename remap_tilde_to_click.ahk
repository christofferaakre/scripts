; this script remaps the tilde click as well as some other
; keys to left mouse button in a program, you can change
; which programs below on the line that starts #IfWinActive
; Alt + Home toggles the script by default, this hotkey
; can be changed below

#SingleInstance force
#Persistent
#InstallKeybdHook

setTitleMatchMode,2
; specify which program the script should be active in
#IfWinActive, RuneLite

`::Send {LButton}
1::Send {LButton}
Up::Send {LButton}
Down::Send {LButton}
Left::Send {LButton}
Right::Send {LButton}
return

; set hotkey to toggle script
!Home::Suspend ; 
