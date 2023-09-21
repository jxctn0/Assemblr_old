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

// create menu using Javascript
function create_menu() {
    // create menu
    var menu_root = document.getElementById("menu-root");
    var menu_item = document.createElement("div");
    menu_item.classList.add("menu-item");
    // check if there is a save file with content
    // if there is, add a menu item to "Continue"
    // if there isn't, show "Start New" instead.
    if (findSave() != -1) {
        menu_item.innerHTML = "Continue";
        menu_item.id = "menu-item-continue";
        // add event listener to menu item
        menu_item.addEventListener("click", function () {
            // load last save in game.html
            // redirect to game.html
            save_file_location = preventDefault(); // prevent default action
            window.location.href =
                "../views/game.html?savefile=" + save_file_location; // redirect to game.html with save file
        });
    } else {
        menu_item.innerHTML = "Start New";
        menu_item.id = "menu-item-start-new";
    }
}

// wait for DOM to load
document.addEventListener("DOMContentLoaded", function (event) {
    // run menu script
    create_menu();
});
