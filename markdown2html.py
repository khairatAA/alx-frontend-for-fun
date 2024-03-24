#!/usr/bin/python3
"""markdown2html"""
import sys
import os


def markdown2html(markdown, output):
    """
    markdown2html: Markdown to HTML

    Args:
        markdown: Markdown file
        output: output file name
    """

    if not os.path.isfile(markdown):
        print(f"Missing {markdown}", file=sys.stderr)
        sys.exit(1)

    with open(markdown, 'r') as f:
        lines = f.readlines()

    with open(output, 'w') as f:
        list_item = False
        ordered_list = False
        contd_paragraph = False

        for line in lines:
            line = line.strip()

            if line.startswith('#'):
                heading_count = line.count('#')
                heading_text = line.strip('#').strip()

                html = f'<h{heading_count}>{heading_text}</h{heading_count}>'
                f.write(f'{html}\n')

            elif line.startswith('-'):
                if not list_item:
                    f.write('<ul>\n')
                    list_item = True
                f.write(f"  <li>{line.strip('-').strip()}</li>\n")

            elif line.startswith('*'):
                if not ordered_list:
                    f.write('<ol>\n')
                    ordered_list = True
                f.write(f"  <li>{line.strip('*').strip()}</li>\n")

            else:
                if line:
                    if not contd_paragraph:
                        f.write('<p>\n')
                        contd_paragraph = True
                    else:
                        f.write('<br/>\n')
                    f.write(f'{line}\n')
                else:
                    if contd_paragraph:
                        f.write('</p>\n')
                        contd_paragraph = False

                if list_item:
                    f.write('</ul>\n')
                    list_item = False
                elif ordered_list:
                    f.write('</ol>\n')
                    ordered_list = False

        if contd_paragraph:
            f.write('</p>\n')

        if list_item:
            f.write('</ul>\n')
        elif ordered_list:
            f.write('</ol>\n')

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
