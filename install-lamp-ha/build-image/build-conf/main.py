#!/usr/bin/env python3

# --- Global imports ---
import os
import sys
import re

# --- Local imports ---
# from graphic_tools import bcolors, progressbar
# from analysis_tools import regex
# from template import Template


class bcolors:
    SUCCESS = '\033[92m'
    WARNING = '\033[93m'
    ERROR = '\033[91m'
    ENDC = '\033[0m'


class regex:
    DIGIT = re.compile('^[0-9]+$')
    STRNOSPACE = re.compile('^[0-9a-zA-Z_]+$')
    IPV4 = re.compile('^[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}$')
    EMAIL = re.compile('^$')


class Main:

    def __init__(self):
        self.int_params = {
            "apache_http_port": 0,
        }
        self.str_params = {
            "apache_server_name": "",
        }
        self.email_params = {
            "apache_admin_email": ""
        }
        self.ip_params = {
            "global_host_ipv4": "",
        }

        try:
            with open('./header.txt', 'r') as ifile:
                self.header = ifile.read()
        except FileNotFoundError as error:
            print(f"{bcolors.ERROR}ERROR - Cannot load header text but is required{bcolors.ENDC}")
            print(f"{bcolors.ERROR}Program return: {error}{bcolors.ENDC}")
            print(f"{bcolors.ERROR}Program was aborded with exit code 1, see ./docs/doc_v1_0.fr.md for more informations{bcolors.ENDC}")
            sys.exit()

    def buildConfigurations(self):

        print("\nBUILD CONFIGURATIONS")
        print("Please indicate all required parameters bellow:\n")

        for i in self.int_params:
            param = input(f"{i}: ")
            while regex.DIGIT.match(param) == None:
                print(f"{bcolors.WARNING}WARNING - {i} must be positive integer, not '{param}'{bcolors.ENDC}")
                param = input(f"(Try again) {i}: ")
            self.int_params[i] = param

        for i in self.ip_params:
            param = input(f"{i}: ")
            while regex.IPV4.match(param) == None:
                print(f"{bcolors.WARNING}WARNING - {i} must be IPv4 format (e.g. 192.168.1.1), not '{param}'{bcolors.ENDC}")
                param = input(f"(Try again) {i}: ")
            self.ip_params[i] = param

    def getHelp(self):
        return

    def restorBackup(self):
        return

    def displayFlip(self, on_error=False, error_code=0, error_value=""):
        os.system("clear")
        print(self.header)
        if on_error:
            if error_code == 1:
                print(f"{bcolors.WARNING}WARNING - Please indicate 1, 2, 3 or exit, not '{error_value}'{bcolors.ENDC}")
        else:
            print("Type 'exit' or 'e' to stop.")

    def run(self):
        self.displayFlip()
        choice = input("Please select an option: ")
        while choice not in ["1", "2", "3", "exit", "e"]:
            self.displayFlip(on_error=True, error_code=1, error_value=choice)
            choice = input("Please select an option: ")

        if choice in ["exit", "e"]:
            os.system("clear")
            sys.exit()

        elif choice == "1":
            self.buildConfigurations()


if __name__ == '__main__':
    main = Main()
    main.run()
