# -*- coding: utf-8 -*-

import difflib
import copy
import re
from humanize import intword

fields_good_name = {
    "symbol": "Symbol",
    "lastPrice": "Price",
    "priceChangePercent": "Change (24H)",
}


class Colors:
    YELLOW = '\033[93m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    ENDLINE = '\033[0m'

    @staticmethod
    def color_data(data):
        data[0][0] = Colors.YELLOW + data[0][0]
        data[0][len(data[0]) - 1] = data[0][len(data[0]) - 1] + Colors.ENDLINE

        for item in data[1:]:
            if re.search('-\d+\.\d+', item[2]):
                item[2] = Colors.RED + item[2] + '%' + Colors.ENDLINE
            else:
                item[2] = Colors.GREEN + item[2] + '%' + Colors.ENDLINE


def process_data(data, fields=['symbol','lastPrice','priceChangePercent']):

    # Initialize structure
    tabulated_data = []
    tabulated_data.append(copy.copy(fields))   # Headers in position 0

    pos = 0
    for header in tabulated_data[0]:   # Headers in position 0
        good_header = difflib.get_close_matches(header, fields_good_name.keys())[0]
        tabulated_data[0][pos] = fields_good_name[good_header]

        pos += 1

    for item in data:
        tab_item = []
        for field in fields:
            tab_item.append(item[field])
        tabulated_data.append(copy.copy(tab_item))

    return tabulated_data


def find_data(data, symbols):

    symbols = [x.upper() for x in symbols]   # Convert to upper-case
    filtered_items = []
    for item in data:
        if item['symbol'] in symbols:
            filtered_items.append(item)

    return filtered_items
