```text
    _    ____ ____  _____ __  __ ____  _          
   / \  / ___/ ___|| ____|  \/  | __ )| |    _ __ 
  / _ \ \___ \___ \|  _| | |\/| |  _ \| |   | '__|
 / ___ \ ___) |__) | |___| |  | | |_) | |___| |   
/_/   \_\____/____/|____Assembly Language Emulator
```
<!-- Version display from ./VERSION -->
[![Version](https://img.shields.io/badge/Version-0.1.1-blue.svg)](

# What is an assembler?
An assembler is a program that takes in assembly code and converts it to machine code. Assembly code is a human-readable representation of machine code, which is a set of instructions that a computer's CPU can execute. Machine code is a sequence of binary numbers that the CPU can execute directly. An assembler is used to convert assembly code to machine code so that it can be executed by the CPU.

## How does mine work?
My assembler works by taking in a file of assembly code and converting it to machine code. It does this by reading the file line by line and converting each line to machine code. It then loads the machine code into memory and runs it using a CPU emulator.

# How to use it?
To use my assembler, create a file with assembly code and save it with a .asr extension. Then run the working_assemblr.py file and it will convert the assembly code to machine code and run it using the CPU emulator.

## How to Write Assembly Code?
Assembly code is made up of instructions and operands. An instruction is a command that tells the CPU what to do, and an operand is a value that the instruction operates on. For example, the ADD instruction adds the value of the operand to the accumulator, which is a special register in the CPU.

Here is the instruction set for my assembler:
| Instruction | Opcode | Description |
| ----------- | ------ | ----------- |
| HLT         | 0x00   | Halt the program |
| SAV         | 0x01   | Save the value in the accumulator to RAM[Address] |
| LDA         | 0x02   | Load the value from RAM[Address] into the accumulator |
| ADD         | 0x03   | Add the value to the accumulator |
| SUB         | 0x04   | Subtract the value from the accumulator |
| OUT         | 0x05   | Output the value in the accumulator to the console |
| INP         | 0x06   | Input a value from the console |
| BAD         | 0x07   | Bitwise AND the value with the accumulator |
| BOR         | 0x08   | Bitwise OR the value with the accumulator |
| BXR         | 0x09   | Bitwise XOR the value with the accumulator |
| BNT         | 0x0A   | Bitwise NOT the accumulator |
| JMP         | 0x0B   | Jump Always to the specified label |
| JEZ         | 0x0C   | Jump to the specified label if the accumulator is equal to zero |
| JGZ         | 0x0D   | Jump to the specified label if the accumulator is greater than zero |
| JLZ         | 0x0E   | Jump to the specified label if the accumulator is less than zero |
| SIG         | 0x0F   | Send a signal to the specified pin (ONLY FOR RASPBERRY PI/MICR0PYTHON) |

### Example Assembly Code:
```assembly
; Example program to add two numbers from user input and output the result
INP
SAV 16 ; Save the first input to RAM address 16
INP
ADD 16 ; Add the second input to the value in RAM address 16
OUT
HLT
```

> **Note:** The assembly code is case-insensitive and can have comments using the `;` character.

> **Note:** Jump instructions currently only support addresses, not labels. (This will be added in a future update)

> **Note:** The SIG instruction is only for use with the Raspberry Pi and MicroPython (This will be removed in a future update, for now it is just a placeholder)

### Example Output:
```bash
$ python working_assemblr.py

Input a value: 5
Input a value: 7
Output: 12
```

## How to Run the Assembler:
To run the assembler, simply run the working_assemblr.py file and it will convert the assembly code to machine code and run it using the CPU emulator.

```bash
python working_assemblr.py
```
# Issues?
If you have any issues or questions, please send me an email at: [jxctno+assemblr@gmail.com](mailto:jxctno+assemblr@gmail.com)

# License
This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

# Acknowledgements
* Little Man Computer - For the inspiration for this project - [LMC](https://peterhigginson.co.uk/LMC/)
* [Python](https://www.python.org/)