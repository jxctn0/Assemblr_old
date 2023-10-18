//! import dev functions from "./dev.js";
import { dev } from "./dev.js";

window.addEventListener("DOMContentLoaded", (event) => {
    var lineCount = 1;
    const editor = document.getElementById("editorText");
    const lineNumbers = document.querySelector(".lineNumberContainer");

    function refreshLineNum() {
        // Get the number of lines in the editor
        lineCount = editor.value.split("\n").length;
        console.log(lineCount);
        // Clear the line numbers
        lineNumbers.innerHTML = "";
        // Add the line numbers
        for (let i = 1; i <= lineCount; i++) {
            // Create a new line number with padded 0s
            let newLineNum = document.createElement("span");
            newLineNum.className = "lineNum";
            newLineNum.innerHTML = i.toString().padStart(2, "0");
            // Add the line number to the line number container
            lineNumbers.appendChild(newLineNum);
        }
        console.log(lineNumbers.length);
    }

    // When the user makes edits to the editor, update the line numbers
    editor.addEventListener("input", function () {
        refreshLineNum();
    });

    //: on ctrl + s, save the file to a .asl file
    document.addEventListener("keydown", function (event) {
        if (event.ctrlKey && event.key === "s") {
            event.preventDefault();
            save();
        }
    });

    // on ctrl + o, open a .asl file
    document.addEventListener("keydown", function (event) {
        if (event.ctrlKey && event.key === "o") {
            event.preventDefault();
            open();
        }
    });
});

// Asynchronous check for file changes, if there is, then if autoSave is enabled, save the file
setInterval(function () {
    if (document.getElementById("editorText").value !== currentFileContents) {
        if (autoSave) {
            save();
        }
    }
}, autoSaveInterval);

// on tab, add 4 spaces to input
document.addEventListener("keydown", function (event) {
    if (event.key === "Tab") {
        event.preventDefault();
        // Get the editor
        const editor = document.getElementById("editorText");
        // Get the cursor position
        const cursorPos = editor.selectionStart;
        // Get the text before the cursor
        const textBeforeCursor = editor.value.substring(0, cursorPos);
        // Get the text after the cursor
        const textAfterCursor = editor.value.substring(
            cursorPos,
            editor.value.length
        );
        // Set the editor to the text before the cursor + 4 spaces + the text after the cursor
        editor.value = textBeforeCursor + "    " + textAfterCursor;
        // Set the cursor position to the end of the 4 spaces
        editor.selectionStart = cursorPos + 4;
        editor.selectionEnd = cursorPos + 4;
    }
});

// on ctrl + n, create a new file
document.addEventListener("keydown", function (event) {
    if (event.ctrlKey && event.key === "n") {
        event.preventDefault();
        newFile();
    }
});

ApplicationMenu = {
    File: {
        save: function () {},
        saveAs: function () {},
        open: function () {},
        new: function () {},
        toggleAutoSave: function () {
            autoSave = !autoSave;
            
        },
    },
};
