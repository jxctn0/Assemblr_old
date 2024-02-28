import os
import time, math

verbose = "ic"
mode = "h"  # h for hex, d for decimal, b for binary

program_path = os.path.join(os.getcwd(), "test.asr")

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

opcode_ls = [
    "HLT", "SAV", "LDA", "ADD", "SUB", "OUT", "INP", "BAD", "BOR", "BXR", "BNT", "JMP", "JEZ", "JGZ", "JLZ", "SIG", "DAT"
]

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
There was an error when handling the exception:
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
        #! continue_()
    else:
        pass


def print_instruction(count, instruction):  # ? Helper function to print the instruction
    print(f"{count} {instruction}")


def clear():
    print("\033c", end="")  # Clear the console by printing the escape character


def bin_str(num):
    return str(f"0b{bin(num)[2:].zfill(8)}")


class Memory:
    def __init__(self, size):
        self.memory = [0x0] * size  # Create a list of 0s of the specified size
        self.freeMem = 0x0  # The next free memory address
        self.size = size  # The size of the memory
        self.progSize = 0x0  # The size of the program
        self.namedAddresses = {}  # A dictionary to store named addresses

    def generate_instruction(self, opcode, operand, addr_mode=0x0):
        # ? Generate the instruction by combining the opcode and operand
        # ^ Convert the opcode to its machine code equivalent
        opcode = opcodes[opcode]["machine_num"]
        info("Opcode", opcode)
        info("Operand", operand)

        # ^ Combine the opcode and address mode to form the first 6 bits of the instruction
        instruction = (opcode << 0x2) | addr_mode
        info("Instruction", instruction)

        # ^ Combine the instruction and operand to form the full 8 bit instruction
        instruction = (instruction << 0x4) | operand
        info("Instruction", bin(instruction))

        return instruction

    def load_program(self, start_address=0x0):
        # ? Load the program into memory starting at the specified address
        # ? The program is loaded from a file called "test.asr" in the same directory as the script
        # ? The program is loaded line by line and each line is split into the opcode and operand
        # ? The opcode is then converted to its machine code equivalent and the operand is converted to a hexadecimal number
        # ? If the operand is a named address, the address is looked up in the namedAddresses dictionary and used as the operand
        # ? The machine code and operand are then combined to form the instruction and written to memory at the specified address

        program = open(program_path, "r").readlines()
        info("Program", program)

        for i, line in enumerate(program):
            # ^ Remove Comments and whitespace
            # ? Remove Comment strings
            line = line.split(";")[0]
            info(f"Line {i}", line)
            # ? Remove leading and trailing whitespace
            line = line.strip()

            # ? Skip empty lines
            if line == "":
                continue

            # ^ Get the opcode and operand
            # ? Split the line into the opcode and operand
            opcode, *operand = line.split(" ")

            info("Opcode", opcode)
            info("Operand", operand)

            if opcode not in opcodes:
                raise SyntaxError(error("Unknown opcode", i, line))

            # ^ Check if the number of operands is correct
            if len(operand) != opcodes[opcode]["operands"]:
                raise SyntaxError(error("Incorrect number of operands", i, line))

            # ^ Check if the opcode needs an operand
            if opcodes[opcode]["operands"] == 0:
                operand = 0x0

            # ^ Check if the opcode is DAT - create a named address
            if opcode == "DAT":
                # ? Get the name of the address
                name = operand[0]
                # ? Get the address - will be length of the memory + 1 OR the next free memory address, whichever is lesser
                address = min(len(self.memory) + 1, self.freeMem)
                # ? Create an indirect reference for the named address
                opcode = address
                # ? Save the address in the named addresses dictionary
                self.namedAddresses[name] = address

            # ^ Check the address mode
            if opcodes[opcode]["operands"] == "@":  # = Mode is indirect
                addr_mode = 0x2
            elif opcodes[opcode]["operands"] == "#":  # = Mode is immediate
                addr_mode = 0x1
            else:  # = Mode is direct
                addr_mode = 0x0

            # ^ Check if the operand is a named address
            if (
                operand
            ):  #! if the operand is not empty (so this doesn't apply to instructions like HLT)
                try:
                    operand = int(operand[0], 16)
                    # = Operand is a hexadecimal number, continue
                except ValueError:
                    # = Operand is a named address
                    if operand[0] in self.namedAddresses:
                        operand = self.namedAddresses[
                            operand[0]
                        ]  # = Will return the address associated with the named address
                        addr_mode = 0x2  # ? Set the address mode to indirect because the operand is a named address (pointing at a pointer)
                    else:
                        raise ValueError(
                            error("Uninitialised Address address", i, line)
                        )

            instruction = self.generate_instruction(opcode, operand, addr_mode)

            # ^ Write the instruction to memory
            self.write(bin(instruction), (start_address - 1) + i)

            # = The final instruction will be a 16 bit number:
            # = 0000 0000 0000 0000
            # = |__/ |/|__________/
            # = |    | |
            # = |    | Operand
            # = |    |
            # = |    Address Mode
            # = Opcode

        # ? Save the size of the program
        self.progSize = len(program)

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
        # 1. Extract the instriction from the memory data register - 10bits
        # 2. Extract the opcode from the instruction (first 4 bits)
        # 3. Extract the address mode from the instruction (next 2 bits)
        # 4. Extract the operand from the instruction (last 2 bits)
        # 5. Return the opcode, operand and address mode

        instruction = self.mdr
        info("Instruction", instruction)

        # remove the 0b prefix
        instruction = instruction[2:].zfill(10)

        opcode = instruction[0:4]
        addrMode = instruction[4:6]
        operand = instruction[6:]

        return opcode, operand, addrMode

    def get_operand(self, address_mode, operand):
        if address_mode == 0x0:  # ? Direct
            return self.memory.read(operand)
        elif address_mode == 0x1:
            return self.memory.read(self.memory.read(operand))
        elif address_mode == 0x2:
            return operand
        

    def execute(self, opcode, operand, instructionNum, address_mode=0x0):

        info("Opcode", opcode)
        operand = self.get_operand(address_mode, operand)
        info("Operand", operand)
        # Execute:
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
                opcode, operand, addrMode = self.decode()
                if not self.execute(
                    opcode, operand, address_mode=addrMode, instructionNum=self.pc - 1
                ):
                    break  # HLT encountered, terminate program
        # except Exception as e:
        #     error("Error handling execution", self.pc - 1, f"{opcode} {operand}")
        #     print(f"Error: {e}")
        except KeyboardInterrupt:
            print("Program terminated by user.")
        finally:
            print("Program terminated.")

    def print_(self):
        overscore = "\u203E"  # ‾
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
    info("Program Loaded", memory.memory)

    #continue_()

    cpu = CPU(memory)  # Create a CPU object with the memory object
    cpu.run()  # Run the program


if __name__ == "__main__":
    main()
