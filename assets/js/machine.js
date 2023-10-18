registers = {
    program_counter: {
        value: 0,
        bit_length: 16,
        reference: {
            name:"$PRC",
            read: true,
            write: false
        },
    },
    instruction_register: {
        value: 0,
        bit_length: 16,
        reference: {
            name:"$INS",
            read: true,
            write: false
        },
    },
    accumulator: {
        value: 0,
        bit_length: 16,
        reference: {
            name:"$ACC",
            read: true,
            write: true
        },
    },
    
    
}

function get_address(address_mode, operand) {
    
    /*
    *  Addressing Modes
     ? For more information see ../README.md#addressing-modes
     - imm: immediate - operand is the value
     - dir: direct - operand is the address
     - ind: indirect - operand is the address of the address
     - ixd: indexed - operand is the address of the address + the value of the index register
    */
   
}




Instructions = { 
    "ASSEMBLER":{ //? Default instructions
        "HLT":{
            "opcode": "0000",
            "addressing_modes": [],
            "description": "Halt the machine",
            "function": function() {
                //? Halt the machine
                quit()
            }
        },

    },
    "BITWISE":{ //? Bitwise instructions (Addon)
        "AND":{
            "opcode": "0000",
            "addressing_modes": ["imm","dir", "ind", "ixd"],
            "description": "Bitwise AND",
            "function": function(operand_address_mode) {
                //? perform bitwise AND on the accumulator and the operand
                operand = get_address(operand_address_mode)
                registers.accumulator.value = registers.accumulator.value & operand // AND already exists in JS
            
            }
        },
        "NOT":{
            "opcode": "0001",
            "addressing_modes": ["imm","dir", "ind", "ixd"],
            "description": "Bitwise NOT",
            "function": function(operand_address_mode) {
                //? perform bitwise NOT on the accumulator
                registers.accumulator.value = ~registers.accumulator.value
            
            }
        },
        "OR":{
            "opcode": "0010",
            "addressing_modes": ["imm","dir", "ind", "ixd"],
            "description": "Bitwise OR",
            "function": function(operand_address_mode) {
                //? perform bitwise OR on the accumulator and the operand
                operand = get_address(operand_address_mode)
                registers.accumulator.value = registers.accumulator.value | operand // OR already exists in JS
            
            }
        },
        "XOR":{
            "opcode": "0011",
            "addressing_modes": ["imm","dir", "ind", "ixd"],
            "description": "Bitwise XOR",
            "function": function(operand_address_mode) {
                //? perform bitwise XOR on the accumulator and the operand
                operand = get_address(operand_address_mode)
                registers.accumulator.value = registers.accumulator.value ^ operand // XOR already exists in JS
            
            }
        },
        "SHL":{
            "opcode": "0100",
            "addressing_modes": ["imm","dir", "ind", "ixd"],
            "description": "Bitwise shift left",
            "function": function(operand_address_mode) {
                //? perform bitwise shift left on the accumulator
                operand = get_address(operand_address_mode)
                registers.accumulator.value = registers.accumulator.value << operand // Shift left already exists in JS
            
            }
        },
        "SHR":{
            "opcode": "0101",
            "addressing_modes": ["imm","dir", "ind", "ixd"],
            "description": "Bitwise shift right",
            "function": function(operand_address_mode) {
                //? perform bitwise shift right on the accumulator
                operand = get_address(operand_address_mode)
                registers.accumulator.value = registers.accumulator.value >> operand // Shift right already exists in JS
            
            }
        },
        "NAD":{
            "opcode": "0110",
            "addressing_modes": ["imm","dir", "ind", "ixd"],
            "description": "Bitwise NAND",
            "function": function(operand_address_mode) {
                //? perform bitwise NAND on the accumulator and the operand
                operand = get_address(operand_address_mode)
                registers.accumulator.value = ~(registers.accumulator.value & operand)             
            }
        },
        "NOR":{
            "opcode": "0111",
            "addressing_modes": ["imm","dir", "ind", "ixd"],
            "description": "Bitwise NOR",
            "function": function(operand_address_mode) {
                //? perform bitwise NOR on the accumulator and the operand
                operand = get_address(operand_address_mode)
                registers.accumulator.value = ~(registers.accumulator.value | operand)             
            }
        },
        "XNR":{
            "opcode": "1000",
            "addressing_modes": ["imm","dir", "ind", "ixd"],
            "description": "Bitwise XNOR",
            "function": function(operand_address_mode) {
                //? perform bitwise XNOR on the accumulator and the operand
                operand = get_address(operand_address_mode)
                registers.accumulator.value = ~(registers.accumulator.value ^ operand)             
            }
        },
    }
}