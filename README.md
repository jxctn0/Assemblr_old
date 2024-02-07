```

 █████╗  ██████╗ ██████╗███████╗███╗   ███╗██████╗ ██╗     ██████╗ 
██╔══██╗██╔════╝██╔════╝██╔════╝████╗ ████║██╔══██╗██║     ██╔══██╗
███████║╚█████╗ ╚█████╗ █████╗  ██╔████╔██║██████╦╝██║     ██████╔╝
██╔══██║ ╚═══██╗ ╚═══██╗██╔══╝  ██║╚██╔╝██║██╔══██╗██║     ██╔══██╗
██║  ██║██████╔╝██████╔╝███████╗██║ ╚═╝ ██║██████╦╝███████╗██║  ██║
╚═╝  ╚═╝╚═════╝ ╚═════╝ ╚══════╝╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
                                 Assembly Language Learning Program

```

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

`<br><br>``<br><br>`

---

---

## Parts of the "Emulator"

### RAM
<<<<<<< HEAD

*_Random Access Memory_*

- Contains the currently running program, and the data for that program. Will ont save between runtimes

### CPU

*_Central Processing Unit_*

## Instruction Set

Based off of the Little Man Computer IS, but has a few extra commands to interface with "Peripherals"

| Number |          |   | Opcode  | Instruction                | Syntax                                                   | Description                                                 |
| ------ | -------- | - | ------- | -------------------------- | -------------------------------------------------------- | ----------------------------------------------------------- |
| 0      | `0000` | 0 | `HLT` | Halt                       | `HLT`                                                  | Stops the execution of the program                          |
| 1      | `0001` | 1 | `STA` | Store                      | `STA <location>`                                       | Stores the value in the accumulator into memory             |
| 2      | `0010` | 2 | `LDA` | Load                       | `LDA <location>`                                       | Loads a value from memory into the accumulator              |
| 3      | `0011` | 3 | `SEG` | Set Group                  | `SEG <group name>` `<location start> <location end>` | Sets a group of memory locations                            |
| 4      | `0100` | 4 | `APG` | Append to Group            | `APG <group name>` ```<int>````                      | Appends a value to a group of memory locations              |
| 5      | `0101` | 5 | `RMG` | Remove from Group          | `RMG <group name>` ```<int>````                      | Removes a value from a group of memory locations            |
| 6      | `0110` | 6 | `SGR` | Shift Group Right          | `SHG <group name>`                                     | Shifts a group of memory locations to the right             |
| 7      | `0111` | 7 | `SGL` | Shift Group Left           | `SGL <group name>`                                     | Shifts a group of memory locations to the left              |
| 8      | `1000` | 8 | `DLG` | Delete Group               | `DLG <group name>`                                     | Deletes a group of memory locations                         |
| 9      | `1001` | 9 | `ADD` | Add                        | `ADD <int>`                                            | Adds the value in the accumulator to another value          |
| 10     | `1010` | A | `SUB` | Subtract                   | `SUB <int>`                                            | Subtracts a value from the accumulator                      |
| 11     | `1011` | B | `JMP` | Jump always                | `JMP <addr>`                                           | Jumps unconditionally to a specified memory address         |
| 12     | `1100` | C | `JEZ` | Jump if Equal to `0`     | `JEZ <addr>`                                           | Jumps to a specified memory address if accumulator is `0` |
| 13     | `1101` | D | `JGZ` | Jump if Greater than `0` | `JGZ <addr>`                                           | Jumps to a specified memory address if accumulator >0`      |
| 14     | `1110` | E | `JLZ` | Jump is Less than `0`    | `JLZ <addr>`                                           | Jumps to a specified memory address if accumulator <`0`   |
| 15     | `1111` | F | `SIG` | Send Signal                | `SIG <signal> <x> <y>` ```<port>````                 | Sends a signal to a port                                    |

## Program Error Codes
*_Error Codes _*

| Code | Name | Description |
| ---- | ---- | ----------- |
| 0 | `NO_ERROR` | No error |
| 1 | `INVALID_OPCODE` | Invalid opcode |
| 2 | `INVALID_ADDRESS` | Invalid address |
| 3 | `INVALID_VALUE` | Invalid value |
| 4 | `INVALID_PORT` | Invalid port ID |
=======
*_Random Access Memory_*
- Contains
### ROM
*_Read Only Memory_*
<br><br>
## Instruction Set

| Opcode | Instruction | Parameters | Description                                                                       |
| ------ | ----------- | ---------- | --------------------------------------------------------------------------------- |
| `0000` | `HLT`       | `-`        | Halts all operations, resets system                                               |
| `0001` | `SAV`       | `Address`  | Saves the value in the accumulator to RAM                                         |
| `0010` | `LDA`       | `Address`  | Loads the value from RAM[Address] into the accumulator                            |
| `0011` | `ADD`       | `Value`    | Adds the value to the accumulator                                                 |
| `0100` | `SUB`       | `Value`    | Subtracts the value from the accumulator                                          |
| `0101` | `JMP`       | `Label`    | Jump Always to the specified label                                                |
| `0110` | `JEZ`       | `Label`    | Jump to the specified label if the accumulator is equal to zero                   |
| `0111` | `JGZ`       | `Label`    | Jump to the specified label if the accumulator is greater than zero               |
| `1000` | `JLZ`       | `Label`    | Jump to the specified label if the accumulator is less than zero                  |
| `1001` | `INP`       | `Pin`      | Input a value from the specified pin (ONLY FOR RASPBERRY PI/MICR0PYTHON)/ Console |
| `1010` | `OUT`       | `-`        | Output the value in the accumulator to the console                                |
| `1011` | `SIG`       | `Pin`      | Send a signal to the specified pin (ONLY FOR RASPBERRY PI/MICR0PYTHON)            |
| `1100` | `BAD`       | `Value`    | Bitwise AND the value with the accumulator                                        |
| `1101` | `BOR`       | `Value`    | Bitwise OR the value with the accumulator                                         |
| `1110` | `BXR`       | `Value`    | Bitwise XOR the value with the accumulator                                        |
| `1111` | `BNT`       | `-`        | Bitwise NOT the accumulator                                                       |
| `0000` | `DLY`       | `Cycles`   | Delay for a specified number of cycles                                            |

<br><br>

#### Test Program
test program that tests all the instructions
```assembler
; Without Jumps
ADD 3 ; Add 3 to the accumulator
SUB 2 ; Subtract 2 from the accumulator
SAV 4 ; Save the accumulator to RAM[4]
OUT
SIG 1 ; Send a signal to pin 1
BAD 23 ; Bitwise AND the accumulator with 23
OUT
BOR 38 ; Bitwise OR the accumulator with 38
OUT
BXR 12 ; Bitwise XOR the accumulator with 12
OUT
BNT ; Bitwise NOT the accumulator
OUT
LDA 4 ; Load RAM[4] into the accumulator
OUT
HLT
```
>>>>>>> 726275daead98c15be28176162a2e27f2961a45b
