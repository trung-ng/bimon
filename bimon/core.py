# -*- coding: utf-8 -*-

import argparse
from tabulate import tabulate
from bimon.common import process_data, find_data, Colors
from bimon.ascii import ascii_title, process_title
from bimon.metadata import Metadata
from binance.client import Client
#from terminaltables import AsciiTable
from colorama import init, deinit
import os
import time

class BiMon(object):

    def __init__(self):
        if 'PYCHARM_HOSTED' not in os.environ:  # Exclude PyCharm IDE from colorama init
            init()
        self.meta = Metadata()
        self.sourceURL = "https://api.coinmarketcap.com/v1/ticker"

        # Parse arguments provided
        parser = argparse.ArgumentParser()
        parser.add_argument('-a', '--apikey', dest='api_key',
                            help='Binance API_KEY', type=str, default=None)
        parser.add_argument('-s', '--apisecret', dest='api_secret',
                            help='Binance SECRET_KEY', type=str, default=None)
        parser.add_argument('-v', '--version', action='version', version=self.meta.get_version())
        parser.add_argument('-f', '--find', dest='symbol',
                            help='Find specific coin data with coin symbol (can be a space seperated list)',
                            metavar='S', type=str, nargs='+')
        parser.add_argument('-l', '--layout', dest='template', help='Select table layout', default='grid',
                            choices=['plain', 'simple', 'grid', 'fancy_grid', 'pipe', 'orgtbl', 'presto', 'psql',
                                     'rst'],
                            type=lambda s: s.lower())
        parser.add_argument('-u', '--update', dest='frequency',
                            help='Update data with frequency specified in seconds. If 0 just show one time.',
                            type=self.check_positive)

        self.args = parser.parse_args()
        self.client = Client(self.args.api_key, self.args.api_secret)

    def __del__(self):
        if deinit is not None:   # Prevent error when argparse raise exception
            deinit()

    @staticmethod
    def check_positive(value):
        ivalue = int(value)
        if ivalue <= 0:
            raise argparse.ArgumentTypeError("%s is an invalid positive int value" % value)
        return ivalue

    def print_values(self):
        # Update values

        response = self.client.get_ticker()

        # Clear screen
        if os.name == 'nt':
            os.system('cls')   # on windows
        else:
            os.system('clear')   # on linux / os x

        # Redraw data

        print(process_title(ascii_title))
        # print(Colors.YELLOW + ascii_title + Colors.ENDLINE)
        if self.args.symbol:
            filtered_data = find_data(response, self.args.symbol)
        else:
            filtered_data = response

        tabulated_data = process_data(filtered_data)

        Colors.color_data(tabulated_data)
        # table = AsciiTable(tabulated_data)
        # print(table.table)
        print(tabulate(tabulated_data, headers='firstrow', numalign="right", tablefmt=self.args.template))
        print("\n")

    def run(self):
        if self.args.frequency:
            try:
                while True:
                    self.print_values()
                    print("Press Ctrl + C to exit.")
                    time.sleep(int(self.args.frequency))
            except KeyboardInterrupt:
                pass
        else:
            self.print_values()


if __name__ == "__main__":
    bimon = BiMon()
    bimon.run()
