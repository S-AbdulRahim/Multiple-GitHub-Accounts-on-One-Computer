# Setting Up Multiple GitHub Accounts on One Computer

A comprehensive guide to configure and use multiple GitHub accounts (personal and work) on the same machine using HTTPS authentication with credential namespaces.

---

## Table of Contents
- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Quick Setup (Using Scripts)](#quick-setup-using-scripts)
- [Manual Setup Instructions](#manual-setup-instructions)
- [Verification](#verification)
- [Troubleshooting](#troubleshooting)
- [FAQ](#faq)

---

## Overview

This guide helps you configure Git to automatically use the correct GitHub credentials based on the project folder you're working in. No more authentication errors or pushing to the wrong account!

**What you'll achieve:**
- Automatic account switching based on folder location
- Separate credentials for personal and work accounts
- No need to manually configure each repository
- Works with HTTPS (no SSH keys required)

---

## Prerequisites

Before starting, ensure you have:
- Git installed on your system
- Two GitHub accounts (personal and work/organization)
- Basic familiarity with command line/terminal

---

## Quick Setup (Using Scripts)

The fastest way to set up multiple GitHub accounts is using our automated scripts.

### Windows

1. Download `setup_multiple_github_accounts.bat`
2. Double-click the file or run from Command Prompt:
     setup_multiple_github_accounts.bat
3. Follow the prompts to enter your information

### Linux / macOS

1. Download `setup_multiple_github_accounts.sh`
2. Make it executable and run:
    chmod +x setup_multiple_github_accounts.sh
    ./setup_multiple_github_accounts.sh
3. Follow the prompts to enter your information

### What the Script Will Ask

- **Personal GitHub username** (e.g., `john-doe`)
- **Personal GitHub email** (e.g., `john@personal.com`)
- **Personal projects folder path** (e.g., `C:\Users\John\projects\personal` or `~/projects/personal`)
- **Work GitHub username** (e.g., `john-company`)
- **Work GitHub email** (e.g., `john@company.com`)
- **Work projects folder path** (e.g., `C:\Users\John\projects\work` or `~/projects/work`)

---

**Important Notes:**
- Use forward slashes `/` even on Windows
- Include the trailing slash `/` at the end of the path
- Paths are case-sensitive on Linux/macOS
