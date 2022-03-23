@echo off
color 9
echo Iti place de mine?(raspunde cu "da" sau "nu")
set /p love=
if %love% == da goto love
if %love% == nu goto hate
:love
echo -----------------------------
echo Si mie imi place de tine ;)
echo -----------------------------
echo Vreau sa ne intalnim maine. Suna-ma
echo -----------------------------
pause
exit
:hate
echo -----------------------------
echo Bine, pa :(
echo Hehehehehehe
echo -----------------------------
echo Calculatorul tau se ba stinge in 10 secunde
timeout 10
shutdown -s -t 50