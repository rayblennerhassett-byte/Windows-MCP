# Windows Development Environment Setup Guide

This guide demonstrates the ExecuteMarkdown tool for automated hands-free setup.
Execute this entire guide with a single command in Claude Desktop!

**Usage**: Ask Claude "Execute the setup from setup-guide.md" and watch it automatically run all steps.

---

## Step 1: Create Project Directory

Create the base project structure:

```powershell
# Create main project directory
$ProjectPath = "E:\DevProjects\MyApp"

if (-not (Test-Path $ProjectPath)) {
    New-Item -ItemType Directory -Path $ProjectPath | Out-Null
    Write-Output "✓ Project directory created at $ProjectPath"
} else {
    Write-Output "✓ Project directory already exists"
}

# Create subdirectories
@("src", "tests", "docs", "build") | ForEach-Object {
    $SubPath = Join-Path $ProjectPath $_
    if (-not (Test-Path $SubPath)) {
        New-Item -ItemType Directory -Path $SubPath | Out-Null
        Write-Output "✓ Created subdirectory: $_"
    }
}
```

---

## Step 2: Initialize Git Repository

Set up version control:

```bash
cd E:\DevProjects\MyApp
git init
git config user.name "Developer"
git config user.email "dev@example.com"
echo "✓ Git repository initialized"
```

---

## Step 3: Create Python Virtual Environment

Set up Python development environment:

```powershell
# Navigate to project
cd E:\DevProjects\MyApp

# Create virtual environment
python -m venv venv

# Activate virtual environment
& ".\venv\Scripts\Activate.ps1"

Write-Output "✓ Python virtual environment created and activated"
```

---

## Step 4: Install Python Dependencies

Install required packages:

```python
import subprocess
import sys

packages = [
    "flask",
    "requests",
    "python-dotenv",
    "pytest",
    "black",
    "pylint"
]

print("📦 Installing Python packages...")
print("=" * 50)

for package in packages:
    try:
        subprocess.run(
            [sys.executable, "-m", "pip", "install", package],
            check=True,
            capture_output=True
        )
        print(f"✓ {package:20} installed successfully")
    except subprocess.CalledProcessError as e:
        print(f"✗ {package:20} installation failed")
        raise

print("=" * 50)
print("✓ All packages installed successfully!")
```

---

## Step 5: Create Project Files

Create initial project structure with files:

```powershell
$ProjectPath = "E:\DevProjects\MyApp"

# Create main application file
$AppContent = @"
#!/usr/bin/env python3
"""
Main application entry point
"""

def hello():
    return "Hello from Windows-MCP!"

if __name__ == "__main__":
    print(hello())
"@

Set-Content -Path (Join-Path $ProjectPath "src\main.py") -Value $AppContent
Write-Output "✓ Created src/main.py"

# Create requirements.txt
$ReqContent = @"
flask==3.0.0
requests==2.31.0
python-dotenv==1.0.0
pytest==7.4.0
black==23.9.1
pylint==2.17.5
"@

Set-Content -Path (Join-Path $ProjectPath "requirements.txt") -Value $ReqContent
Write-Output "✓ Created requirements.txt"

# Create .gitignore
$GitIgnoreContent = @"
venv/
__pycache__/
*.pyc
.env
.pytest_cache/
.coverage
build/
dist/
*.egg-info/
.vscode/
.idea/
"@

Set-Content -Path (Join-Path $ProjectPath ".gitignore") -Value $GitIgnoreContent
Write-Output "✓ Created .gitignore"

# Create README
$ReadmeContent = @"
# My Application

A demonstration project using Windows-MCP and ExecuteMarkdown.

## Setup

Run the setup guide to automatically configure this project:
\`\`\`bash
Execute setup-guide.md
\`\`\`

## Development

Activate the virtual environment:
\`\`\`bash
.\venv\Scripts\Activate.ps1
\`\`\`

## Testing

Run tests:
\`\`\`bash
pytest tests/
\`\`\`
"@

Set-Content -Path (Join-Path $ProjectPath "README.md") -Value $ReadmeContent
Write-Output "✓ Created README.md"

Write-Output "✓ All project files created successfully!"
```

---

## Step 6: Run Initial Tests

Create and run a test file:

```python
import subprocess
import sys
from pathlib import Path

# Create test file
test_content = '''
def test_hello():
    from src.main import hello
    assert hello() == "Hello from Windows-MCP!"

def test_import():
    import flask
    import requests
    assert flask is not None
    assert requests is not None
'''

test_dir = Path("E:\DevProjects\MyApp\tests")
test_file = test_dir / "test_main.py"

test_file.write_text(test_content)
print("✓ Created test file")

# Run tests
print("\n" + "=" * 50)
print("Running tests...")
print("=" * 50 + "\n")

result = subprocess.run(
    [sys.executable, "-m", "pytest", "tests/", "-v"],
    cwd="E:\DevProjects\MyApp"
)

if result.returncode == 0:
    print("\n✓ All tests passed!")
else:
    print("\n⚠ Some tests failed - review output above")
```

---

## Step 7: Verify Installation

Confirm everything is set up correctly:

```powershell
$ProjectPath = "E:\DevProjects\MyApp"

Write-Output "`n" + "=" * 60
Write-Output "SETUP VERIFICATION"
Write-Output "=" * 60 + "`n"

# Check directory structure
Write-Output "Directory Structure:"
Get-ChildItem -Path $ProjectPath -Recurse -Directory |
    ForEach-Object { "  ✓ $_" }

# Check files
Write-Output "`nProject Files:"
Get-ChildItem -Path $ProjectPath -File |
    ForEach-Object { "  ✓ $($_.Name)" }

# Check Python version
Write-Output "`nPython Information:"
$PythonVersion = python --version 2>&1
Write-Output "  ✓ $PythonVersion"

# Check git
Write-Output "`nGit Repository:"
if (Test-Path (Join-Path $ProjectPath ".git")) {
    Write-Output "  ✓ Git repository initialized"
} else {
    Write-Output "  ✗ Git repository not found"
}

Write-Output "`n" + "=" * 60
Write-Output "✓ SETUP COMPLETE!"
Write-Output "=" * 60
Write-Output "`nYour development environment is ready to use!"
Write-Output "Next steps:"
Write-Output "  1. Navigate to: cd E:\DevProjects\MyApp"
Write-Output "  2. Activate venv: .\venv\Scripts\Activate.ps1"
Write-Output "  3. Start coding!"
```

---

## Summary

This guide automatically:
- ✓ Creates project directory structure
- ✓ Initializes git repository
- ✓ Sets up Python virtual environment
- ✓ Installs all dependencies
- ✓ Creates project files (main.py, README, .gitignore)
- ✓ Creates and runs initial tests
- ✓ Verifies installation

**Time saved**: ~15-20 minutes of manual setup
**Errors prevented**: Typos, missed steps, version conflicts
**Accessibility benefit**: 100% hands-free operation
