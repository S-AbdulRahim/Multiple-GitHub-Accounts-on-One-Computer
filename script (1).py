
# Windows Batch Script
windows_script = '''@echo off
REM Script to setup multiple GitHub accounts on Windows
REM This script configures Git with conditional includes for personal and work accounts

echo ===============================================
echo  Multiple GitHub Accounts Setup Script
echo ===============================================
echo.

REM Get user inputs
set /p PERSONAL_NAME="Enter your PERSONAL GitHub username: "
set /p PERSONAL_EMAIL="Enter your PERSONAL GitHub email: "
set /p PERSONAL_PATH="Enter the full path for PERSONAL projects folder (e.g., C:\\Users\\YourName\\projects\\personal): "

echo.
set /p WORK_NAME="Enter your WORK GitHub username: "
set /p WORK_EMAIL="Enter your WORK GitHub email: "
set /p WORK_PATH="Enter the full path for WORK projects folder (e.g., C:\\Users\\YourName\\projects\\work): "

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
set PERSONAL_PATH_GIT=%PERSONAL_PATH:\\=/%
set WORK_PATH_GIT=%WORK_PATH:\\=/%

REM Create .gitconfig-personal
echo [user] > "%USERPROFILE%\\.gitconfig-personal"
echo     name = %PERSONAL_NAME% >> "%USERPROFILE%\\.gitconfig-personal"
echo     email = %PERSONAL_EMAIL% >> "%USERPROFILE%\\.gitconfig-personal"
echo. >> "%USERPROFILE%\\.gitconfig-personal"
echo [credential] >> "%USERPROFILE%\\.gitconfig-personal"
echo     namespace = personal >> "%USERPROFILE%\\.gitconfig-personal"

echo Created: %USERPROFILE%\\.gitconfig-personal

REM Create .gitconfig-work
echo [user] > "%USERPROFILE%\\.gitconfig-work"
echo     name = %WORK_NAME% >> "%USERPROFILE%\\.gitconfig-work"
echo     email = %WORK_EMAIL% >> "%USERPROFILE%\\.gitconfig-work"
echo. >> "%USERPROFILE%\\.gitconfig-work"
echo [credential] >> "%USERPROFILE%\\.gitconfig-work"
echo     namespace = work >> "%USERPROFILE%\\.gitconfig-work"

echo Created: %USERPROFILE%\\.gitconfig-work

echo.
echo ===============================================
echo  Updating global Git configuration...
echo ===============================================

REM Backup existing .gitconfig
if exist "%USERPROFILE%\\.gitconfig" (
    copy "%USERPROFILE%\\.gitconfig" "%USERPROFILE%\\.gitconfig.backup" >nul
    echo Backed up existing .gitconfig to .gitconfig.backup
)

REM Add conditional includes to .gitconfig
echo. >> "%USERPROFILE%\\.gitconfig"
echo [includeIf "gitdir:%PERSONAL_PATH_GIT%/"] >> "%USERPROFILE%\\.gitconfig"
echo     path = ~/.gitconfig-personal >> "%USERPROFILE%\\.gitconfig"
echo. >> "%USERPROFILE%\\.gitconfig"
echo [includeIf "gitdir:%WORK_PATH_GIT%/"] >> "%USERPROFILE%\\.gitconfig"
echo     path = ~/.gitconfig-work >> "%USERPROFILE%\\.gitconfig"

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
'''

# Linux/macOS Bash Script
unix_script = '''#!/bin/bash

# Script to setup multiple GitHub accounts on Linux/macOS
# This script configures Git with conditional includes for personal and work accounts

echo "==============================================="
echo " Multiple GitHub Accounts Setup Script"
echo "==============================================="
echo ""

# Get user inputs
read -p "Enter your PERSONAL GitHub username: " PERSONAL_NAME
read -p "Enter your PERSONAL GitHub email: " PERSONAL_EMAIL
read -p "Enter the full path for PERSONAL projects folder (e.g., $HOME/projects/personal): " PERSONAL_PATH

echo ""
read -p "Enter your WORK GitHub username: " WORK_NAME
read -p "Enter your WORK GitHub email: " WORK_EMAIL
read -p "Enter the full path for WORK projects folder (e.g., $HOME/projects/work): " WORK_PATH

echo ""
echo "==============================================="
echo " Creating project directories..."
echo "==============================================="

# Expand tilde to home directory
PERSONAL_PATH="${PERSONAL_PATH/#\\~/$HOME}"
WORK_PATH="${WORK_PATH/#\\~/$HOME}"

# Create directories if they don't exist
if [ ! -d "$PERSONAL_PATH" ]; then
    mkdir -p "$PERSONAL_PATH"
    echo "Created: $PERSONAL_PATH"
else
    echo "Already exists: $PERSONAL_PATH"
fi

if [ ! -d "$WORK_PATH" ]; then
    mkdir -p "$WORK_PATH"
    echo "Created: $WORK_PATH"
else
    echo "Already exists: $WORK_PATH"
fi

echo ""
echo "==============================================="
echo " Creating Git configuration files..."
echo "==============================================="

# Create .gitconfig-personal
cat > "$HOME/.gitconfig-personal" << EOF
[user]
    name = $PERSONAL_NAME
    email = $PERSONAL_EMAIL

[credential]
    namespace = personal
EOF

echo "Created: $HOME/.gitconfig-personal"

# Create .gitconfig-work
cat > "$HOME/.gitconfig-work" << EOF
[user]
    name = $WORK_NAME
    email = $WORK_EMAIL

[credential]
    namespace = work
EOF

echo "Created: $HOME/.gitconfig-work"

echo ""
echo "==============================================="
echo " Updating global Git configuration..."
echo "==============================================="

# Backup existing .gitconfig
if [ -f "$HOME/.gitconfig" ]; then
    cp "$HOME/.gitconfig" "$HOME/.gitconfig.backup"
    echo "Backed up existing .gitconfig to .gitconfig.backup"
else
    touch "$HOME/.gitconfig"
fi

# Check if conditional includes already exist
if grep -q "includeIf.*gitdir:$PERSONAL_PATH" "$HOME/.gitconfig" 2>/dev/null; then
    echo "Personal configuration already exists in .gitconfig"
else
    # Add conditional includes to .gitconfig
    cat >> "$HOME/.gitconfig" << EOF

[includeIf "gitdir:$PERSONAL_PATH/"]
    path = ~/.gitconfig-personal
EOF
    echo "Added personal account configuration"
fi

if grep -q "includeIf.*gitdir:$WORK_PATH" "$HOME/.gitconfig" 2>/dev/null; then
    echo "Work configuration already exists in .gitconfig"
else
    cat >> "$HOME/.gitconfig" << EOF

[includeIf "gitdir:$WORK_PATH/"]
    path = ~/.gitconfig-work
EOF
    echo "Added work account configuration"
fi

echo ""
echo "==============================================="
echo " Setup Complete!"
echo "==============================================="
echo ""
echo "Configuration Summary:"
echo "---------------------"
echo "Personal Account:"
echo "  Name: $PERSONAL_NAME"
echo "  Email: $PERSONAL_EMAIL"
echo "  Folder: $PERSONAL_PATH"
echo "  Namespace: personal"
echo ""
echo "Work Account:"
echo "  Name: $WORK_NAME"
echo "  Email: $WORK_EMAIL"
echo "  Folder: $WORK_PATH"
echo "  Namespace: work"
echo ""
echo "==============================================="
echo " Next Steps:"
echo "==============================================="
echo ""
echo "1. Clear old GitHub credentials (if using HTTPS):"
echo "   - macOS: Use Keychain Access and search for 'github.com'"
echo "   - Linux: Run 'git credential-cache exit' or check ~/.git-credentials"
echo ""
echo "2. Clone or move your repos to the appropriate folders:"
echo "   - Personal repos go in: $PERSONAL_PATH"
echo "   - Work repos go in: $WORK_PATH"
echo ""
echo "3. When you push/pull for the first time, you'll be prompted to"
echo "   authenticate with GitHub. Make sure to use the correct account!"
echo ""
echo "4. Verify your setup by running these commands in each folder:"
echo "   cd $PERSONAL_PATH"
echo "   git config user.email"
echo "   git config credential.namespace"
echo ""
echo "==============================================="
'''

# Save Windows script
with open('setup_multiple_github_accounts.bat', 'w', encoding='utf-8') as f:
    f.write(windows_script)

# Save Linux/macOS script
with open('setup_multiple_github_accounts.sh', 'w', encoding='utf-8') as f:
    f.write(unix_script)

print("✅ Scripts created successfully!\n")
print("Files created:")
print("1. setup_multiple_github_accounts.bat (Windows)")
print("2. setup_multiple_github_accounts.sh (Linux/macOS)")
print("\n" + "="*60)
print("HOW TO USE:")
print("="*60)
print("\n📁 WINDOWS:")
print("   - Double-click 'setup_multiple_github_accounts.bat'")
print("   - Or run: setup_multiple_github_accounts.bat")
print("\n🐧 LINUX / 🍎 macOS:")
print("   - Make it executable: chmod +x setup_multiple_github_accounts.sh")
print("   - Run: ./setup_multiple_github_accounts.sh")
print("   - Or run: bash setup_multiple_github_accounts.sh")
print("\n" + "="*60)
