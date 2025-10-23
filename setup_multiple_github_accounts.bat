@echo off
REM Script to setup multiple GitHub accounts on Windows
REM This script configures Git with conditional includes for personal and work accounts

echo ===============================================
echo  Multiple GitHub Accounts Setup Script
echo ===============================================
echo.

REM Get user inputs
set /p PERSONAL_NAME="Enter your PERSONAL GitHub username: "
set /p PERSONAL_EMAIL="Enter your PERSONAL GitHub email: "
set /p PERSONAL_PATH="Enter the full path for PERSONAL projects folder (e.g., C:\Users\YourName\projects\personal): "

echo.
set /p WORK_NAME="Enter your WORK GitHub username: "
set /p WORK_EMAIL="Enter your WORK GitHub email: "
set /p WORK_PATH="Enter the full path for WORK projects folder (e.g., C:\Users\YourName\projects\work): "

echo.
echo ===============================================
echo  Creating project directories...
echo ===============================================

REM Create directories if they don't exist
if not exist "%PERSONAL_PATH%" (
    mkdir "%PERSONAL_PATH%"
    echo Created: %PERSONAL_PATH%
) else (
    echo Already exists: %PERSONAL_PATH%
)

if not exist "%WORK_PATH%" (
    mkdir "%WORK_PATH%"
    echo Created: %WORK_PATH%
) else (
    echo Already exists: %WORK_PATH%
)

echo.
echo ===============================================
echo  Creating Git configuration files...
echo ===============================================

REM Convert Windows paths to Git-compatible format (forward slashes)
set PERSONAL_PATH_GIT=%PERSONAL_PATH:\=/%
set WORK_PATH_GIT=%WORK_PATH:\=/%

REM Create .gitconfig-personal
echo [user] > "%USERPROFILE%\.gitconfig-personal"
echo     name = %PERSONAL_NAME% >> "%USERPROFILE%\.gitconfig-personal"
echo     email = %PERSONAL_EMAIL% >> "%USERPROFILE%\.gitconfig-personal"
echo. >> "%USERPROFILE%\.gitconfig-personal"
echo [credential] >> "%USERPROFILE%\.gitconfig-personal"
echo     namespace = personal >> "%USERPROFILE%\.gitconfig-personal"

echo Created: %USERPROFILE%\.gitconfig-personal

REM Create .gitconfig-work
echo [user] > "%USERPROFILE%\.gitconfig-work"
echo     name = %WORK_NAME% >> "%USERPROFILE%\.gitconfig-work"
echo     email = %WORK_EMAIL% >> "%USERPROFILE%\.gitconfig-work"
echo. >> "%USERPROFILE%\.gitconfig-work"
echo [credential] >> "%USERPROFILE%\.gitconfig-work"
echo     namespace = work >> "%USERPROFILE%\.gitconfig-work"

echo Created: %USERPROFILE%\.gitconfig-work

echo.
echo ===============================================
echo  Updating global Git configuration...
echo ===============================================

REM Backup existing .gitconfig
if exist "%USERPROFILE%\.gitconfig" (
    copy "%USERPROFILE%\.gitconfig" "%USERPROFILE%\.gitconfig.backup" >nul
    echo Backed up existing .gitconfig to .gitconfig.backup
)

REM Add conditional includes to .gitconfig
echo. >> "%USERPROFILE%\.gitconfig"
echo [includeIf "gitdir:%PERSONAL_PATH_GIT%/"] >> "%USERPROFILE%\.gitconfig"
echo     path = ~/.gitconfig-personal >> "%USERPROFILE%\.gitconfig"
echo. >> "%USERPROFILE%\.gitconfig"
echo [includeIf "gitdir:%WORK_PATH_GIT%/"] >> "%USERPROFILE%\.gitconfig"
echo     path = ~/.gitconfig-work >> "%USERPROFILE%\.gitconfig"

echo Updated global .gitconfig with conditional includes

echo.
echo ===============================================
echo  Setup Complete!
echo ===============================================
echo.
echo Configuration Summary:
echo ---------------------
echo Personal Account:
echo   Name: %PERSONAL_NAME%
echo   Email: %PERSONAL_EMAIL%
echo   Folder: %PERSONAL_PATH%
echo   Namespace: personal
echo.
echo Work Account:
echo   Name: %WORK_NAME%
echo   Email: %WORK_EMAIL%
echo   Folder: %WORK_PATH%
echo   Namespace: work
echo.
echo ===============================================
echo  Next Steps:
echo ===============================================
echo.
echo 1. Clear old GitHub credentials from Windows Credential Manager:
echo    - Press Win + R, type "control", press Enter
echo    - Go to User Accounts ^> Credential Manager ^> Windows Credentials
echo    - Remove any "git:https://github.com" entries
echo.
echo 2. Clone or move your repos to the appropriate folders:
echo    - Personal repos go in: %PERSONAL_PATH%
echo    - Work repos go in: %WORK_PATH%
echo.
echo 3. When you push/pull for the first time, you'll be prompted to
echo    authenticate with GitHub. Make sure to use the correct account!
echo.
echo 4. Verify your setup by running these commands in each folder:
echo    cd "%PERSONAL_PATH%"
echo    git config user.email
echo    git config credential.namespace
echo.
echo ===============================================
pause
