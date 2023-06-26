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

![Emulation Display](https://raw.githubusercontent.com/joshua-cotugno/Assemblr/main/README-resources/display.svg?token=GHSAT0AAAAAACEIBKQDHAQLIR7AT2C7K56IZEZVMAA)

## What Makes It Complex?
The Assemblr Emulator project involves several challenging aspects, including:

- Creation of IDE (Assemblr Compile): #
    - Develop a complete IDE that supports Assembly Language syntax highlighting
- Creation of an emulator to translate Assemblr Language to display:
    - Build an efficient and accurate emulator that can interpret Assembly Language instructions and render the corresponding output on the 512 x 64 bit display.

- Design progressive puzzles to be written in the language

<br><br>
****

## Instruction Set
| Number |      |   | Opcode | Instruction            | Syntax                                           | Description                                             |
|--------|------|---|--------|------------------------|--------------------------------------------------|---------------------------------------------------------|
| 0      | `0000` | 0 | `HLT`    | Halt                   | `HLT`                                              | Stops the execution of the program                      |
| 1      | `0001` | 1 | `STA`    | Store                  | `STA <location>`                                   | Stores the value in the accumulator into memory         |
| 2      | `0010` | 2 | `LDA`    | Load                   | `LDA <location>`                                   | Loads a value from memory into the accumulator          |
| 3      | `0011` | 3 | `SEG`    | Set Group              | `SEG <group name>` <location start>` <location end>` | Sets a group of memory locations                        |
| 4      | `0100` | 4 | `APG`    | Append to Group        | `APG <group name>` <int>`                           | Appends a value to a group of memory locations           |
| 5      | `0101` | 5 | `RMG`    | Remove from Group      | `RMG <group name>` <int>`                           | Removes a value from a group of memory locations         |
| 6      | `0110` | 6 | `SGR`    | Shift Group Right      | `SHG <group name>`                                 | Shifts a group of memory locations to the right          |
| 7      | `0111` | 7 | `SGL`    | Shift Group Left       | `SGL <group name>`                                 | Shifts a group of memory locations to the left           |
| 8      | `1000` | 8 | `DLG`    | Delete Group           | `DLG <group name>`                                 | Deletes a group of memory locations                      |
| 9      | `1001` | 9 | `ADD`    | Add                    | `ADD <int>`                                        | Adds the value in the accumulator to another value      |
| 10     | `1010` | A | `SUB`    | Subtract               | `SUB <int>`                                        | Subtracts a value from the accumulator                  |
| 11     | `1011` | B | `JMP`    | Jump always            | `JMP <addr>`                                       | Jumps unconditionally to a specified memory address     |
| 12     | `1100` | C | `JEZ`    | Jump if Equal to `0`     | `JEZ <addr>`                                       | Jumps to a specified memory address if accumulator is `0` |
| 13     | `1101` | D | `JGZ`    | Jump if Greater than `0` | `JGZ <addr>`                                       | Jumps to a specified memory address if accumulator >` `0`  |
| 14     | `1110` | E | `JLZ`    | Jump is Less than `0`    | `JLZ <addr>`                                       | Jumps to a specified memory address if accumulator < `0`  |
| 15     | `1111` | F | `SIG`    | Send Signal            | `SIG <signal> <x> <y>` <port>`                              | Sends a signal to a port                                |



