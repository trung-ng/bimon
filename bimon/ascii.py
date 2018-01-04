# -*- coding: utf-8 -*-

import sys
from bimon.common import Colors
if sys.version_info >= (3, 0):
    import io
else:
    import StringIO as io



ascii_title = """
 /$$$$$$$  /$$                                                         /$$      /$$                    
| $$__  $$|__/                                                        | $$$    /$$$                    
| $$  \ $$ /$$ /$$$$$$$   /$$$$$$  /$$$$$$$   /$$$$$$$  /$$$$$$       | $$$$  /$$$$  /$$$$$$  /$$$$$$$ 
| $$$$$$$ | $$| $$__  $$ |____  $$| $$__  $$ /$$_____/ /$$__  $$      | $$ $$/$$ $$ /$$__  $$| $$__  $$
| $$__  $$| $$| $$  \ $$  /$$$$$$$| $$  \ $$| $$      | $$$$$$$$      | $$  $$$| $$| $$  \ $$| $$  \ $$
| $$  \ $$| $$| $$  | $$ /$$__  $$| $$  | $$| $$      | $$_____/      | $$\  $ | $$| $$  | $$| $$  | $$
| $$$$$$$/| $$| $$  | $$|  $$$$$$$| $$  | $$|  $$$$$$$|  $$$$$$$      | $$ \/  | $$|  $$$$$$/| $$  | $$
|_______/ |__/|__/  |__/ \_______/|__/  |__/ \_______/ \_______/      |__/     |__/ \______/ |__/  |__/
"""                                                                                                       
                                                                                                       
def process_title(title):
    buf = io.StringIO(title)
    lines = buf.readlines()
    lines = lines[1:-1]
    colored_lines = []
    colored_title = ""

    for line in lines:
        colored_lines.append(Colors.BLUE + line[:13] + Colors.YELLOW + line[14:])

    for line in colored_lines:
        colored_title += line

    return colored_title + Colors.ENDLINE
