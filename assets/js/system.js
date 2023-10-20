// this script holds alll the system variables

globalThis.registers = {};

class Register {
    constructor(
        name, // name of the register
        size, // size in bits
        start_value = 0, // value at machine start
        address_name, // name of the address (i.e. $acc)
        addressmodes = [true, true, true, true], // address modes (immediate, direct, indirect, indexed)
        read = true, // is register readable
        write = true // is register writable
    ) {
        this.name = name;
        this.size = size;
        this.value = start_value;
        this.address_name = address_name;
        this.addressmodes = addressmodes;
        this.read = read;
        this.write = write;
    }
    // change value
    setValue(value) {
        this.value = value;
    }

    // increment and decrement
    increment() {
        this.value++;
    }
    decrement() {
        this.value--;
    }

    // get value
    getValue() {
        return this.value;
    }
}

class Port {
    constructor(name, size, read = true, write = true) {
        this.name = name;
        this.size = size;
        this.value = 0;
        this.read = read;
        this.write = write;
    }
    write(value) {
        this.value = value;
    }
    read() {
        return this.value;
    }
}

class Stack {
    constructor(addressNum, size) {
        this.stack = [];
        this.addressNum = addressNum;
        this.stackPointer = new Register(
            "stack_pointer_" + addressNum,
            8,
            0,
            "$sp" + addressNum,
            [true, true, true, true],
            true,
            true
        );
        this.size = size;
    }
    push(value) {
        // Check if stack is full
        if (this.stack.length >= this.size) {
            // StackOverflow Error
            // return -1
            error("StackOverflow", "The stack has overflowed.");
            return -1; // StackOverflow Error
        }

        // push value to stack
        this.stack.push(value);

        // increment stack pointer
        this.stackPointer.increment();
    }
    pop() {
        // Check if stack is empty
        if (this.stack.length == 0) {
            // StackUnderflow Error
            // return -1
            error("StackUnderflow", "The stack has underflowed.");
            return -1; // StackUnderflow Error
        }

        // pop value from stack
        this.stack.pop();

        // decrement stack pointer
        this.stackPointer.decrement();
    }

    // get top value
    getValue() {
        return this.stack[this.stack.length - 1];
    }
}

class System {
    constructor() {
        /*  Registers:
          - PC - Program Counter
          - MAR - Memory Address Register
          - MDR - Memory Data Register
          - CIR - Current Instruction Register
          - ACC - Accumulator

          - STK - Stack
          - STP - Stack Pointer
        */
        this.registers = {
            // PC - Program Counter
            PC: new Register(
                "program_counter",
                8,
                0,
                "$PC",
                [true, true, true, true],
                true,
                true
            ),
            // MAR - Memory Address Register
            MAR: new Register(
                "memory_address_register",
                8,
                0,
                "$MAR",
                [true, true, true, true],
                true,
                true
            ),
            // MDR - Memory Data Register
            MDR: new Register(
                "memory_data_register",
                8,
                0,
                "$MDR",
                [true, true, true, true],
                true,
                true
            ),
            // CIR - Current Instruction Register
            CIR: new Register(
                "current_instruction_register",
                8,
                0,
                "$CIR",
                [true, true, true, true],
                true,
                true
            ),
            // ACC - Accumulator
            ACC: new Register(
                "accumulator",
                8,
                0,
                "$ACC",
                [true, true, true, true],
                true,
                true
            ),

            // STK - Stack
            STK: new Stack(1, 8),
        };

        // Initialise ports

        // Number of ports
        port_num = getConfig("port_num");

        // Initialise ports
        for (i = 0; i < port_num; i++) {
            // Add a port to this.ports
            this.ports["port" + i] = new Port("port" + i, 8, true, true);
        }
    }

    // create memory
    CreateMemory(size = 256) {
        // create memory
        var memory = new Array(size);

        // return memory
        return memory;
    }

    printSystem() {
        console.log(this.registers); // CLI Only
    }

    displaySystem() {
        // Shows the system in the GUI
        // TODO!!
    }
}
