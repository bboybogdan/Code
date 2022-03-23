@echo off
color 9
echo Ma iubesti?(raspunde cu "da" sau "nu")
set /p love=
if %love% == da goto love
if %love% == nu goto hate
:love
echo -----------------------------
echo Si eu te iubesc
echo -----------------------------
echo Maimutica mea 
echo -----------------------------
echo PS Tb sa fie si niste inimioare dar nu se poate pentru ca programarea n are emotii :)))
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