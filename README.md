<img src="./assets/img/Assemblr Logo.png" alt="Assemblr Logo"/>

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

## What Makes It Complex?

The Assemblr Emulator project involves several challenging aspects, including:

-   Creation of IDE (Assemblr Compile): #

    -   Develop a complete IDE that supports Assembly Language syntax highlighting

-   Creation of an emulator to translate Assemblr Language to display:

    -   Build an efficient and accurate emulator that can interpret Assembly Language instructions.
    -   Create the emulator modularly so that it can be easily extended to support new features, i.e. supporting an actual hardware device like the [Raspberry Pi](https://raspberrypi.org) or [Arduino](https://arduino.cc).

-   Design progressive puzzles to be written in the language

    -   Create a series of puzzles that teach users how to write Assembly Language code in a fun and engaging way.
    -   Develop a system for tracking user progress and providing feedback on their performance.
    -   Design a system for users to create their own puzzles

## How Does It Work?

### Fetch-Decode-Execute Cycle

### Assemblr Language

<p style="display: none">
- based on OCR instruction set, but can use others through the use of a configuration file
- uses a 16 bit word size
- uses 16 bit addresses
- uses 16 bit values
</p>

#### Instruction Set

| Opcode | Hex    | Dec | Name  | Mnemonic               | Syntax                       | Description                                                                         |
| ------ | ------ | --- | ----- | ---------------------- | ---------------------------- | ----------------------------------------------------------------------------------- |
| 0      | `0000` | 0   | `HLT` | Halt                   | `HLT`                        | Stops the execution of the program                                                  |
| 1      | `0001` | 1   | `STA` | Store                  | `STA <location>`             | Stores the value in the accumulator into memory                                     |
| 2      | `0010` | 2   | `LDA` | Load                   | `LDA <location>`             | Loads a value from memory into the accumulator                                      |
| 3      | `0011` | 3   | `ADD` | Add                    | `ADD <location>`             | Adds a value from memory to the accumulator                                         |
| 4      | `0100` | 4   | `SUB` | Subtract               | `SUB <location>`             | Subtracts a value from memory from the accumulator                                  |
| 5      | `0101` | 5   | `JMP` | Jump                   | `JMP <location>`             | Jumps to the specified memory location                                              |
| 6      | `0110` | 6   | `JGZ` | Jump if greater than 0 | `JGZ <location>`             | Jumps to the specified memory location if the accumulator is greater than 0         |
| 7      | `0111` | 7   | `JLZ` | Jump if less than 0    | `JLZ <location>`             | Jumps to the specified memory location if the accumulator is less than 0            |
| 8      | `1000` | 8   | `JEZ` | Jump if equal to 0     | `JEZ <location>`             | Jumps to the specified memory location if the accumulator is equal to 0             |
| 9      | `1001` | 9   | `JMR` | Jump relative          | `JMR <offset>`               | Jumps to the specified memory location relative to the current instruction location |
| 10     | `1010` | 10  | `OUT` | Output                 | `OUT <location>`             | Outputs the value in the accumulator to the specified port                          |
| 11     | `1011` | 11  | `INP` | Input                  | `INP <location>`             | Inputs a value from the specified port into the accumulator                         |
| 12     | `1100` | 12  | `PWR` | Port Write             | `PWR <port address> <value>` | Writes the specified value to the specified port                                    |
| 13     | `1101` | 13  | `PRD` | Port Read              | `PRD <port address>`         | Reads the value from the specified port into the accumulator                        |

## Registers

| Name                 | Address | Reference   | Read | Write | Description                                               |
| -------------------- | ------- | ----------- | :--: | :---: | --------------------------------------------------------- |
| Accumulator          | 0       | `$ACC`      |  ✔  |  ✔    | Stores the result of arithmetic operations                |
| Null Register        | 1       | `$NUL`      |  ✔  |  ❌   | Stores the value 0                                        |
| Instruction Pointer  | 2       | `$IP`       |  ✔  |  ✔    | Stores the address of the next instruction to be executed |
| Instruction Register | 3       | `$IR`       |  ✔  |  ❌   | Stores the current instruction being executed             |
| Stack Pointer        | 4       | `$SP`       |  ✔  |  ✔    | Stores the address of the top of the stack                |
| Stack                | 5       | `$STK`      |  ✔  |  ✔    | Stores the values pushed to the stack                     |
| Ports                | 6-15    | `$P0`-`$P9` |  ✔  |  ✔    | Stores the values of the ports                            |

