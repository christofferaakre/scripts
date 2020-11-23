#SingleInstance force
#Persistent
#InstallKeybdHook

setTitleMatchMode,2
#IfWinActive, RuneLite

`::Send {LButton}
1::Send {LButton}
Up::Send {LButton}
Down::Send {LButton}
Left::Send {LButton}
Right::Send {LButton}
return

!Home::Suspend ; 

#IfWinActive