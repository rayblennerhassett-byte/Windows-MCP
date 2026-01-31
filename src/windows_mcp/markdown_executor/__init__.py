"""Markdown Executor - Auto-execute code blocks from markdown files.

Supports accessibility features for users with motor disabilities by allowing
automatic execution of setup scripts and deployment instructions.
"""

from .service import CodeBlock, ExecutionResult, MarkdownExecutor

__all__ = ["MarkdownExecutor", "CodeBlock", "ExecutionResult"]
