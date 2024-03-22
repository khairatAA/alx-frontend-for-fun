#!/usr/bin/python3
"""markdown2html"""
import sys
import os
import markdown


def markdown2html(markdown_file, output_file):
    """
    markdown2html: Markdown to HTML

    Args:
        markdown_file(str): Markdown file
        output_file(str): output file name
    """

    if not os.path.isfile(markdown_file):
        print(f"Missing {markdown_file}", file=sys.stderr)
        sys.exit(1)

    with open(markdown_file, 'r') as f:
        tempMd = f.read()

    tempHTML = markdown.markdown(tempMd)

    with open(output_file, 'w') as f:
        f.write(tempHTML)

    sys.exit(0)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(
            'Usage: ./markdown2html.py README.md README.html',
            file=sys.stderr
            )
        sys.exit(1)

    # if isinstance(sys.argv[1], str) and isinstance(sys.argv[2], str):
    markdown2html(sys.argv[1], sys.argv[2])
