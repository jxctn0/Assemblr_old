import os
import time, math

verbose = "ei"

colors = {
    "foreground": {
        "black": "\u001b[30m",
        "red": "\u001b[31m",
        "green": "\u001b[32m",
        "yellow": "\u001b[33m",
        "blue": "\u001b[34m",
        "purple": "\u001b[35m",
        "cyan": "\u001b[36m",
        "white": "\u001b[37m",
    },
    "background": {
        "black": "\u001b[40m",
        "red": "\u001b[41m",
        "green": "\u001b[42m",
        "yellow": "\u001b[43m",
        "blue": "\u001b[44m",
        "purple": "\u001b[45m",
        "cyan": "\u001b[46m",
        "white": "\u001b[47m",
    },
    "formatting": {
        "reset": "\u001b[0m",
        "bold": "\u001b[1m",
        "italic": "\u001b[3m",
        "underline": "\u001b[4m",
        "blink": "\u001b[5m",
        "reversed": "\u001b[7m",
    },
}

COLORS = {
    "ERROR": colors["foreground"]["red"] + colors["formatting"]["bold"],
    "RESET": colors["formatting"]["reset"],
    "INFO": colors["foreground"]["cyan"] + colors["formatting"]["bold"],
    "WARNING": colors["foreground"]["yellow"] + colors["formatting"]["bold"],
    "SUCCESS": colors["foreground"]["green"] + colors["formatting"]["bold"],
    # Black background, yellow text, bold formatting
    "RAM_BYTE": colors["background"]["black"] + colors["foreground"]["yellow"] + colors["formatting"]["bold"],
    # Green background
    "RAMBACKGROUND": colors["background"]["green"],
}

"""
[ERROR]
Traced Line: 
     |- Unknown opcode 'WAN'
> 04 | WAN 0
       ^^^
"""


def error(message, lineNum, line):
    if "e" in verbose:
        print(
            f"""
{COLORS['ERROR']}[ERROR]{COLORS['RESET']}
Traced Line: 
     |- {message}
> {lineNum.zfill(2)} | {line}
       {colors['foreground']["red"]}^^^
{colors['formatting']["reset"]}"""
        )
    else:
        pass


"""
[INFO] Opcode # cyan
Opcode: SAV
"""


def info(name, message):
    if "i" in verbose:
        print(
            f"""
{COLORS['INFO']}[INFO]{colors['foreground']["cyan"]} {name}{COLORS['RESET']}
{message}
"""
        )
    else:
        pass


def clear():
    print("\033c", end="")  # Clear the console by printing the escape character


class Memory:
    def __init__(self, size):
        self.memory = [0x0] * size  # Create a list of 0s of the specified size

    def load_program(self, program, start_address):
        for i, instruction in enumerate(program):
            self.memory[start_address + i] = instruction

    def read(self, address):
        return self.memory[address]

    def write(self, address, value):
        self.memory[address] = value

    def print(self):
        # Print the memory in 0x20 byte rows with the address in hexadecimal (0x00 - 0xFF)
        for i in range(0, len(self.memory), 0x20):
            # COLORS["RAMBACKGROUND + " " + COLORS["RESET"] + COLORS["RAM_BYTE"] + ADDRESS + COLORS["RESET"]
            for j in range(0x20):
                print(
                    f"{COLORS['RAMBACKGROUND']} {COLORS['RAM_BYTE']}{self.memory[i+j]:02X}{COLORS['RESET']}",
                    end="",
                )
            print("")

class CPU:
    def __init__(self, memory):
        self.memory = memory  # Memory object (iniialised outside of the CPU class to allow for multiple CPUs to share the same memory object)
        self.pc = 0  # Program counter
        self.acc = 0  # Accumulator
        self.mar = (
            0  # Memory address register - holds the address of the current instruction
        )
        self.mdr = 0  # Memory data register - holds the data of the current instruction

    def fetch(self):
        # Fetch:
        # 1. Copy the address in the program counter to the memory address register
        # 2. Copy the data from the memory at the address in the memory address register to the memory data register
        # 3. Increment the program counter
        self.mar = self.pc
        self.mdr = self.memory.read(self.mar)
        self.pc += 1

    def decode(self):
        # Decode:
        # 1. Split the data in the memory data register into the opcode and operand
        # 2. Return the opcode and operand
        opcode = (
            self.mdr >> 4
        )  # Shift the data in the memory data register 4 bits to the right to get the opcode
        operand = self.mdr & 0xF
        return opcode, operand

    def execute(self, opcode, operand, instructionNum):
        if opcode == 0x0:
            # HLT - Halt the program
            print(f"{instructionNum} | HLT - Halt the program")
            return False
        elif opcode == 0x1:
            # SAV - Save the value in the accumulator to RAM[Address]
            address = operand[1]
            print(
                f"{instructionNum} | SAV - Save the value in the accumulator to RAM[{address}]"
            )
            self.memory.write(address, self.acc)
        elif opcode == 0x2:
            # LDA - Load the value from RAM[Address] into the accumulator
            address = operand
            print(
                f"{instructionNum} | LDA - Load the value from RAM[{address}] into the accumulator"
            )
            self.acc = self.memory.read(address)
        elif opcode == 0x3:
            # ADD - Add the value to the accumulator
            value = operand
            print(f"{instructionNum} | ADD - Add {value} to the accumulator")
            self.acc += self.memory.read(value)
        elif opcode == 0x4:
            # SUB - Subtract the value from the accumulator
            value = operand
            print(f"{instructionNum} | SUB - Subtract {value} from the accumulator")
            self.acc -= self.memory.read(value)
        elif opcode == 0x5:
            # OUT - Output the value in the accumulator to the console
            print(
                f"{instructionNum} | OUT - Output the value in the accumulator to the console"
            )
            print(f"Output: {self.acc}")
        elif opcode == 0x6:
            # INP - Input a value from the console
            print(f"{instructionNum} | INP - Input a value from the console")
            self.acc = int(input("Enter a value: "))
        elif opcode == 0x7:
            # BAD - Bitwise AND the value with the accumulator
            value = operand
            print(f"{instructionNum} | BAD - Bitwise AND {value} with the accumulator")
            self.acc &= self.memory.read(value)
        elif opcode == 0x8:
            # BOR - Bitwise OR the value with the accumulator
            value = operand
            print(f"{instructionNum} | BOR - Bitwise OR {value} with the accumulator")
            self.acc |= self.memory.read(value)
        elif opcode == 0x9:
            # BXR - Bitwise XOR the value with the accumulator
            value = operand
            print(f"{instructionNum} | BXR - Bitwise XOR {value} with the accumulator")
            self.acc ^= self.memory.read(value)
        elif opcode == 0xA:
            # BNT - Bitwise NOT the accumulator
            print(f"{instructionNum} | BNT - Bitwise NOT the accumulator")
            self.acc = ~self.acc
        elif opcode == 0xB:
            # JMP - Jump Always to the specified label
            print(f"{instructionNum} | JMP - Jump Always to label {operand}")
            self.pc = operand
        elif opcode == 0xC:
            # JEZ - Jump to the specified label if the accumulator is equal to zero
            print(
                f"{instructionNum} | JEZ - Jump to label {operand} if the accumulator is equal to zero"
            )
            if self.acc == 0:
                self.pc = operand
        elif opcode == 0xD:
            # JGZ - Jump to the specified label if the accumulator is greater than zero
            print(
                f"{instructionNum} | JGZ - Jump to label {operand} if the accumulator is greater than zero"
            )
            if self.acc > 0:
                self.pc = operand
        elif opcode == 0xE:
            # JLZ - Jump to the specified label if the accumulator is less than zero
            print(
                f"{instructionNum} | JLZ - Jump to label {operand} if the accumulator is less than zero"
            )
            if self.acc < 0:
                self.pc = operand
        elif opcode == 0xF:
            # SIG - Send a signal to the specified pin (ONLY FOR RASPBERRY PI/MICR0PYTHON)
            print(f"{instructionNum} | SIG - Send a signal to the specified pin")
            pass
        return True

    def run(self):
        try:
            count = 0
            while True:
                info("Program Counter", self.pc)
                info("Accumulator", self.acc)
                self.fetch()
                opcode, operand = self.decode()
                continue_execution = self.execute(opcode, operand, count)
                count += 1
                if not continue_execution:
                    break
        except KeyboardInterrupt:
            error("Keyboard Interrupt", count - 1, f"{opcode} {operand}")


opcodes = {
    "HLT": {
        "machine_num": 0,
        "decription": "Halt the program",
        "operands": 0,
        "usage": "HLT",
    },
    "SAV": {
        "machine_num": 1,
        "decription": "Save the value in the accumulator to RAM[Address]",
        "operands": 1,
        "usage": "SAV Address",
    },
    "LDA": {
        "machine_num": 2,
        "decription": "Load the value from RAM[Address] into the accumulator",
        "operands": 1,
        "usage": "LDA Address",
    },
    "ADD": {
        "machine_num": 3,
        "decription": "Add the value to the accumulator",
        "operands": 1,
        "usage": "ADD Value",
    },
    "SUB": {
        "machine_num": 4,
        "decription": "Subtract the value from the accumulator",
        "operands": 1,
        "usage": "SUB Value",
    },
    "OUT": {
        "machine_num": 5,
        "decription": "Output the value in the accumulator to the console",
        "operands": 0,
        "usage": "OUT",
    },
    "INP": {
        "machine_num": 6,
        "decription": "Input a value from the console",
        "operands": 0,
        "usage": "INP",
    },
    "BAD": {
        "machine_num": 7,
        "decription": "Bitwise AND the value with the accumulator",
        "operands": 1,
        "usage": "BAD Value",
    },
    "BOR": {
        "machine_num": 8,
        "decription": "Bitwise OR the value with the accumulator",
        "operands": 1,
        "usage": "BOR Value",
    },
    "BXR": {
        "machine_num": 9,
        "decription": "Bitwise XOR the value with the accumulator",
        "operands": 1,
        "usage": "BXR Value",
    },
    "BNT": {
        "machine_num": 10,
        "decription": "Bitwise NOT the accumulator",
        "operands": 0,
        "usage": "BNT",
    },
    "JMP": {
        "machine_num": 11,
        "decription": "Jump Always to the specified label",
        "operands": 1,
        "usage": "JMP Label",
    },
    "JEZ": {
        "machine_num": 12,
        "decription": "Jump to the specified label if the accumulator is equal to zero",
        "operands": 1,
        "usage": "JEZ Label",
    },
    "JGZ": {
        "machine_num": 13,
        "decription": "Jump to the specified label if the accumulator is greater than zero",
        "operands": 1,
        "usage": "JGZ Label",
    },
    "JLZ": {
        "machine_num": 14,
        "decription": "Jump to the specified label if the accumulator is less than zero",
        "operands": 1,
        "usage": "JLZ Label",
    },
    "SIG": {
        "machine_num": 15,
        "decription": "Send a signal to the specified pin (ONLY FOR RASPBERRY PI/MICR0PYTHON)",
        "operands": 1,
        "usage": "SIG Pin",
    },
}


def checkErrors(line, lineNum):
    opcode = line.split(" ")[0]
    operand = line.split(" ")[1] if len(line.split(" ")) > 1 else 0
    # Check for errors:
    if not opcode in opcodes:  # Invalid Opcode
        raise Exception(error(f"Unknown opcode '{opcode}'", lineNum, line))

    # Check if the operand is a number in range
    if int(operand) > 0:
        if not operand.isdigit():
            raise Exception(
                error(f"Operand '{operand}' is not a number", lineNum, line)
            )
        if int(operand) > 0xFFFF:
            raise Exception(
                error(f"Operand '{operand}' is out of range", lineNum, line)
            )

    if len(line.split(" ")) > 2:
        raise Exception(
            f"[Line {lineNum}]\n | Error: \n\t|- Too many operands in '{line}'"
        )

    if len(line.split(" ")) < 2 and line.split(" ")[0] not in [
        "HLT",
        "OUT",
        "INP",
        "BNT",
        "SIG",
    ]:  # If the operand is empty and the opcode is not HLT, OUT, INP, BNT or SIG
        raise Exception(
            f"[Line {lineNum}]\n | Error: \n\t|- Missing operand for opcode '{line.split(' ')[0]}'| Traced Line: {line}"
        )

    return opcode, operand

def decodeOperand(operand):
    # determine between immediate, direct, indirect
    if operand[0] == "@":
        return int(operand[1:]), "indirect"
    elif operand[0] == "#":
        return int(operand[1:]), "immediate"
    else:
        return int(operand), "direct" # default to direct


def getProgram():
    # open program file:
    program_path = os.path.join(os.path.dirname(__file__), "test2.asr")
    with open(program_path, "r") as file:
        program = file.read().split("\n")

    if verbose:
        info("Raw Program", program)

    # remove comments and empty lines:
    program = [line.split(";")[0] for line in program]
    clear()
    info("Comments Removed", program)

    program = [line for line in program if line]  # Remove empty lines
    clear()
    info("Empty Lines Removed", program)

    # remove whitespace at the start and end of each line:
    program = [line.strip() for line in program]
    clear()
    info("Whitespace Removed", program)

    # convert program to machine code:
    machine_code = []
    lineCount = 0
    for line in program:
        info(f"Line {lineCount}", line)
        # Check for syntax errors:
        opcode, operand = checkErrors(line, lineCount)
        info("Opcode + Operand", [opcode, operand])

        # Convert the opcode and operand to machine code:
        machine_opcode = opcodes[opcode]["machine_num"]
        machine_operand = (
            operand if operand == 0 else int(operand)
        )  # If the operand is empty, set it to 0, otherwise convert it to an integer

        info("Machine Opcode + Operand", [machine_opcode, machine_operand])

        # Combine the opcode and operand to create a single integer of bit length 8 (4 bits for the opcode and 4 bits for the operand)
        # bitshift the opcode 4 bits to the left and then bitwise OR it with the operand
        machine_instruction = int(machine_opcode) << 4 | int(machine_operand)

        info("Machine Instruction", machine_instruction)
        machine_instruction_hex = hex(machine_instruction)

        info("Hex Machine Instruction", machine_instruction_hex)
        machine_code.append(machine_instruction)

        clear()
        info("Machine Code", machine_code)

        lineCount += 1

    return machine_code  # Convert the list of machine code instructions to a single integer (hexadecimal)


def main():
    # Example program
    program = getProgram()
    print(program)
    memory = Memory(128)  # Example memory size of 128 bytes
    memory.load_program(
        program, 0
    )  # Load the program into memory starting at address 0
    memory.print()

    cpu = CPU(memory)
    cpu.run()


if __name__ == "__main__":
    main()
