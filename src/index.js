// First Hello World Electron App

const { app, BrowserWindow } = require('electron') // Electron 

// include the Node.js 'path' module at the top of your file
const path = require('node:path')

const createWindow = () => { // Create Window

    const win = new BrowserWindow({
        width: 800,
        height: 600,
        webPreferences: {
            preload: path.join(__dirname, 'preload.js')
        } // Load preload.js
    })


    win.loadFile('index.html') // Load index.html
}

app.whenReady().then(() => { // When app is ready create window
    createWindow() // Create window

    app.on('activate', () => { // When app is activated create window
        if (BrowserWindow.getAllWindows().length === 0) createWindow() // If no windows are open create window
    })
})

app.on('window-all-closed', () => { // When all windows are closed quit the app
    if (process.platform !== 'darwin') app.quit() // If not macOS quit the app 
    // this needs to be done because macOS apps stay open 
})