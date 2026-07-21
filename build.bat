@echo off
REM ============================================================
REM  CathLab Manager v1.0 - Script de build Windows (un clic)
REM  Prerequis : Python 3.13 installe (case "Add to PATH" cochee)
REM  Le programme compile est depose DIRECTEMENT dans ce dossier,
REM  a cote de build.bat (pas de sous-dossier dist/ a chercher).
REM ============================================================

cd /d "%~dp0"

echo [1/4] Creation de l'environnement virtuel...
python -m venv venv
call venv\Scripts\activate.bat

echo [2/4] Installation des dependances...
pip install --upgrade pip
pip install -r requirements.txt
pip install pyinstaller

echo [3/4] Compilation en cours (peut prendre quelques minutes)...
REM --distpath "%~dp0" = dossier ou se trouve build.bat lui-meme
pyinstaller build.spec --noconfirm --distpath "%~dp0" --workpath "%~dp0build_temp"

echo [4/4] Termine !
echo.
echo Le programme se trouve juste ici, dans ce meme dossier :
echo   %~dp0CathLabManager\CathLabManager.exe
echo.
echo Regarde dans le dossier CathLabManager qui vient d'apparaitre
echo a cote de build.bat.
echo.
pause
