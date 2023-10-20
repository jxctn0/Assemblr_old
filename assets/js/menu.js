// Import config file
const config = require("../config.json");
// Import fs module
const fs = require("fs");
// Import path module
const path = require("path");
// Import electron module
const electron = require("electron");
// Import process module
const process = require("process");
const { inherits } = require("util");
const { create } = require("domain");

// Set Globals
global.save_file_location = null;
global.platform = process.platform;
global.directories = {
    program_root: {
        win32: path.join(process.env.APPDATA, "Assemblr"),
        linux: path.join(process.env.HOME, ".config", "Assemblr"),
        darwin: path.join(
            process.env.HOME,
            "Library",
            "Application Support",
            "Assemblr"
        ),
    },
    data: {
        win32: path.join(process.env.APPDATA, "Assemblr", "data", "saves"),
        linux: path.join(process.env.HOME, ".config", "Assemblr", "data", "saves"),
        darwin: path.join(
            process.env.HOME,
            "Library",
            "Application Support",
            "Assemblr",
            "data",
            "saves"
        ),
    },
};
// Config file ../config.json
config_file_location = path.join(__dirname, "..", "config.json");
// path.join(global.directories.program_root[global.platform], "config.json");

// class to create dialog boxes with electron
class Dialog {
    // create dialog box
    constructor(title, message, type, buttons) {
        // create dialog box
        this.dialog = electron.dialog.showMessageBoxSync({
            title: title,
            message: message,
            type: type,
            buttons: buttons,
        });
    }
    // return dialog box
    getDialog() {
        return this.dialog;
    }
}

// Read config file
function readConfig() {
    // read config file
    var config_file = fs.readFileSync(config_file_location, "utf-8");
    // parse config file
    var config = JSON.parse(config_file);
    // Set Globals from Config
    // Set Save File Location
    global.save_file_location = config.save_file_location;
}

// find file
function findFile(file_name, locations = ["./"]) {
    // global.directories.appdata[global.platform]
    // loop through locations
    for (var i = 0; i < locations.length; i++) {
        // Check if file exists
        if (fs.existsSync(path.join(locations[i], file_name))) {
            // return filepath
            return path.join(locations[i], file_name);
        } else {
            // FileNotFound Error
            // show dialog box
            var dialog = new Dialog(
                "File Not Found",
                "The file " + file_name + " was not found.",
                "error",
                ["OK"]
            );
            // return -1
            error("FileNotFound", "The file " + file_name + " was not found.");
            return -1; // FileNotFound Error
        }
    }
}


// Menu Creation

class MenuOption {
    // Each object should have the following properties:
    // name: The name of the button
    // action: The function to run when the button is clicked
    // icon: The icon to display on the button
    // size: The size of the button (1/2, full or double)
    constructor (name="",icon="",action= function(){alert("No action defined")}
    ,size=1) {
        this.name = name;
        this.icon = icon;
        this.action = action;
        this.size = size;
    }

    // Remove Attributes
    RemoveName() {
        // remove the name from the option
        this.name = "";
    }
    RemoveIcon() {
        // remove the icon from the option
        this.icon = "";
    }
    RemoveAction() {
        // remove the action from the option
        this.action = function(){alert("No action defined")};
    }
    RemoveSize() {
        // remove the size from the option
        this.size = 1;
    }
    
}

class Menu {
    // Menu should be an array of objects, all displayed as buttons on an overlay window
    

    constructor (titleBarName, menuObjects) {
        this.titleBarName = titleBarName;
        this.menuObjects = menuObjects;
    }
    ShowMenu() {
        // Shows the menu in a popup window

    }
    AddItem() {
        // add an item to the menu
        new MenuOption();
    }
    RemoveItem() {
        // remove the option from the menu
    }
}

MainMenu = new Menu("Main Menu",[]);
MainMenu.