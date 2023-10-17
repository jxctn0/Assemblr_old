// import scripts
import { System } from './system.js';

// Create a new system
var BaseSystem = new System();

// initialise Aliases for the registers
var PC = BaseSystem.registers.program_counter;
var ACC = BaseSystem.registers.accumulator;
var IR = BaseSystem.registers.instruction_register;
var AR = BaseSystem.registers.address_register;
var STACK = BaseSystem.registers.stack;
var SP = STACK.stackPointer;

// initialise the memory alias with a size from the config
var memory = BaseSystemSystem.CreateMemory();

// Function to read through the code and execute it
//* Fetch, Decode, Execute Cycle:
//? https://upload.wikimedia.org/wikipedia/commons/d/de/Fetch-Decode-Execute_Cycle.png
// Fetch the instruction:
//    Address of the instruction is in the program counter
//    Copy the instruction into the instruction register
//    Increment the program counter
//    Instruction in instruction register is now the current instruction



function executeProgram() {
    //! FETCH
    // Fetch the instruction
    IR.value = memory[PC.value];
    // Increment the program counter
    PC.value++;
    // Fetch the address
    AR.value = memory[PC.value];
    // Increment the program counter
    PC.value++;

}