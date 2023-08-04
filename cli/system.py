# imports
import json
import os
import time
# import local modules
import cli, app

"""
INSTRUCTION SET
+--------+---+--------+------------------------+----------------------------------+--------------------------------------------------------------------------+
|        |   | Opcode | Instruction            | Syntax                           | Description                                                              |
+--------+---+--------+------------------------+----------------------------------+--------------------------------------------------------------------------+
| `0000` | 0 | `HLT`  | Halt                   | `HLT`                            | Stops the execution of the program                                       |
| `0001` | 1 | `SAV`  | Store                  | `SAV <location>`                 | Stores the value in the accumulator into memory                          |
| `0010` | 2 | `LDA`  | Load                   | `LDA <location>`                 | Loads a value from memory into the accumulator                           |
| `0011` | 3 | `ADD`  | Add                    | `ADD <int>`                      | Adds the value in the accumulator to another value                       |
| `0100` | 4 | `SUB`  | Subtract               | `SUB <int>`                      | Subtracts a value from the accumulator                                   |
| `0101` | 5 | `JMP`  | Jump always            | `JMP <addr>`                     | Jumps unconditionally to a specified memory address                      |
| `0110` | 6 | `JEZ`  | Jump if Equal to 0     | `JEZ <addr>`                     | Jumps to a specified memory address if accumulator is 0                  |
| `0111` | 7 | `JGZ`  | Jump if Greater than 0 | `JGZ <addr>`                     | Jumps to a specified memory address if accumulator >` 0                  |
| `1000` | 8 | `JLZ`  | Jump is Less than 0    | `JLZ <addr>`                     | Jumps to a specified memory address if accumulator < 0                   |
| `1001` | 9 | `INP`  | Input                  | `INP <port>`                     | Read input from console to accumulator                                   |
| `1010` | A | `OUT`  | Output                 | `OUT`                            | Outputs to console                                                       |
| `1011` | B | `SIG`  | Send Signal            | `SIG <signal> <strength> <addr>` | Sends a signal to a peripheral address                                   |
| `1100` | C | `BAD`  | Bitwise AND            | `AND <int>`                      | Performs a bitwise AND on a given operand & the value in the accumulator |
| `1101` | D | `BOR`  | Bitwise OR             | `BOR <int>`                      | Performs a bitwise OR on a given operand & the value in the accumulator  |
| `1110` | E | `BXR`  | Bitwise XOR            | `BXR <int>`                      | Performs a bitwise XOR on a given operand & the value in the accumulator |
| `1111` | F | `DLY`  | Delay                  | `DLY <int>`                      | Delays processing by operand                                             |
+--------+---+--------+------------------------+----------------------------------+--------------------------------------------------------------------------+



Instruction set JSON schema:
"OPCODE": {
    "opcode": ["bin", "hex", dec],
    "operands": 0,
    "description": "description",
    "function": function
}
"""

class operations:
    def HLT():
        if app.VERBOSE:
            cli.notify.info("HLT")
        exit(0)
    
    def SAV(location):
        if app.VERBOSE:
            cli.notify.info("SAV")
        app.registers.cache[location] = app.registers.accumulator

    def LDA(location):
        if app.VERBOSE:
            cli.notify.info("LDA")
        app.registers.accumulator = app.registers.cache[location]

    def ADD(value):
        if app.VERBOSE:
            cli.notify.info("ADD")
        app.registers.accumulator += value
    
    def SUB(value):
        if app.VERBOSE:
            cli.notify.info("SUB")
        app.registers.accumulator -= value

    def JMP(address):
        if app.VERBOSE:
            cli.notify.info("JMP")
        app.registers.line_counter = address
    
    def JEZ(address):
        if app.VERBOSE:
            cli.notify.info("JEZ")
        if app.registers.accumulator == 0:
            app.registers.line_counter = address
    
    def JGZ(address):
        if app.VERBOSE:
            cli.notify.info("JGZ")
        if app.registers.accumulator > 0:
            app.registers.line_counter = address
    
    def JLZ(address):

        if app.VERBOSE:
            cli.notify.info("JLZ")
        if app.registers.accumulator < 0:
            app.registers.line_counter = addresses[address]
    
    def INP(port):
        if app.VERBOSE:
            cli.notify.info("INP")
        app.registers.accumulator = input(port)
    

    def OUT():
        if app.VERBOSE:
            cli.notify.info("OUT")
        print(app.registers.accumulator)

    def SIG(signal, strength, address):
        if app.VERBOSE:
            cli.notify.info("SIG")

    def BAD(value):
        if app.VERBOSE:
            cli.notify.info("BAD")
        app.registers.accumulator &= value

    def BOR(value):
        if app.VERBOSE:
            cli.notify.info("BOR")
        app.registers.accumulator |= value

    def BXR(value):
        if app.VERBOSE:
            cli.notify.info("BXR")
        app.registers.accumulator ^= value

    def DLY(value):
        if app.VERBOSE:
            cli.notify.info("DLY")
        time.sleep(value)

# INSTUCTION SET
INSTRUCTION_SET = {
    "HLT": {
        # Halts the program completely, exiting with code 0
        "opcode": ["0000", "0", 0],
        "operands": 0,
        "description": "Halt",
        "function": operations.HLT
    },
    "SAV": {
        # Stores the value in the accumulator into a given memory address
        "opcode": ["0001", "1", 1],
        "operands": 1,
        "description": "Store",
        "function": operations.SAV
    },
    "LDA": {
        # Loads a value from a specific memory address into the accumulator
        "opcode": ["0010", "2", 2],
        "operands": 1,
        "description": "Load",
        "function": operations.LDA
    }, 
    "ADD": {
        # Adds a given value to the accumulator
        "opcode": ["0011", "3", 3],
        "operands": 1,
        "description": "Add",
        "function": operations.ADD
    },
    "SUB": {
        # Subtracts a given value from the accumulator
        "opcode": ["0100", "4", 4],
        "operands": 1,
        "description": "Subtract",
        "function": operations.SUB
    },
    "JMP": {
        # Jumps to a given instruction address
        "opcode": ["0101", "5", 5],
        "operands": 1,
        "description": "Jump always",
        "function": operations.JMP
    },
    "JEZ": {
        # Jumps to a given instruction address only if the accumulator is 0
        "opcode": ["0110", "6", 6],
        "operands": 1,
        "description": "Jump if Equal to 0",
        "function": operations.JEZ
    },
    "JGZ": {
        # Jumps to a given instruction address only if the accumulator is greater than 0
        "opcode": ["0111", "7", 7],
        "operands": 1,
        "description": "Jump if Greater than 0",
        "function": operations.JGZ
    },
    "JLZ": {
        # Jumps to a given instruction address only if the accumulator is less than 0
        "opcode": ["1000", "8", 8],
        "operands": 1,
        "description": "Jump is Less than 0",
        "function": operations.JLZ
    },
    "INP": {
        # Takes input from the console and stores it in the accumulator
        "opcode": ["1001", "9", 9],
        "operands": 1,
        "description": "Input",
        "function": operations.INP
    }, 
    "OUT": {
        # Outputs the value in the accumulator to the console
        "opcode": ["1010", "A", 10],
        "operands": 0,
        "description": "Output",
        "function": operations.OUT
    },
    "SIG": {
        # Sends a signal to a peripheral address
        # A signal is either a hex value or a 8-bit binary value
        # A signal strength is a hex value between 0 and 15
        # A peripheral address is a 4-bit binary value or a hex value between 0 and f
        # Syntax: SIG <signal> <strength> <addr>
        "opcode": ["1011", "B", 11],
        "operands": 3,
        "description": "Send Signal",
        "function": operations.SIG
    },
    "BAD": {
        # Performs a bitwise AND on a given operand & the value in the accumulator
        "opcode": ["1100", "C", 12],
        "operands": 1,
        "description": "Bitwise AND",
        "function": operations.BAD
    },
    "BOR": {
        # Performs a bitwise OR on a given operand & the value in the accumulator
        "opcode": ["1101", "D", 13],
        "operands": 1,
        "description": "Bitwise OR",
        "function": operations.BOR
    },
    "BXR": {
        # Performs a bitwise XOR on a given operand & the value in the accumulator
        "opcode": ["1110", "E", 14],
        "operands": 1,
        "description": "Bitwise XOR",
        "function": operations.BXR
    },
    "DLY": {
        # Delays processing by a given value
        "opcode": ["1111", "F", 15],
        "operands": 1,
        "description": "Delay",
        "function": operations.DLY
    }
}


# system.operands[function]["function"](number)