"""
██╗░░██╗░█████╗░██████╗░██╗░░░██╗██████╗░░██████╗████████╗
██║░░██║██╔══██╗██╔══██╗██║░░░██║╚════██╗██╔════╝╚══██╔══╝
███████║███████║██████╔╝╚██╗░██╔╝░█████╔╝╚█████╗░░░░██║░░░
██╔══██║██╔══██║██╔══██╗░╚████╔╝░░╚═══██╗░╚═══██╗░░░██║░░░
██║░░██║██║░░██║██║░░██║░░╚██╔╝░░██████╔╝██████╔╝░░░██║░░░
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═════╝░╚═════╝░░░░╚═╝░░░

370rokas (c) 2022
https://github.com/370rokas

misc.py - Random stuff, mainly graphical/aesthetic stuff
"""

banner = f'''                                         
@@@  @@@  @@@@@@  @@@@@@@  @@@  @@@ @@@@@@   @@@@@@ @@@@@@@ 
@@!  @@@ @@!  @@@ @@!  @@@ @@!  @@@     @@! !@@       @!!   
@!@!@!@! @!@!@!@! @!@!!@!  @!@  !@!  @!!!:   !@@!!    @!!   
!!:  !!! !!:  !!! !!: :!!   !: .:!      !!:     !:!   !!:   
 :   : :  :   : :  :   : :    ::    ::: ::  ::.: :     :    '''


def pretty_output(title, name, stuff, verbose_level):
    from colorama import Fore

    if stuff["Found"]:
        print(Fore.GREEN + f"[{name}] - {title} - Found." + Fore.RESET)
        null_values = []

        for data_i, data_v in stuff["Data"].items():
            if data_v is None or (type(data_v) == str and data_v == ""):
                null_values.append(data_i)
            else:
                print(Fore.GREEN + f"-- {data_i} - {data_v}")

        if verbose_level > 0:
            for null_val in null_values:
                print(Fore.YELLOW + f"-- {null_val} - null")

    else:
        print(Fore.RED + f"[{name}] - {title} - Not Found." + Fore.RESET)
