#!/bin/bash

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
PERSONAL_PATH="${PERSONAL_PATH/#\~/$HOME}"
WORK_PATH="${WORK_PATH/#\~/$HOME}"

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
