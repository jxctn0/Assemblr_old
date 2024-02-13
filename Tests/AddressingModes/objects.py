import os
import time, math

verbose = "ic"
mode = "h"  # h for hex, d for decimal, b for binary

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
    "RAM_BYTE": colors["background"]["black"]
    + colors["foreground"]["yellow"]
    + colors["formatting"]["bold"],
    # Green background
    "RAMBACKGROUND": colors["background"]["green"],
}

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
    "DAT": {
        "machine_num": 16,
        "decription": "Create a named address",
        "operands": 1,
        "usage": "DAT Label",
    },
}


def continue_():
    if "c" in verbose:
        input("Press Enter to continue...")
    else:
        pass


def error(message, lineNum, line):
    return f"""
{COLORS['ERROR']}[ERROR]{COLORS['RESET']}
Traced Line: 
      |- {message}
{colors['foreground']["red"]}=>{colors['formatting']["reset"]} {str(lineNum).zfill(2)} | {line}
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


def print_instruction(count, instruction):  # ? Helper function to print the instruction
    print(f"{count} {instruction}")


def clear():
    print("\033c", end="")  # Clear the console by printing the escape character


class Memory:
    def __init__(self, size):
        self.memory = [0x0] * size  # Create a list of 0s of the specified size
        self.freeMem = 0x0  # The next free memory address
        self.namedAddresses = {}  # Named addresses (e.g. labels)
        """
? The namedAddresses dictionary is used to store the addresses of named labels in the program.
? For example, if the program contains the line "label: DAT", the namedAddresses dictionary will contain the key "label" with the value of the address of the DAT instruction.
? this functionality can also be used for jump instructions (e.g. JMP label) where the label is the key in the namedAddresses dictionary and the value is the address of the label.

{
    "num1": 0xf6,
}

= the value the user stored with the key "num1" is stored at the address 0xf6

LDA num1
= the value stored at the address 0xf6 is loaded into the accumulator


JMP num1
= the program counter is set to the address 0xf6
        """
        self.size = size  # The size of the memory

    def load_program(self, start_address=0x0):
        program = self.getProgram()
        info("Program created / got from disk")
        if verbose:
            print(program)
        info("Program syntax checked")
        self.namedAddresses = self.extract_named_addresses(program)
        program_range = range(start_address, start_address + len(program))
        self.memory_map = {"program": program_range, "named_addresses": self.namedAddresses}
        info(self.memory.memory_map)
        for i, instruction in enumerate(program):
            self.memory[start_address + i] = instruction
        info("Memory map created:")
        if verbose:
            print(self.memory_map)
        info("Program loaded into RAM:")
        self.freeMem = start_address + len(program)

    def extract_named_addresses(self, program):
        named_addresses = {}
        for i, line in enumerate(program):
            opcode, *operand = line.split(" ")
            if opcode == "DAT" and operand:
                if operand[0].startswith("$"):
                    named_addresses[operand[0][1:]] = i
        return named_addresses

    def validate_instruction(self, line, lineNum):
        opcode, *operand = line.split(" ")

        if opcode not in opcodes:
            raise ValueError(error("Unknown opcode", lineNum, line))

        if len(operand) != opcodes[opcode]["operands"]:
            raise ValueError(error("Invalid number of operands", lineNum, line))

        if operand:
            if operand[0][0] == "#":
                # Immediate addressing
                self.memory.write(int(operand[0][1:]), self.freeMem)
                operand = self.freeMem
                self.freeMem += 1
            elif operand[0].startswith("$"):
                #$ Named address
                operand = operand[0][1:]  # Remove the "$" prefix
                #? If the named address is not in the namedAddresses dictionary, create a new entry with the address of the next free memory location
                if operand not in self.namedAddresses and opcode == "DAT":
                    self.namedAddresses[operand.replace("$", "")] = self.freeMem #? the key is the name of the address and the value is the address
                    info("Named Address Created", operand)
                elif operand not in self.namedAddresses:
                    raise ValueError(error("Uninitialised named address", lineNum, line))
                else:
                    operand = self.namedAddresses[operand]
                    info("Named Address Loaded", operand)
            else:
                try:
                    operand = int(operand[0])
                except ValueError:
                    raise ValueError(error("Invalid operand", lineNum, line))
        else:
            operand = 0

        return opcode, operand

    def getProgram(self):
        # open program file:
        program_path = os.path.join(os.path.dirname(__file__), "test2.asr")
        with open(program_path, "r") as file:
            program = file.read().split("\n")

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
            opcode, operand = self.validate_instruction(line, lineCount)
            info("Opcode + Operand", [opcode, operand])

            # Convert the opcode and operand to machine code:
            machine_opcode = opcodes[opcode]["machine_num"]
            machine_operand = (
                operand if operand == 0 else int(operand)
            )  # If the operand is empty, set it to 0, otherwise convert it to an integer
            machine_addressing_mode = 0x0 # Set the addressing mode to 0 for now
            #TODO: Implement addressing modes
            #? The addressing mode will be stored in the last 4 bits of the machine code instruction
            #? INstruction stored as:
            #? f    f    f    f    f    3
            #? 0000 0000 0000 0000 0000 00
            #?  ^    ^                  ^
            #?  |    |                  |
            #?  |    |                  Addressing mode 0b00 -> Immediate, 0b01 -> Direct, 0b10 -> Indirect, 0b11 -> Relative 
            #?  |    Operand (16 bits)
            #?  Opcode (4 bits)
            #? 

            info("Machine Opcode + Operand + Addressing Mode", [machine_opcode, machine_operand, machine_addressing_mode])

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
            continue_()

        return machine_code  # Convert the list of machine code instructions to a single integer (hexadecimal)

    def read(self, address):
        return self.memory[address]

    def write(self, value, address=None):
        if address is None:
            self.memory[self.freeMem] = value
            self.freeMem += 1
        self.memory[address] = value

    def print(self):
        # ? Calculate the width of each row
        #! will be either 25% of the width of the console or sqrt of the size of the memory, whichever is the closest to the console width
        console_width = os.get_terminal_size().columns
        row_width = math.sqrt(self.size)

        row_width = int(row_width)
        if row_width < console_width:
            row_width = int(row_width)
        else:
            row_width = int(console_width / 4)

        # ? Print the memory
        for i, byte in enumerate(self.memory):

            # ^ stop the program from printing the entire memory
            if i == self.size:
                break

            mode = "b"
            # ? convert the byte to the respective base
            if mode == "h":
                fillLength = 3
                byte = hex(byte)[2:].zfill(fillLength)
            elif mode == "d":
                fillLength = 3
                byte = int(byte)[2:].zfill(fillLength)
            elif mode == "b":
                fillLength = 8
                byte = bin(byte)[2:].zfill(fillLength)

            # ? Print the memory address
            if i % row_width == 0:
                if "h" in mode:
                    addrRow = hex(i)

                elif "d" in mode:
                    addrRow = int(i)

                elif "b" in mode:
                    addrRow = bin(i)

                print(
                    f"\n{COLORS['RESET']}0{mode}{str(addrRow)[2:].zfill(fillLength)}{COLORS['RESET']}",
                    end=" ",
                )
            print(
                f"{COLORS['RAMBACKGROUND']} {COLORS['RAM_BYTE']}{str(byte).zfill(fillLength)}{COLORS['RAMBACKGROUND']}",
                end=" ",
            )

        print()


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
        # Convert named address to actual memory address
        if isinstance(operand, str):
            operand = self.memory.namedAddresses[operand]

        if opcode == 0x0:
            # HLT - Halt the program
            print_instruction(instructionNum, "HLT - Halt the program")
            return False

        elif opcode == 0x1:
            # SAV - Save the value in the accumulator to RAM[Address]
            address = operand[1]
            print_instruction(
                instructionNum,
                f"SAV - Save the value in the accumulator to RAM[{address}]",
            )
            self.memory.write(address, self.acc)
            info("Accumulator", self.acc)

        elif opcode == 0x2:
            # LDA - Load the value from RAM[Address] into the accumulator
            address = operand
            print_instruction(
                instructionNum,
                f"LDA - Load the value from RAM[{address}] into the accumulator",
            )
            self.acc = self.memory.read(address)

        elif opcode == 0x3:
            # ADD - Add the value to the accumulator
            value = operand
            print_instruction(instructionNum, f"Add {value} to the accumulator")
            self.acc += self.memory.read(value)

        elif opcode == 0x4:
            # SUB - Subtract the value from the accumulator
            value = operand
            print_instruction(
                instructionNum,
                f"SUB - Subtract {value} from the accumulator",
            )
            self.acc -= self.memory.read(value)

        elif opcode == 0x5:
            # OUT - Output the value in the accumulator to the console
            print_instruction(
                instructionNum,
                "OUT - Output the value in the accumulator to the console",
            )
            print(f"Output: {self.acc}")

        elif opcode == 0x6:
            # INP - Input a value from the console
            print_instruction(instructionNum, "INP - Input a value from the console")
            while True:
                try:
                    self.acc = int(input("Enter a value: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    continue

        elif opcode == 0x7:
            # BAD - Bitwise AND the value with the accumulator
            value = operand
            print_instruction(
                instructionNum, f"BAD - Bitwise AND {value} with the accumulator"
            )
            self.acc &= self.memory.read(value)

        elif opcode == 0x8:
            # BOR - Bitwise OR the value with the accumulator
            value = operand
            print_instruction(
                instructionNum, f"BOR - Bitwise OR {value} with the accumulator"
            )
            self.acc |= self.memory.read(value)

        elif opcode == 0x9:
            # BXR - Bitwise XOR the value with the accumulator
            value = operand
            print_instruction(
                instructionNum, f"BXR - Bitwise XOR {value} with the accumulator"
            )
            self.acc ^= self.memory.read(value)

        elif opcode == 0xA:
            # BNT - Bitwise NOT the accumulator
            print_instruction(instructionNum, "BNT - Bitwise NOT the accumulator")
            self.acc = ~self.acc

        elif opcode == 0xB:
            # JMP - Jump Always to the specified label
            print_instruction(instructionNum, f"JMP - Jump Always to label {operand}")
            self.pc = operand

        elif opcode == 0xC:
            # JEZ - Jump to the specified label if the accumulator is equal to zero
            print_instruction(
                instructionNum,
                f"JEZ - Jump to label {operand} if the accumulator is equal to zero",
            )
            # convert the operand to an integer if it is a named address

            if self.acc == 0:
                self.pc = operand

        elif opcode == 0xD:
            # JGZ - Jump to the specified label if the accumulator is greater than zero
            print_instruction(
                instructionNum,
                f"JGZ - Jump to label {operand} if the accumulator is greater than zero",
            )
            if self.acc > 0:
                self.pc = operand

        elif opcode == 0xE:
            # JLZ - Jump to the specified label if the accumulator is less than zero
            print_instruction(
                instructionNum,
                f"JLZ - Jump to label {operand} if the accumulator is less than zero",
            )
            if self.acc < 0:
                self.pc = operand
        elif opcode == 0xF:
            # SIG - Send a signal to the specified pin (ONLY FOR RASPBERRY PI/MICR0PYTHON)
            print(f"{instructionNum} | SIG - Send a signal to the specified pin")
            pass
        elif opcode == 0x10:
            # DAT - Create a named address
            print(f"{instructionNum} | DAT - Create a named address")
            # Get the name of the address
            name = operand
            # Get the address
            address = self.freeMem
            # Save the address in the named addresses dictionary
            self.memory.namedAddresses[name] = address
            # Increment the free memory address
            self.freeMem += 1
        else:
            raise ValueError(
                error("Unknown opcode", instructionNum, f"{opcode} {operand}")
            )

        return True

    def run(self):
        try:
            while True:
                if self.pc >= len(self.memory.memory):
                    raise ValueError("Program Counter exceeded memory size")
                self.fetch()
                opcode, operand = self.decode()
                if not self.execute(opcode, operand):
                    break  # HLT encountered, terminate program
        except Exception as e:
            error("Error handling execution", self.pc - 1, f"{opcode} {operand}")
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("Program terminated by user.")
        finally:
            print("Program terminated.")

    def print_(self):
        overscore = "\u203E"
        underscore = "_"
        if mode == "h":
            pc = str(hex(self.pc)).zfill(2)
            acc = str(hex(self.acc)).zfill(2)
            mar = str(hex(self.mar)).zfill(2)
            mdr = str(hex(self.mdr)).zfill(2)
        elif mode == "d":
            pc = str(self.pc).zfill(3)
            acc = str(self.acc).zfill(3)
            mar = str(self.mar).zfill(3)
            mdr = str(self.mdr).zfill(3)
        elif mode == "b":
            pc = bin(self.pc)[2:].zfill(8)
            acc = bin(self.acc)[2:].zfill(8)
            mar = bin(self.mar)[2:].zfill(8)
            mdr = bin(self.mdr)[2:].zfill(8)

        print(
            f"""
    _{underscore * int(len(pc))}_        _{underscore * len(acc)}_        _{underscore * len(mar)}_        _{underscore * len(mdr)}_
PC | {pc} |  ACC | {acc} |  MAR | {mar} |  MDR | {mdr} |
    ‾{overscore * len(pc)}‾        ‾{overscore * len(acc)}‾        ‾{overscore * len(mar)}‾        ‾{overscore * len(mdr)}‾
            """
        )

        self.memory.print()


def main():
    memory = Memory((2**7))  # Example memory size of 2**7 (128 bytes)
    memory.load_program(0)  # Load the program into memory starting at address 0

    cpu = CPU(memory) # Create a CPU object with the memory object
    cpu.run() # Run the program

if __name__ == "__main__":
    main()
