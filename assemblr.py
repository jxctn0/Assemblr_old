# Very basic assembly code emulator

def execute(opcode):
    opcode
    # EXECUTE - execute instruction
    if opcode == "HLT":
        # Code to execute if the opcode is "HLT"
        print("Halt program")
        quit()
    elif opcode == "SAV":
        # Code to execute if the opcode is "SAV"
        print("Save value")
    elif opcode == "LDA":
        # Code to execute if the opcode is "LDA"
        print("Load value")
    elif opcode == "ADD":
        # Code to execute if the opcode is "ADD"
        ACCUMULATOR += int(params[0])
        print("Add values")
    elif opcode == "SUB":
        # Code to execute if the opcode is "SUB"
        ACCUMULATOR -= int(params[0])
        print("Subtract values")
    elif opcode == "JMP":
            # Code to execute if the opcode is "JMP"
        print("Jump to location")
    elif opcode == "JEZ":
        # Code to execute if the opcode is "JEZ"
        print("Jump if equal to zero")
    elif opcode == "JGZ":
        # Code to execute if the opcode is "JGZ"
        print("Jump if greater than zero")
    elif opcode == "JLZ":
        # Code to execute if the opcode is "JLZ"
        print("Jump if less than zero")
    elif opcode == "INP":
        # Code to execute if the opcode is "INP"
        print("Input value")
    elif opcode == "OUT":
        # Code to execute if the opcode is "OUT"
        print(ACCUMULATOR)
        print("Output value")
    elif opcode == "SIG":
        # Code to execute if the opcode is "SIG"
        print("Send signal")
    elif opcode == "BAD":
        # Code to execute if the opcode is "BAD"
        print("Bad opcode")
    elif opcode == "BOR":
        # Code to execute if the opcode is "BOR"
        print("Bitwise OR")
    elif opcode == "BXR":
        # Code to execute if the opcode is "BXR"
        print("Bitwise XOR")
    elif opcode == "DLY":
        # Code to execute if the opcode is "DLY"
        print("Delay")
    else:
        # Code to execute if the opcode doesn't match any of the given opcodes
        print("Unknown opcode " + opcode)
        quit()
    