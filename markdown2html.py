#!/usr/bin/python3
"""markdown2html"""
import sys
import os


def markdown2html(markdown, output):
    """
    markdown2html: Markdown to HTML

    args:
        markdown: Markdown file
        output: output file name
    """

    if not os.path.isfile(markdown):
        print(f"Missing {markdown}", file=sys.stderr)
        sys.exit(1)

    sys.exit(0)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(
            'Usage: ./markdown2html.py README.md README.html',
            file=sys.stderr
            )
        sys.exit(1)

    if isinstance(sys.argv[1], str) and isinstance(sys.argv[2], str):
        markdown2html(sys.argv[1], sys.argv[2])
