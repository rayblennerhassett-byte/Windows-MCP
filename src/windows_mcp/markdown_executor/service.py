"""Markdown Executor Service - Parse and execute code blocks from markdown files.

This service enables accessibility features for users with motor disabilities by
allowing automatic execution of code blocks from markdown files, supporting Python,
PowerShell, Bash, and shell commands.
"""

import re
import subprocess
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Optional


@dataclass
class CodeBlock:
    """Represents a code block extracted from markdown."""

    language: str
    code: str
    line_number: int


@dataclass
class ExecutionResult:
    """Result of executing a code block."""

    language: str
    code: str
    success: bool
    output: str
    error: Optional[str] = None
    execution_time: float = 0.0


class MarkdownExecutor:
    """Parse and execute code blocks from markdown files.

    This class helps users with motor disabilities by automatically executing
    setup scripts and deployment instructions embedded in markdown files.
    Supports Python, PowerShell, Bash, and shell scripts.
    """

    def __init__(self):
        """Initialize the Markdown Executor."""
        self.results: list[ExecutionResult] = []
        self.code_block_pattern = re.compile(
            r"```(\w+)\n(.*?)```", re.DOTALL
        )

    def extract_code_blocks(self, markdown_content: str) -> list[CodeBlock]:
        """Extract all code blocks from markdown content.

        Args:
            markdown_content: The markdown file content as a string

        Returns:
            List of CodeBlock objects with language, code, and line numbers
        """
        blocks = []
        current_line = 1

        for match in self.code_block_pattern.finditer(markdown_content):
            language = match.group(1).lower().strip()
            code = match.group(2).strip()

            # Count lines before this block to get accurate line numbers
            lines_before = markdown_content[: match.start()].count("\n")

            blocks.append(
                CodeBlock(
                    language=language,
                    code=code,
                    line_number=lines_before + 1,
                )
            )

        return blocks

    def execute_python_block(self, code: str) -> tuple[bool, str, Optional[str]]:
        """Execute a Python code block.

        Args:
            code: Python code to execute

        Returns:
            Tuple of (success, output, error)
        """
        try:
            with tempfile.NamedTemporaryFile(
                mode="w", suffix=".py", delete=False
            ) as f:
                f.write(code)
                temp_file = f.name

            try:
                result = subprocess.run(
                    ["python", temp_file],
                    capture_output=True,
                    text=True,
                    timeout=30,
                )
                output = result.stdout
                error = result.stderr if result.returncode != 0 else None
                success = result.returncode == 0

                return success, output, error
            finally:
                Path(temp_file).unlink(missing_ok=True)

        except subprocess.TimeoutExpired:
            return False, "", "Execution timeout (30 seconds)"
        except Exception as e:
            return False, "", str(e)

    def execute_powershell_block(
        self, code: str
    ) -> tuple[bool, str, Optional[str]]:
        """Execute a PowerShell code block.

        Args:
            code: PowerShell code to execute

        Returns:
            Tuple of (success, output, error)
        """
        try:
            result = subprocess.run(
                ["powershell", "-Command", code],
                capture_output=True,
                text=True,
                timeout=30,
            )
            output = result.stdout
            error = result.stderr if result.returncode != 0 else None
            success = result.returncode == 0

            return success, output, error

        except subprocess.TimeoutExpired:
            return False, "", "Execution timeout (30 seconds)"
        except Exception as e:
            return False, "", str(e)

    def execute_shell_block(self, code: str) -> tuple[bool, str, Optional[str]]:
        """Execute a shell/bash code block.

        Args:
            code: Shell code to execute

        Returns:
            Tuple of (success, output, error)
        """
        try:
            result = subprocess.run(
                code,
                shell=True,
                capture_output=True,
                text=True,
                timeout=30,
            )
            output = result.stdout
            error = result.stderr if result.returncode != 0 else None
            success = result.returncode == 0

            return success, output, error

        except subprocess.TimeoutExpired:
            return False, "", "Execution timeout (30 seconds)"
        except Exception as e:
            return False, "", str(e)

    def execute_block(self, block: CodeBlock) -> ExecutionResult:
        """Execute a single code block.

        Args:
            block: The CodeBlock to execute

        Returns:
            ExecutionResult with success status and output
        """
        import time

        start_time = time.time()

        language = block.language.lower()

        if language in ("python", "py"):
            success, output, error = self.execute_python_block(block.code)
        elif language in ("powershell", "ps1", "posh"):
            success, output, error = self.execute_powershell_block(block.code)
        elif language in ("bash", "sh", "shell"):
            success, output, error = self.execute_shell_block(block.code)
        else:
            success = False
            output = ""
            error = f"Unsupported language: {language}. Supported: python, powershell, bash"

        execution_time = time.time() - start_time

        result = ExecutionResult(
            language=block.language,
            code=block.code,
            success=success,
            output=output,
            error=error,
            execution_time=execution_time,
        )

        self.results.append(result)
        return result

    def execute_markdown_file(
        self, file_path: str, skip_on_error: bool = False
    ) -> dict:
        """Execute all code blocks in a markdown file.

        Args:
            file_path: Path to the markdown file
            skip_on_error: If True, continue executing even if a block fails

        Returns:
            Dictionary with execution summary and results
        """
        self.results = []

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                markdown_content = f.read()
        except Exception as e:
            return {
                "success": False,
                "error": f"Failed to read file: {str(e)}",
                "file": file_path,
                "blocks_found": 0,
                "blocks_executed": 0,
                "blocks_failed": 0,
                "results": [],
            }

        blocks = self.extract_code_blocks(markdown_content)

        executed = 0
        failed = 0

        for block in blocks:
            result = self.execute_block(block)
            executed += 1

            if not result.success:
                failed += 1
                if not skip_on_error:
                    break

        return {
            "success": failed == 0,
            "file": file_path,
            "blocks_found": len(blocks),
            "blocks_executed": executed,
            "blocks_failed": failed,
            "results": [
                {
                    "language": r.language,
                    "success": r.success,
                    "output": r.output[:500],  # Limit output length
                    "error": r.error,
                    "execution_time": f"{r.execution_time:.2f}s",
                }
                for r in self.results
            ],
        }

    def execute_markdown_content(
        self, content: str, skip_on_error: bool = False
    ) -> dict:
        """Execute all code blocks in markdown content string.

        Args:
            content: Markdown content as a string
            skip_on_error: If True, continue executing even if a block fails

        Returns:
            Dictionary with execution summary and results
        """
        self.results = []

        blocks = self.extract_code_blocks(content)

        executed = 0
        failed = 0

        for block in blocks:
            result = self.execute_block(block)
            executed += 1

            if not result.success:
                failed += 1
                if not skip_on_error:
                    break

        return {
            "success": failed == 0,
            "blocks_found": len(blocks),
            "blocks_executed": executed,
            "blocks_failed": failed,
            "results": [
                {
                    "language": r.language,
                    "success": r.success,
                    "output": r.output[:500],
                    "error": r.error,
                    "execution_time": f"{r.execution_time:.2f}s",
                }
                for r in self.results
            ],
        }
