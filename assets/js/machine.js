class machine {
    opcodes = {
        hlt: {
            operands: 0,
            opcode: 0,
            description: "Halts the program",
            function: function () {
                // halt the program
                hlt();
            },
        },
        sav: {
            opcode: 1,
            operands: {
                count: 2,
                op_1: {
                    type: "register" | "port",
                    description: "The register/port to read from",
                },
                op_2: {
                    type: "address",
                    description: "The memory address to save to",
                },
            },
            description:
                "Saves the value in the given register the given location in memory",
            function: function (operands) {
                // save the value in the given register to the given location in memory
                sav(operands[0], operands[1]);
            }
        },
        lda: {
            opcode: 2,
            operands: {
                count: 2,
                op_1: {
                    type: "address",
                    description: "The memory address to load from",
                },
                op_2: {
                    type: "register",
                    description: "The register to load to",
                },
            },
            description:
                "Loads the value in the given memory address to the given register",
            function: function (operands) {
                // load the value in the given memory address to the given register
                lda(operands[0], operands[1]);
            }
        },
        add: {
            opcode: 3,
            operands: {
                count: 2,
                op_1: {
                    type: "register",
                    description: "The register to add to",
                },
                op_2: {
                    type: "address",
                    description: "The memory address to add to the register",
                },
            },
            description:
                "Adds the value in the second register to the value in the first register",
            function: function (operands) {
                // add the value in the second register to the value in the first register
                add(operands[0], operands[1]);
            }
        },
        sub: {
            opcode: 4,
            operands: {
                count: 2,
                op_1: {
                    type: "register",
                    description: "The register to subtract from",
                },
                op_2: {
                    type: "address",
                    description: "The memory address to subtract from the register",
                },
            },
            description:
                "Subtracts the value in the second register from the value in the first register",
            function: function (operands) {
                // subtract the value in the second register from the value in the first register
                sub(operands[0], operands[1]);
            }
        },

        }
    };
    registers = {
        ACC: {
            address: 0,
            value: 0,
            description:
                "The Accumulator is used to store data temporarily while it is being processed.",
            reference_code: "$ACC",
        },
        NUL: {
            address: 1,
            value: 0,
            description:
                "The Null Register is used to store the value 0. If read or written to, it will always return 0.",
            reference_code: "$NUL",
        },
        SKP: {
            address: 2,
            value: 0,
            description:
                "The Stack Pointer is used to store the address of the top of the stack. It cannot be written to, but can be read. If an attemt to write is made, execution will terminate, and return an io error.",
            reference_code: "$STP",
        },
        STK: {
            address: 2,
            value: 0,
            description:
                "The Stack Pointer is used to store the address of the top of the stack. It can only hold 0b1111 (16) values. If the stack is empty, it will return 0b0000 (0). If the stack is written to while full, it will return a stack_overflow error. If the stack is read from while empty, it will return a stack_underflow error. when reading from the stack, it will return the top value and then remove it from the stack. When writing to the stack, it will add the value to the top of the stack and then increment the stack pointer.",
            reference_code: "$STK",
        }
    };
}

// get Config
function getConfig() {
    // open config.json
    var config = fs.readFileSync(config_file_location);
    // parse config.json
    config = JSON.parse(config);
    // return config
    return config;
}

var config = getConfig();

// set comment character
var comment_char = config.comment_char; // defualts to ';'

function runCode() {
    // get the code from the editor
    var code = editor.getValue();
    // split code into lines
    var lines = code.split("\n");

    // loop through lines
    for (line in lines) {
        // get line
        var current_line = lines[line];
        console.log(current_line);
        // remove comments
        current_line = current_line.split(comment_char)[0];
        // remove whitespace
        current_line = current_line.trim();
        // split line into opcode and operands
        var opcode = current_line.split(" ")[0];
        var operands = current_line.split(" ").slice(1);

        // check if opcode is valid
        if (opcodes[opcode] == undefined) {
            // show error
            error("Invalid Opcode", "The opcode " + opcode + " is not valid.");
            // return -1
            return -1;
        }
    }
}
