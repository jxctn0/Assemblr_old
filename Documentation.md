# Assemblr Documentation

## Opcodes
|          |          | **Opcode** | **Instruction**        | **Syntax**                       | **Description**                                                          |
|----------|----------|------------|------------------------|----------------------------------|--------------------------------------------------------------------------|
| `0000`   | 0        | `HLT`      | Halt                   | `HLT`                            | Stops the execution of the program                                       |
| `0001`   | 1        | `SAV`      | Store                  | `SAV <location>`                 | Stores the value in the accumulator into memory                          |
| `0010`   | 2        | `LDA`      | Load                   | `LDA <location>`                 | Loads a value from memory into the accumulator                           |
| `0011`   | 3        | `ADD`      | Add                    | `ADD <int>`                      | Adds the value in the accumulator to another value                       |
| `0100`   | 4        | `SUB`      | Subtract               | `SUB <int>`                      | Subtracts a value from the accumulator                                   |
| `0101`   | 5        | `JMP`      | Jump always            | `JMP <addr>`                     | Jumps unconditionally to a specified memory address                      |
| `0110`   | 6        | `JEZ`      | Jump if Equal to 0     | `JEZ <addr>`                     | Jumps to a specified memory address if accumulator is 0                  |
| `0111`   | 7        | `JGZ`      | Jump if Greater than 0 | `JGZ <addr>`                     | Jumps to a specified memory address if accumulator >` 0                  |
| `1000`   | 8        | `JLZ`      | Jump is Less than 0    | `JLZ <addr>`                     | Jumps to a specified memory address if accumulator < 0                   |
| `1001`   | 9        | `INP`      | Input                  | `INP <port>`                     | Read input from console to accumulator                                   |
| `1010`   | A        | `OUT`      | Output                 | `OUT`                            | Outputs to console                                                       |
| `1011`   | B        | `SIG`      | Send Signal            | `SIG <signal> <strength> <addr>` | Sends a signal to a peripheral address                                   |
| `1100`   | C        | `BAD`      | Bitwise AND            | `AND <int>`                      | Performs a bitwise AND on a given operand & the value in the accumulator |
| `1101`   | D        | `BOR`      | Bitwise OR             | `BOR <int>`                      | Performs a bitwise OR on a given operand & the value in the accumulator  |
| `1110`   | E        | `BXR`      | Bitwise XOR            | `BXR <int>`                      | Performs a bitwise XOR on a given operand & the value in the accumulator |
| `1111`   | F        | `DLY`      | Delay                  | `DLY <int>`                      | Delays processing by operand                                             |

## How the emulator works

# Version Alpha 0.0.1
Assumes that each file is in "ROM" (_.asrom_) which is directly accessible to the CPU, similar to a Game Cartridge for a N64