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

    with open(markdown, 'r') as f:
        lines = f.readlines()

    with open(output, 'w') as f:
        for line in lines:
            line = line.strip()
        
            if line.startswith('#'):
                heading_count = line.count('#')
                heading_text = line.strip('#').strip()

                html = f'<h{heading_count}>{heading_text}</h{heading_count}>'
                f.write(html)
            else:
                f.write(line + '\n')
    sys.exit(0)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(
            'Usage: ./markdown2html.py README.md README.html',
            file=sys.stderr
            )
        sys.exit(1)

    if isinstance(sys.argv[1], str) and isinstance(sys.argv[2], str):
        markdown2html(sys.argv[1], sys.argv[2])
