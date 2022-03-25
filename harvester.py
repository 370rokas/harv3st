"""
██╗░░██╗░█████╗░██████╗░██╗░░░██╗██████╗░░██████╗████████╗
██║░░██║██╔══██╗██╔══██╗██║░░░██║╚════██╗██╔════╝╚══██╔══╝
███████║███████║██████╔╝╚██╗░██╔╝░█████╔╝╚█████╗░░░░██║░░░
██╔══██║██╔══██║██╔══██╗░╚████╔╝░░╚═══██╗░╚═══██╗░░░██║░░░
██║░░██║██║░░██║██║░░██║░░╚██╔╝░░██████╔╝██████╔╝░░░██║░░░
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═════╝░╚═════╝░░░░╚═╝░░░

370rokas (c) 2022
https://github.com/370rokas

harvester.py - Contains main functions and stuff
"""

from misc import pretty_output
import harversters.github as gh


def run_username(username, verbose_level):
    pretty_output("GitHub", username, gh.run_username(username), verbose_level)


def run_email(email, verbose_level):
    pretty_output("GitHub", email, gh.run_email(email), verbose_level)
