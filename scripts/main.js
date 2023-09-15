//////////////////////////////////////////////////////////////////////////////////////////////////////
// Description:
// This is the main file for the Electron app. It is responsible for creating the window and loading
// the HTML file. It also contains some code that is specific to Mac OS.
//////////////////////////////////////////////////////////////////////////////////////////////////////

// Importing modules
const { app, BrowserWindow } = require('electron') // Electron modules are imported to create the window

const path = require('node:path') // Node.js path module is used to get the path to the HTML file

// module to parse the command line arguments
const minimist = require('minimist')

// Function to create the window
const createWindow = () => {
    const win = new BrowserWindow({
        width: 800,
        height: 600,
        webPreferences: {
            preload: path.join(__dirname, 'preload.js')
        }
    })


    win.loadFile('../views/index.html')
}

// Call the createWindow function when the app is ready
app.whenReady().then(() => {
    createWindow()
})

// Mac OS specific code
function macosSpecific() {
    app.on('window-all-closed', () => {
        if (process.platform !== 'darwin') app.quit()
    })

    app.whenReady().then(() => {
        createWindow()

        app.on('activate', () => {
            if (BrowserWindow.getAllWindows().length === 0) createWindow()
        })
    })
}

// Call the macosSpecific function if the platform is Mac OS
if (process.platform === 'darwin') macosSpecific()


// Parse the command line arguments
const args = minimist(process.argv.slice(2)) // main.js --verbose

// Check if verbose mode is enabled
if (args.verbose) {

    // Greet user in terminal if verbose mode is enabled



    console.log('Hello, Welcome to Assemblr!')
    console.log('Verbose Mode is enabled!')
    console.log(`
----------------------------------------
Version: \t\t${process.env.npm_package_version}
Platform: \t\t${process.platform}
Architecture: \t\t${process.arch}
Node.js version: \t${process.version}
Electron version: \t${process.versions.electron}
Chromium version: \t${process.versions.chrome}

`)
    console.log('Please enjoy your stay!')
}