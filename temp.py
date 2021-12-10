from pyfiglet import figlet_format as ff
from termcolor import colored

# help(figlet_format)
# help(termcolor)
    # available: red, green, yellow, blue, magenta, cyan, white

valid_colors = ("red", "green", "yellow", "blue", "magenta", "cyan", "white")

message = input("what message do you want to print? Python!!!!\n")
color = input("what color?\n")

def print_art(msg, color):
    if color not in valid_colors:
        color = "magenta"

    ascii_msg = ff(message)
    colored_ascii = colored(ascii_msg, color=color)

    print(colored_ascii)

print_art(message, color)
