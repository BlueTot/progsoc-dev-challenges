from assembler_utils import Assembler, AssemblySimulation
import os

files = {

    # Demo code file to demonstrate a loop
    "loop.ass": """
    STO i 1
    CMP i 6
    BLT 4
    BAL 7
    OUT i
    ADD i i 1
    BAL 1
    HLT
""",

    # ==> TASK 3: Complete the assembly code below to evaluate the expression x = (5 * (3 + 4)) ^ 2 - 7 and print x.
    "task2.ass": """
    ADD num 3 4
    MUL num ____ _____
    POW ____ ____ 2
    SUB ____ num ____
    OUT num
    HLT
""",

    # ==> TASK 4: Find the bug in the assembly code below that calculates the sum of the first N natural numbers including N
    # e.g. the output should be 6 (1+2+3) if the user enters 3.
    "task3.ass": """
    STO sum 0
    INP n
    STO i 1
    ADD x n 1
    CMP i x
    BLT 7
    BAL 10
    ADD sum sum i
    ADD i i 2
    BAL 4
    OUT sum
    HLT
""",

    # ==> EXTENSION TASK: Find the bug in the assembly code below that tests if a number is prime.
    "ext.ass": """
    INP num
    STO prime 1
    STO i 2
    CMP i num
    BLT 6
    BAL 15
    MOD x num i
    CMP 10 x
    BEQ 10
    BAL 13
    STO prime 0
    BAL 9
    BAL 13
    ADD i i 1
    BAL 3
    OUT prime
    HLT
""",

}

DEFAULT_COLOUR = "black"
BLUE_ARROW_EMOJI = "\U000027A1"


class Colours:  # Colour Rendering Class

    # Colours dictionary
    COLOURS = {'black': 30, 'red': 31, 'green': 32, 'yellow': 33,
               'blue': 34, 'magenta': 35, 'cyan': 36, 'white': 37}

    @staticmethod
    def colour_text(text, colour):
        # Function to print coloured text using ANSI terminal codes
        return f'\033[{Colours.COLOURS[colour]};1;1m{text}\033[0m'


def print_assembly(assembly):
    for ln, line in enumerate(assembly.strip().splitlines()):
        print(Colours.colour_text(f"{ln:^3}", "cyan") + f"{line.strip()}")


def print_header():  # Function to print the instructions on how to use the program
    print("\nCOMMANDS:")
    print("\t Viewing code: view <filename>")
    print("\t Assembling code: assemble <filename>.py")
    print("\t Running code: run <filename>.exe")
    print("\t Debug code: debug <filename>.exe")
    print("\t Quit the program: exit\n")
    print(f"YOUR CURRENT FILES: {' '.join([k for k in files.keys()])}\n")


def view_code(filename):
    if filename not in files:  # If file doesn't exist
        raise FileNotFoundError(f"File '{filename}' not found")
    elif ".ass" in filename:  # assembly file
        print_assembly(files[filename])
    else:
        print("unable to look at machine code contents in this simulator!")


def assemble_code(filename):  # Function to compile code
    if filename not in files:  # If file doesn't exist
        raise FileNotFoundError(f"File '{filename}' not found")
    elif ".ass" not in filename:  # If file is of the wrong type
        raise FileNotFoundError(f"Only .ass files can be assembled")
    assembly = Assembler.assemble_code(files[filename])
    files[f"{filename.replace('.ass', '')}.exe"] = assembly
    print(Colours.colour_text(
        f"{filename} assembled sucessfully into {filename.replace('.ass', '')}.exe", "green"))


def run_code(filename):  # Function to run code
    if filename not in files:  # If file doesn't exist
        raise FileNotFoundError(f"File '{filename}' not found")
    elif ".exe" not in filename:  # If file is of the wrong type
        raise FileNotFoundError(f"Only .exe files can be executed")
    simulation = AssemblySimulation()
    for _ in simulation.execute_assembly_code(files[filename], input, print):
        pass


# Function to render debug environment after each pass of the debugger
def render_debug_environment(assembly, curr_line_num, variables, status_register, output):
    os.system("cls")
    print(Colours.colour_text(
        f"{'='*20}\nDEBUGGER\n{'='*20}\n", "cyan"))
    print(Colours.colour_text("ASSEMBLY: \n", DEFAULT_COLOUR))
    for linenum, line in assembly.items():
        # ==> TASK 2: Show a blue arrow to the left of the line number to mark more clearly which line is currently selected by the debugger.
        prefix = '   '
        if linenum == curr_line_num:
            line = Colours.colour_text(line, "blue")
        debug_line = prefix + \
            Colours.colour_text(f"{linenum:^3}", "cyan") + f"{line}"
        print(debug_line)
    print(Colours.colour_text("\nVARIABLES: \n", DEFAULT_COLOUR))
    for var, contents in variables.items():
        print(f"{var}: {contents}")
    print(Colours.colour_text("\nLAST COMPARISON STATUS: \n", DEFAULT_COLOUR))
    for tag, val in zip(("Equal", "Not Equal", "Greater Than", "Less Than"), status_register):
        print(f"{tag}: {val}")
    print(Colours.colour_text("\nOUTPUT: \n", DEFAULT_COLOUR))
    for line in output:
        print(line)
    print()


def debug_code(filename):  # Function to debug code
    if filename not in files:  # If file doesn't exist
        raise FileNotFoundError(f"File '{filename}' not found")
    elif ".exe" not in filename:  # If file is of the wrong type
        raise FileNotFoundError(f"Only .exe files can be simulated")
    simulation = AssemblySimulation()
    assembly = files[filename]
    for ln, variables, status_register, output in simulation.execute_assembly_code(assembly, input, print, debug=True):
        render_debug_environment(
            assembly, ln, variables, status_register, output)
        check = input(Colours.colour_text(
            "Press enter to continue or q to quit: ", "green"))
        if check.lower() == "q":
            break


# Main part of code
while True:

    print_header()  # Print the header

    try:

        command = input(Colours.colour_text(">>> ", "cyan")).lower().split(" ")

        # ==> TASK 1: Add another if statement to run the code file when the user enters the keyword "run"
        if command[0] == "exit":  # Exit command
            break
        elif command[0] == "view":  # View command
            view_code(command[1])
        elif command[0] == "assemble":  # Assemble command
            assemble_code(command[1])
        elif command[0] == "debug":  # Debug command
            debug_code(command[1])
        else:
            print(Colours.colour_text("Command not found", "red"))

    except FileNotFoundError as err:
        # Print any errors that occur
        print(Colours.colour_text(str(err), "red"))

    print("\n"+"="*100)

