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
            Program Counter
            Accumulator
            Instruction Register
            Address Register

            Stack
            Stack Pointer
        */
        this.registers = {
            program_counter: new Register(
                "program_counter",
                8,
                0,
                "$pc",
                [true, true, true, true],
                true,
                true
            ),
            accumulator: new Register(
                "accumulator",
                8,
                0,
                "$acc",
                [true, true, true, true],
                true,
                true
            ),
            instruction_register: new Register(
                "instruction_register",
                8,
                0,
                "$ir",
                [true, true, true, true],
                true,
                true
            ),
            address_register: new Register(
                "address_register",
                8,
                0,
                "$ar",
                [true, true, true, true],
                true,
                true
            ),
            stack: new Stack(1, 8),
        };
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
