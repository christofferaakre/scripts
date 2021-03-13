; this script remaps W, A, S, D to Up, Left, Down, Right
; arrow keys in certain user specified prorgams. The default
; is a program I use called 
; ImageGlass, but you can simply edit the line that starts
; #IfWinActive to change which program the script should work in
; Alt + O toggles the script by default, you can change that hotkey
; below 
; Useful if you use any programs where the arrow keys serve a purpose
; but the arrow keys are hard to reach

#SingleInstance force
#Persistent
#InstallKeybdHook

setTitleMatchMode, 2
#IfWinActive, ImageGlass
W::Send {Up}
A::Send {Left}
S::Send {Down}
D::Send {Right}
return

; set hotkey to toggle script
!O::Suspend

#IfWinActive
