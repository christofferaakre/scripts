; This script will remap the capslock key to ESC,
; this is very useful for anyone who uses the ESC key regularly,
; for example people who use vim, as the ESC is hard to reach
; Toggle the script on and off with Ctrl + End on your keyboard
#SingleInstance force
#Persistent
#InstallKeybdHook

setTitleMatchMode,2
CAPSLOCK::ESC
return

; Set hotkey to toggle script
!End::Suspend ; 

#IfWinActive
