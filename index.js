//! Electron Launcher

const { app, BrowserWindow } = require('electron'); //? imports electron
const path = require('path'); //? imports path

function createWindow() { //? creates the window
  const win = new BrowserWindow({
    width: function() { return electron.screen.getPrimaryDisplay().workAreaSize.width; }, //* set width to full screen: width: function() { return electron.screen.getPrimaryDisplay().workAreaSize.width; }
    height: function() { return electron.screen.getPrimaryDisplay().workAreaSize.height; }, //* set height to full screen: height: function() { return electron.screen.getPrimaryDisplay().workAreaSize.height; }
    webPreferences: {
      nodeIntegration: true //? allows node integration (node.js) in the window
    },
    //% HIDE MENU BAR
    autoHideMenuBar: true,
    //? SET WINDOW ICON
    icon: path.join(__dirname, 'assets', 'img', 'icons', '48x48', 'main_icon.png'),
  });

  win.loadFile(path.join(__dirname, 'views', 'editor.html')); //? loads the editor.html file
}

app.whenReady().then(() => {
  createWindow(); //? creates the window

  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) {
      createWindow();
    }
  });
});

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});