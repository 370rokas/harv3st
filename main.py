"""
██╗░░██╗░█████╗░██████╗░██╗░░░██╗██████╗░░██████╗████████╗
██║░░██║██╔══██╗██╔══██╗██║░░░██║╚════██╗██╔════╝╚══██╔══╝
███████║███████║██████╔╝╚██╗░██╔╝░█████╔╝╚█████╗░░░░██║░░░
██╔══██║██╔══██║██╔══██╗░╚████╔╝░░╚═══██╗░╚═══██╗░░░██║░░░
██║░░██║██║░░██║██║░░██║░░╚██╔╝░░██████╔╝██████╔╝░░░██║░░░
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═════╝░╚═════╝░░░░╚═╝░░░

370rokas (c) 2022
https://github.com/370rokas

main.py - the main file... literally..
"""

import argparse
parser = argparse.ArgumentParser(description="Harvests various websites for information about an username or an email.")
parser.add_argument('--username', metavar="u", type=str, help="username to harvest", nargs='+')
parser.add_argument('--email', metavar="e", type=str, help="email to harvest", nargs='+')
parser.add_argument('--verbose', '-v', action='count', default=0)

from harvester import run_username, run_email
from misc import banner
from colorama import Fore


def main():
    args = parser.parse_args()
    print(Fore.RED + banner + "\n370rokas (c) 2022\n" + Fore.RESET)

    if not args.username and not args.email:
        parser.print_help()
        return

    verbose_level = args.verbose

    if args.username:
        # Harvest by usernames
        for username in args.username:
            print(Fore.CYAN + f"[{username}] Harvesting started." + Fore.RESET)
            run_username(username, verbose_level)
            print(Fore.CYAN + f"[{username}] Harvesting finished." + Fore.RESET)

    if args.email:
        # Harvest by emails
        for email in args.email:
            print(Fore.CYAN + f"[{email}] Harvesting started." + Fore.RESET)
            run_email(email, verbose_level)
            print(Fore.CYAN + f"[{email}] Harvesting finished." + Fore.RESET)


if __name__ == '__main__':
    main()
