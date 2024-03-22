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
    if len(sys.argv) < 3:
        sys.stderr('Usage: ./markdown2html.py README.md README.html')
        sys.exit(1)
        
    if not os.path.isfile(markdown):
        sys.stderr('Missing', markdown, file=sys.stderr)
        sys.exit(1)
    
    sys.exit(0)
