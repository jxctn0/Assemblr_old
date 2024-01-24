# Assemblr Emulator
_The Assemblr Emulator is a game designed to teach people the fundamentals of Assembly Language programming. It provides a platform for users to learn and practice Assembly Language concepts through a series of set puzzles and projects._

## Set Puzzles
The game is divided into different sets of puzzles, each increasing in difficulty. These sets are categorized as follows:

### Tutorial
The tutorial section provides an introduction to Assembly Language programming. Users will be guided through step-by-step instructions on how to write simple Assembly code and execute it within the emulator.

### Basic Projects
In this section, users will be given basic projects to complete using Assembly Language. These projects will challenge their understanding of core concepts and encourage them to apply their knowledge in practical scenarios.

### Intermediate
The intermediate section offers more complex challenges that require a deeper understanding of Assembly Language. Users will tackle advanced programming problems and implement more sophisticated algorithms.

## UI
_The Assemblr Emulator consists of two main components:_

### IDE/Console
The IDE (Integrated Development Environment) provides a user-friendly interface for writing Assembly Language code. It offers features such as syntax highlighting, code suggestions, and error checking to assist users in their programming tasks. The console allows users to execute their code and view the program's output or any error messages.

### Emulation Display
The emulator's display simulates a 512 x 64 bit screen, which can be manipulated using the SIG command. Users can interact with the display by writing Assembly code that controls the pixels and colors on the screen. This provides a visual representation of their programs and allows for experimentation and creativity.

![Emulation Display](https://raw.githubusercontent.com/joshua-cotugno/Assemblr/main/README-resources/display.svg)

## What Makes It Complex?
The Assemblr Emulator project involves several challenging aspects, including:

- Creation of IDE (Assemblr Compile): #
    - Develop a complete IDE that supports Assembly Language syntax highlighting
- Creation of an emulator to translate Assemblr Language to display:
    - Build an efficient and accurate emulator that can interpret Assembly Language instructions and render the corresponding output on the 512 x 64 bit display.

- Design progressive puzzles to be written in the language

<br><br><br><br><br><br><br><br>
****
****
## Parts of the "Emulator"

### RAM
*_Random Access Memory_*
- Contains
### ROM
*_Read Only Memory_*
<br><br>
## Instruction Set

Opcode | Instruction | Parameters | Description
------------|------------|------------|------------
`0000` | `HLT` | `-` | Halts all operations, resets system
`0001` | `SAV` | `-` | Saves the value in the accumulator to RAM
`0010` | `LDA` | `Address` | Loads the value from RAM[Address] into the accumulator
`0011` | `ADD` | `Value` | Adds the value to the accumulator
`0100` | `SUB` | `Value` | Subtracts the value from the accumulator
`0101` | `JMP` | `Label` | Jump Always to the specified label 
`0110` | `JEZ` | `Label` | Jump to the specified label if the accumulator is equal to zero
`0111` | `JGZ` | `Label` | Jump to the specified label if the accumulator is greater than zero
`1000` | `JLZ` | `Label` | Jump to the specified label if the accumulator is less than zero
`1001` | `INP` | `Pin` | Input a value from the specified pin (ONLY FOR RASPBERRY PI/MICR0PYTHON)/ Console
`1010` | `OUT` | `-` | Output the value in the accumulator to the console
`1011` | `SIG` | `Pin, Value` | Send a signal to the specified pin (ONLY FOR RASPBERRY PI/MICR0PYTHON)
`1100` | `BAD` | `Value` | Bitwise AND the value with the accumulator
`1101` | `BOR` | `Value` | Bitwise OR the value with the accumulator
`1110` | `BXR` | `Value` | Bitwise XOR the value with the accumulator
`1111` | `BNT` | `-` | Bitwise NOT the accumulator
`0000` | `DLY` | `Cycles` | Delay for a specified number of cycles