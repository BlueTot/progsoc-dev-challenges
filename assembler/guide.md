# Assembly Simulator

_By Nok Hang Lo_

Assembly language is a low-level language which uses human-readable mnemonics to stand for each machine code instruction. It also supports data variables but behind the scenes it just converts these to main memory locations. Assembly language still needs translating into machine code before it can be executed although this is easier that translating high-level languages like Python because each line in assembly corresponds to a single binary machine code instruction.

In this simulator, we experiment with this idea. Our theoretical and simplified assembly language can be assembled into an executable file which can then be run or debugged!

To see the simulator in action try running this code and then:

    entering `view loop.ass`
    entering `assemble loop.ass`
    entering `debug loop.exe`

Then extend the console view and press Enter several times to watch it run through as it counts to 5 with the current assembly instruction being marked in blue.

Can you figure out how the loop is being achieved?

Let's explain our theoretical assembly language mnemonics:

```
STO <var_name> <val> : STOres the given value into the given data variable name (which would be mapped into a main memory location)
ADD <var_name> <val_1> <val_2> : ADDs val_1 to val_2 and stores into the given variable
SUB <var_name> <val_1> <val_2> : SUBtracts val_2 from val_1 and stores into the given variable
DIV <var_name> <val_1> <val_2> : DIVides val_1 by val_2 and stores into the given variable
MUL <var_name> <val_1> <val_2> : MULtiplies val_1 by val_2 and stores into the given variable
POW <var_name> <val_1> <val_2> : Raises val_1 to the POWer of val_2 and stores into the given variable
MOD <var_name> <val_1> <val_2> : Calculates the remainder (MODulus) when val_1 is divided by val_2 and stores into the given variable
FDV <var_name> <val_1> <val_2> : Calculate the Floo DiVision of val_1 and val_2 (i.e. val_1 \ val_2 rounded down) and stores into the given variable

INP <var_name> : INPuts a number from the user and stores into the given variable
OUT <val> : OUTputs the value onto the screen

CMP <val_1> <val_2> : CoMPares the two values and updates the system flags
These flags record if an EQUALS, NOT EQUALS, LESS THAN or GREATER THAN event occurs...
...so that the following BRAnch instructions can then operate on the following line

BEQ <line_num> : Branch (i.e. jump) to the given line number if the EQuals flag is set
BNE <line_num> : Branch to the given line number if the Not EQuals flag is set
BGT <line_num> : Branch to the given line number if the Greater Than flag is set
BLT <line_num> : Branch to the given line number if the Less Than flag is set

HLT : HALts the program to end it
```
The values referred to above can all be numerical values (whole numbers or decimals) or they can be references to existing variables.

NOW AFTER ALL THAT INTRODUCTORY FUN, HERE'S SOME CHALLENGES FOR YOU THEN!
## Task 1

Currently the command run loops.exe will generate a command not found error even once loops.ass has been assembled. Fix this so you can also run your exe files!
## Task 2

When debugging, the blue current line is still not perfectly clear. Change the code to also show a blue arrow to the left of the line number to mark more clearly which line is currently selected by the debugger.
## Task 3

Complete the assembly code given to evaluate the expression x = (5 * (3 + 4)) ^ 2 - 7 and print x where ^ means the power/exponential operator.
## Task 4

Find the bug in the assembly code given in task3.ass that is meant to calculate the sum of the first N natural numbers including N. For example the output should be 6 (1+2+3) if the user enters 3 but this isn't working if you try it.
## Extensions

- Find in the bug in the assembly code given in ext.ass that is meant to detect if a number is prime or not.
- Processors support registers which are super high-fast small memories inside the processor. There are a batch of general purpose registers e.g. R1, R2, ... which you should be able to use to hold calculation results to avoid reading and writing to main memory as often which is slower. See what you can find out about registers. Could you add support for 8 general purpose registers to our theoretical assembly language? You should add support to load (LDA) from a main memory variable into one of these registers as well as storing (STO) from a register to a main memory variable.
- One special purpose register in a processor is called the Accumulator and the results of all numerical calculations are always written first to the accumulator in fact. Could you remove the <var_name> operand from all the arithmetic instructions and write the results of the calculations to an accumulator register instead?
- What else can you find out and change to make our theoretical assembly language more closely represent that of a real processor?

