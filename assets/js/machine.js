// import scripts
import { System } from "./system.js";

// Create a new system
var BaseSystem = new System();

// Initialise aliases for the system registers
/*  Registers:
- PC - Program Counter
- MAR - Memory Address Register
- MDR - Memory Data Register
- CIR - Current Instruction Register
- ACC - Accumulator

- STK - Stack
- STP - Stack Pointer
*/
var PC = BaseSystem.registers.PC;
var MAR = BaseSystem.registers.MAR;
var MDR = BaseSystem.registers.MDR;
var CIR = BaseSystem.registers.CIR;
var ACC = BaseSystem.registers.ACC;
var STK = BaseSystem.registers.STK;

// initialise the memory alias with a size from the config
var memory = BaseSystemSystem.CreateMemory();

// Instruction set
INSTRUCTION_SET = {
    "0000": {
        opcode: "HLT",
        description: "Halt operation",
        execute: function () {
            // Stop the program
            console.log("Program halted");
            quit(1); // Code 1 for successful exit
        },
    },
    "0001": {
        opcode: "ADD",
        description: "Add",
        execute: function () {
            // Add the value in the accumulator to the value in the memory address
            ACC.setValue(ACC.getValue() + MDR.getValue());
        }
    },
    "0010": {
        opcode: "SUB",
        description: "Subtract",
        execute: function () {
            // Subtract the value in the accumulator to the value in the memory address
            ACC.setValue(ACC.getValue() - MDR.getValue());
        }
    },
    "0011": {
        opcode: "STA",
        description: "Store",
        execute: function () {
            // Store the value in the accumulator to the memory address
            memory[MAR.getValue()] = ACC.getValue();
        }
    },
    "0100": {
        opcode: "LDA",
        description: "Load",
        execute: function () {
            // Load the value in the memory address to the accumulator
            ACC.setValue(memory[MAR.getValue()]);
        }
    },
    "0101": {
        opcode: "JMP",
        description: "Jump to address",
        execute: function () {
            // Jump to the memory address
            PC.setValue(MAR.getValue());
        }
    },
    "0110": {
        opcode: "JGZ",
        description: "Jump if ACC greater than zero",
        execute: function () {
            // Jump to the memory address if the accumulator is greater than zero
            if (ACC.getValue() > 0) {
                PC.setValue(MAR.getValue());
            }
        }
    },
    "0111": {
        opcode: "JLZ",
        description: "Jump if ACC less than zero",
        execute: function () {
            // Jump to the memory address if the accumulator is less than zero
            if (ACC.getValue() < 0) {
                PC.setValue(MAR.getValue());
            }
        }
    },
    "1000": {
        opcode: "JEZ",
        description: "Jump if ACC equal to zero",
        execute: function () {
            // Jump to the memory address if the accumulator is equal to zero
            if (ACC.getValue() == 0) {
                PC.setValue(MAR.getValue());
            }
        }
    },
    "1001": {
        opcode: "JMR",
        description: "Jump relative to address",
        execute: function () {
            // Jump to the memory address relative to the current address
            PC.setValue(PC.getValue() + MAR.getValue());
        }
    },
    "1010": {
        opcode: "INP",
        description: "Input",
        execute: function () {
            // Input a value into the accumulator
            ACC.setValue(getInput());
        }
    },
    "1011": {
        opcode: "PWR",
        description: "Write to port",
        execute: function () {
            // Write to a port
            port = MAR.getValue();
            value = ACC.getValue();
            // Check if the port exists
            if (PORTS[port] != undefined) {
                // Write to the port
                PORTS[port].write(value);
            } else {
                // Port does not exist
                console.error("Port " + port + " does not exist");
                error(11) // Code 11 for invalid port
                quit();
            }
        }
    },
    "1100": {
        opcode: "PRD",
        description: "Read from port",
        execute: function () {
            // Read from a port
            port = MAR.getValue();
            // Check if the port exists
            if (PORTS[port] != undefined) {
                // Read from the port
                ACC.setValue(PORTS[port].read());
            } else {
                // Port does not exist
                console.error("Port " + port + " does not exist");
                error(11) // Code 11 for invalid port
                quit();
            }
        }
    },
    "1101": {
        opcode: "PSH",
        description: "Push to stack",
        execute: function () {
            // Push a value to the stack
            STK.push(ACC.getValue());
        }
    },
    "1110": {
        opcode: "POP",
        description: "Pop from stack",
        execute: function () {
            // Pop a value from the stack
            ACC.setValue(STK.pop());
        }
    },
    "1111": {
        opcode: "NOP",
        description: "No operation",
        execute: function () {
            // Do nothing for one cycle
            PC.increment();
        }
    }
};
// Function to read through the code and execute it
//* Fetch, Decode, Execute Cycle:
//? https://upload.wikimedia.org/wikipedia/commons/d/de/Fetch-Decode-Execute_Cycle.png
// Fetch the instruction:
//    Address of the instruction is in the program counter
//    Copy the instruction into the instruction register
//    Increment the program counter
//    Instruction in instruction register is now the current instruction
// Decode the instruction:
//    Instruction in the instruction register is decoded into an opcode
// Execute the instruction:
//    Instruction in the instruction register is executed
// Restart the cycle

function executeInstruction() {
    //! FETCH
    // Address of the instruction is in the program counter
    instruction_address = PC.getValue();
    // Copy the instruction into the instruction register
    CIR.setValue(memory[instruction_address]);
    // Increment the program counter
    PC.increment();
    // Instruction in instruction register is now the current instruction
    if (VERBOSE) {
        console.log("FETCH: " + CIR.getValue());
    }
    //! DECODE
    // Instruction in the instruction register is decoded into an opcode
    opcode = IR.getValue().substring(0, 4);
    // Decode the opcode into an instruction
    instruction = INSTRUCTION_SET[opcode].execute
    if (VERBOSE) {
        console.log("DECODE: " + opcode);
    }
    //! EXECUTE
    // Instruction in the instruction register is executed
    instruction();
}
