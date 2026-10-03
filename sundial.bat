@echo off
setlocal EnableExtensions DisableDelayedExpansion
rem =======================================================================
rem  sundial.bat  --  double-click to open the simulator (sundial.py)
rem
rem  * Keep this file in the SAME folder as sundial.py.  It opens the .py
rem    that has its own name (sundial.bat -> sundial.py), falling back to
rem    sundial.py, so a renamed pair such as xyz.bat + xyz.py also works.
rem  * The program opens in its own window with NO black console behind
rem    it.  This console only stays on screen when something is wrong
rem    (Python / tkinter missing, or the .py missing).  If the program
rem    itself fails while starting, a message box shows the Python error
rem    instead of "nothing happens".
rem  * Python used: "python" first (the one you get when you type python
rem    in a terminal, so optional extras such as skyfield are picked up),
rem    then the "py" launcher.  The Microsoft Store placeholder python
rem    fails the test and is skipped, so it never opens the Store.
rem  * From a terminal:
rem        sundial.bat --selftest   numeric self-test, output in console
rem        sundial.bat console      GUI, but keep the console for errors
rem  * Writes nothing into this folder (no log file, no __pycache__).
rem =======================================================================
title %~n0
pushd "%~dp0"

rem ---- which .py to open -------------------------------------------------
set "APP=%~n0.py"
if not exist "%APP%" set "APP=sundial.py"
if exist "%APP%" goto :find_python
echo.
echo  [ERROR] Cannot find %APP% in this folder:
echo          %~dp0
if /i not "%~n0"=="sundial" echo  It also looked for %~n0.py there.
echo  Keep this .bat in the same folder as sundial.py.
goto :fail

:find_python
rem ---- a Python 3.8+ that has tkinter --------------------------------------
rem  "if not errorlevel 1 if errorlevel 0" = exit code exactly 0, so a
rem  missing command (9009) or a crashing interpreter (negative) is rejected.
set "PY="
set "CHECK=import sys, tkinter; sys.exit(0 if sys.version_info >= (3, 8) else 1)"
python -c "%CHECK%" >nul 2>&1
if not errorlevel 1 if errorlevel 0 set "PY=python"
if defined PY goto :have_python
py -3 -c "%CHECK%" >nul 2>&1
if not errorlevel 1 if errorlevel 0 set "PY=py -3"
if defined PY goto :have_python

rem ---- nothing usable: say which problem it is ----------------------------
set "ANYPY="
python -c "import sys" >nul 2>&1
if not errorlevel 1 if errorlevel 0 set "ANYPY=1"
py -3 -c "import sys" >nul 2>&1
if not errorlevel 1 if errorlevel 0 set "ANYPY=1"
echo.
if defined ANYPY goto :no_tk
echo  [ERROR] Python 3 was not found on this computer.
echo  Install it from  https://www.python.org/downloads/
echo  In the installer tick "Add python.exe to PATH" and keep the
echo  "tcl/tk and IDLE" option switched on.
goto :fail

:no_tk
echo  [ERROR] Python was found, but it cannot run this program:
echo  it is older than 3.8, or it was installed without tcl/tk (tkinter).
echo  Fix: run the Python installer again, choose "Modify", and tick
echo  "tcl/tk and IDLE".
goto :fail

:have_python
rem ---- pythonw.exe = the windowless twin of that very interpreter ---------
set "PYW="
for /f "usebackq delims=" %%W in (`%PY% -c "import os, sys; print(os.path.join(os.path.dirname(sys.executable), 'pythonw.exe'))"`) do set "PYW=%%W"
if defined PYW if not exist "%PYW%" set "PYW="

rem ---- any argument, or no pythonw: run inside this console --------------
if not "%~1"=="" goto :console
if not defined PYW goto :console

rem ---- normal double-click: windowless ------------------------------------
rem  pythonw has no console, so a failure would otherwise be silent.  This
rem  small launcher runs the .py exactly as "python sundial.py" would, but
rem    - any error while starting -> message box with the Python traceback;
rem    - the script ends without ever opening a window (e.g. a half-saved
rem      .py whose last lines are missing) -> message box saying so.
set "B=import sys, runpy, traceback, ctypes, tkinter"
set "B=%B%; box = lambda text, icon: ctypes.windll.user32.MessageBoxW(0, text[-3000:], sys.argv[0] + ' - cannot start', icon)"
set "B=%B%; sys.excepthook = lambda t, v, tb: box(''.join(traceback.format_exception(t, v, tb)), 0x10)"
set "B=%B%; opened = []; tk_init = tkinter.Tk.__init__"
set "B=%B%; tkinter.Tk.__init__ = lambda self, *a, **k: (opened.append(1), tk_init(self, *a, **k))[1]"
set "B=%B%; sys.argv = sys.argv[1:]; runpy.run_path(sys.argv[0], run_name='__main__')"
set "B=%B%; opened or box('The program ended without opening its window. The .py file may be incomplete or damaged - save a fresh copy.', 0x30)"
start "" "%PYW%" -c "%B%" "%APP%"
exit /b 0

:console
%PY% "%APP%" %*
echo.
pause
exit /b

:fail
echo.
pause
exit /b 1
