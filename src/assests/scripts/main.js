// Main 

// Importing modules:
// - Electron
const { app, BrowserWindow } = require('electron') // Electron

// - Node.js
const path = require('node:path') // Node.js path module
const fs = require('node:fs') // Node.js fs module

// Constants
if (process.platform === 'win32') { 
    const dataDir = process.env.APPDATA 
} 
else if (process.platform === 'darwin') { 
    const dataDir = process.env.HOME + '/Library/Application Support' 
} 
else if (process.platform === 'linux') {
    const dataDir = process.env.HOME + '/.config'
} else {
    const dataDir = process.env.HOME
}

console.log(dataDir)


function find_file(filename, additionalLocations = []) {
    const defaultLocations = [
        {
            platform: 'win32',
            path: path.join(process.env.APPDATA, 'Assemblr', filename),
        },
        {
            platform: 'darwin',
            path: path.join(process.env.HOME, 'Library', 'Application Support', 'Assemblr', filename),
        },
        {
            platform: 'linux',
            path: path.join(process.env.HOME, '.config', 'Assemblr', filename),
        },
        {
            platform: 'other',
            path: path.join(__dirname, filename),
        },
    ];

    const allLocations = defaultLocations.concat(additionalLocations);

    for (const location of allLocations) {
        if ((location.platform === process.platform || location.platform === 'other') && fs.existsSync(location.path)) {
            return [true, location.path];
        }
    }

    return [false, null];
}

const find_save = () => {
    const [found, path] = find_file('save.json');
    if (found) {
        return path;
    } else {
        return null;
    }
}


function createWindow(width, height, title) { // Create Window
    const win = new BrowserWindow({
        width: width,
        height: height,
        webPreferences: {
            preload: path.join(__dirname, 'preload.js')
        } // Load preload.js

    }) // Create window
}

function createMenu() { } // Create Menu (FOR NOW IN menu.html)

function loadConfig() { // Load config.json
    // Load config.json
    // - If config.json is not found, create it with default values (from file assets/defaults/config.json)
    // - If config.json is found, load it

    // Look for config file in the following locations:
    // - Windows: %APPDATA%/Roaming/Assemblr/config.json
    // - macOS: ~/Library/Application Support/Assemblr/config.json
    // - Linux: ~/.config/Assemblr/config.json
    // - Other: ./config.json

    cfg = find_file('config.json');

    if (cfg[0] == False) { // If config.json is not found, create it with default values (from file assets/defaults/config.json)
        // Create config.json with default values
        // - Read default config.json
        // - Write default config.json to cfg[1]
    
        fetch('assets/defaults/config.json')
            .then(response => response.json())
            .then(data => {
                fs.writeFile(cfg[1], data, (err) => {
                    if (err) throw err;
                    console.log('Config file created!');
                });
            });
    } else { // If config.json is found, load it
        // Load config.json
        // - Read config.json
        // - Save data as config

        fetch(cfg[1])
            .then(response => response.json())
            .then(data => {
                config = data;
            });
    }
}