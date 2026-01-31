# Contributor License Agreement (CLA) Guide

Thank you for your interest in contributing to Windows-MCP! To ensure we can legally use and distribute your contributions, we ask all contributors to agree to a Contributor License Agreement (CLA).

## Table of Contents

- [What is a CLA?](#what-is-a-cla)
- [Our CLA Policy](#our-cla-policy)
- [Contributing Code](#contributing-code)
- [Adding Windows-MCP as a Custom Claude Extension](#adding-windows-mcp-as-a-custom-claude-extension)
- [Accessibility Features](#accessibility-features)
  - [ExecuteMarkdown Tool](#executemarkdown-tool)
  - [Accessibility Best Practices](#accessibility-best-practices)
- [Questions or Concerns?](#questions-or-concerns)

## What is a CLA?

A Contributor License Agreement (CLA) is a legal document that clarifies the intellectual property rights of contributions to an open-source project. It ensures that:

- You have the rights to the code you're contributing
- The project can legally use, modify, and distribute your contributions
- Your contributions are protected under the project's MIT license
- Contributors and maintainers have clear legal standing

## Our CLA Policy

Windows-MCP follows a **simple CLA policy** based on the MIT License:

### For Individual Contributors

By submitting a pull request or contribution to Windows-MCP, you agree that:

1. **You own or have the necessary rights** to the code you're submitting
2. **You grant Windows-MCP a perpetual, worldwide, non-exclusive license** to use your contribution under the MIT License
3. **Your contribution is original** and doesn't infringe on third-party rights
4. **You waive any moral rights** to your contribution in the jurisdictions where such rights can be waived

### For Corporate Contributors

If you're contributing on behalf of a company:

1. Your company grants Windows-MCP the same license as individual contributors
2. Ensure you have authorization from your company to make the contribution
3. The agreement applies to your employer's code contributions

## Contributing Code

### Before You Submit

1. **Review the LICENSE**: Ensure you understand our [MIT License](LICENSE.md)
2. **Follow Contribution Guidelines**: See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines
3. **Agree to the CLA**: By submitting your PR, you're agreeing to these terms
4. **Add Your Name**: Consider adding yourself to the contributors list

### Submission Process

1. Create a fork of the repository
2. Make your changes on a feature branch
3. Ensure your code follows our [style guidelines](CONTRIBUTING.md#code-style)
4. Add tests if applicable
5. Submit a pull request with clear descriptions
6. Your PR will be reviewed by maintainers
7. Upon approval and merge, you'll be recognized as a contributor

### What Happens After Contribution

- Your contribution becomes part of Windows-MCP under the MIT License
- You'll be listed in the [contributors list](https://github.com/CursorTouch/Windows-MCP/graphs/contributors)
- For significant contributions, you may be mentioned in release notes
- Your contribution can be used by anyone under MIT license terms

## Adding Windows-MCP as a Custom Claude Extension

Windows-MCP is available as a custom Claude extension, allowing you to use it with Claude AI for Windows automation tasks.

### Prerequisites

- Claude Desktop application installed
- Python 3.13 or higher
- UV package manager (`pip install uv` or see [UV docs](https://github.com/astral-sh/uv))

### Installation Methods

#### Option A: Install from PyPI (Recommended)

The easiest way to use Windows-MCP as a Claude extension:

1. Open Claude Desktop
2. Go to **Settings** → **Developer** (or **Preferences** → **Developer**)
3. Click **Edit Config** to open your `claude_desktop_config.json` file
4. Add the following configuration:

```json
{
  "mcpServers": {
    "windows-mcp": {
      "command": "uvx",
      "args": [
        "windows-mcp"
      ]
    }
  }
}
```

5. Save the file and restart Claude Desktop
6. You should see "Windows-MCP" listed as an available extension
7. Enable it and start using Windows automation!

#### Option B: Install from Source (Development)

If you're contributing or want the latest development version:

1. Clone the repository:
```bash
git clone https://github.com/CursorTouch/Windows-MCP.git
cd Windows-MCP
```

2. Install dependencies:
```bash
uv sync
```

3. Open your `claude_desktop_config.json` and add:

```json
{
  "mcpServers": {
    "windows-mcp": {
      "command": "uv",
      "args": [
        "--directory",
        "C:\\path\\to\\Windows-MCP",
        "run",
        "windows-mcp"
      ]
    }
  }
}
```

Replace `C:\path\to\Windows-MCP` with the actual path to your cloned repository.

4. Save and restart Claude Desktop

### Configuration Options

#### Disable Telemetry

To disable telemetry collection, add the following environment variable:

```json
{
  "mcpServers": {
    "windows-mcp": {
      "command": "uvx",
      "args": ["windows-mcp"],
      "env": {
        "ANONYMIZED_TELEMETRY": "false"
      }
    }
  }
}
```

#### Custom Timeout (Advanced)

For slower systems, you can increase the timeout:

```json
{
  "mcpServers": {
    "windows-mcp": {
      "command": "uvx",
      "args": ["windows-mcp"],
      "env": {
        "POWERSHELL_TIMEOUT": "20"
      }
    }
  }
}
```

### Verifying Installation

After installation:

1. Restart Claude Desktop completely
2. Check the extension sidebar to ensure Windows-MCP appears
3. You should see available tools like:
   - App Tool (launch/manage applications)
   - State Tool (capture desktop state)
   - Click Tool (interact with UI elements)
   - Type Tool (input text)
   - Scroll Tool (navigate content)
   - And more...

### Troubleshooting

**Extension doesn't appear:**
- Check that your `claude_desktop_config.json` is valid JSON
- Verify Python 3.13+ is installed: `python --version`
- Verify UV is installed: `uv --version`
- Check Claude Desktop logs for errors

**Configuration file location:**
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`

**Extension won't load:**
- Try restarting Claude Desktop completely
- Check the Developer console for error messages
- Ensure you have write permissions to the config file

For more detailed troubleshooting, see the [MCP documentation](https://modelcontextprotocol.io/quickstart/server#claude-for-desktop-integration-issues).

## Accessibility Features

Windows-MCP includes accessibility features designed to support users with motor disabilities and other accessibility needs.

### ExecuteMarkdown Tool

The **ExecuteMarkdown** tool is a powerful accessibility feature that automatically executes code blocks from markdown files or content. This is particularly beneficial for users with motor disabilities who may have difficulty:
- Typing long commands
- Navigating multiple tools and windows
- Performing repetitive setup procedures

#### Use Cases

1. **Automated Setup Scripts**: Execute entire deployment instructions from markdown documentation
2. **Installation Guides**: Auto-run multi-step installation procedures
3. **Configuration Files**: Execute code blocks that configure your system
4. **Development Workflows**: Automate build and test scripts
5. **Batch Operations**: Run multiple commands in sequence without manual intervention

#### Supported Languages

- **Python** (`.py` code blocks)
- **PowerShell** (`.ps1`, `.posh`, `.powershell` blocks)
- **Bash/Shell** (`.sh`, `.bash`, `.shell` blocks)

#### Basic Usage in Claude Desktop

Tell Claude: *"Execute the setup instructions from my markdown file at C:\path\to\setup.md"*

Claude will:
1. Read the markdown file
2. Extract all code blocks
3. Execute them in order
4. Report the results with success/failure status for each block

#### Example Markdown File

```markdown
# Setup Instructions

Install Python dependencies:

\`\`\`python
import subprocess
subprocess.run(["pip", "install", "requests", "numpy"], check=True)
\`\`\`

Create project directories:

\`\`\`powershell
New-Item -ItemType Directory -Path "C:\Projects\MyApp"
Set-Location "C:\Projects\MyApp"
\`\`\`

Initialize git repository:

\`\`\`bash
git init
git config user.name "Your Name"
\`\`\`
```

#### Error Handling

The ExecuteMarkdown tool has two modes:

1. **Stop on Error** (default): Stops execution at the first failed code block
2. **Skip on Error** (skip_on_error=True): Continues executing remaining blocks even if one fails

#### Technical Details

- **Timeout**: Each code block has a 30-second execution timeout
- **Output Limiting**: Output is limited to first 500 characters per block
- **Error Reporting**: Full error messages are captured and reported
- **Execution Timing**: Each block's execution time is tracked and reported

#### Creating Accessible Markdown Guides

If you're creating documentation or guides for users with motor disabilities:

1. **Organize Code Blocks**: Structure your markdown with clear code blocks
2. **Add Context**: Include explanatory text before each code block
3. **Use Comments**: Add comments within code blocks explaining what each line does
4. **Test Your Blocks**: Verify that all code blocks execute correctly in order
5. **Error Handling**: Include error handling in your scripts when possible
6. **Progress Indicators**: Add status output in your code blocks to show progress

#### Example Accessible Setup Guide

```markdown
# Accessible Windows Environment Setup

This guide can be automatically executed using Windows-MCP's ExecuteMarkdown tool.

## Step 1: Create Project Structure

Create the main project directory:

\`\`\`powershell
# Create main project directory
$ProjectPath = "C:\MyAccessibleProject"
if (-not (Test-Path $ProjectPath)) {
    New-Item -ItemType Directory -Path $ProjectPath
    Write-Output "✓ Project directory created"
} else {
    Write-Output "✓ Project directory already exists"
}
\`\`\`

## Step 2: Install Dependencies

Install required Python packages:

\`\`\`python
import subprocess
import sys

packages = ["flask", "requests", "python-dotenv"]
print("📦 Installing packages...")

for package in packages:
    subprocess.run([sys.executable, "-m", "pip", "install", package], check=True)
    print(f"✓ {package} installed")
\`\`\`

## Step 3: Run Tests

Execute test suite:

\`\`\`bash
echo "🧪 Running tests..."
python -m pytest tests/ -v
\`\`\`
```

### Accessibility Best Practices

Windows-MCP is designed with accessibility in mind:

1. **Voice Control Compatible**: Works well with voice control tools for hands-free operation
2. **Minimal Manual Input**: Most operations can be triggered via voice or single commands
3. **Clear Output**: All tool results are formatted clearly and logically
4. **Keyboard Navigation**: All features are keyboard accessible
5. **Batch Operations**: Run multiple commands together reduces repetitive actions
6. **Documentation**: Extensive documentation supports users learning the system

### Getting Help with Accessibility

If you have accessibility needs or suggestions:

- **GitHub Issues**: Open an issue with the [accessibility label](https://github.com/CursorTouch/Windows-MCP/issues?q=label%3Aaccessibility)
- **Email**: [jeogeoalukka@gmail.com](mailto:jeogeoalukka@gmail.com)
- **Discord**: Discuss accessibility features in our [community](https://discord.com/invite/Aue9Yj2VzS)

## Questions or Concerns?

### About the CLA

- **Email**: [jeogeoalukka@gmail.com](mailto:jeogeoalukka@gmail.com)
- **GitHub Issues**: [Submit a question](https://github.com/CursorTouch/Windows-MCP/issues)
- **Discord**: Join our [community](https://discord.com/invite/Aue9Yj2VzS)

### About Windows-MCP

- **Documentation**: [README.md](README.md)
- **Security**: [SECURITY.md](SECURITY.md)
- **Contributing**: [CONTRIBUTING.md](CONTRIBUTING.md)
- **Twitter/X**: [@CursorTouch](https://x.com/CursorTouch)
- **Discord**: [CursorTouch Community](https://discord.com/invite/Aue9Yj2VzS)

## Summary

By contributing to Windows-MCP, you're agreeing to share your work under the MIT License. Your contributions help make Windows automation accessible to everyone while maintaining clear legal protections for both contributors and users.

We appreciate your contribution! 🙏

---

**Version**: 1.0
**Last Updated**: January 2026
**License**: MIT

Made with ❤️ by the CursorTouch community
