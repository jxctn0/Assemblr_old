# Assemblr Documentation



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



