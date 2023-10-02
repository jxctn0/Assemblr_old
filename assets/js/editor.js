window.addEventListener("DOMContentLoaded", (event) => {
    var lineCount = 1;
    const editor = document.getElementById("editorText");
    const lineNumbers = document.querySelector(
        ".lineNumberContainer"
    );

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
            // Get the text from the editor
            const text = editor.value;
            // Create a new file
            const file = new Blob([text], { type: "text/plain" });
            // Create a new URL for the file
            const url = URL.createObjectURL(file);
            // Create a new link
            const link = document.createElement("a");
            // Set the link to the file
            link.href = url;
            // Set the link to download the file
            link.download = "file.asl";
            // Click the link
            link.click();
        }
    });

    // on ctrl + o, open a .asl file
    document.addEventListener("keydown", function (event) {
        if (event.ctrlKey && event.key === "o") {
            event.preventDefault();
            // Create a new input
            const input = document.createElement("input");
            // Set the input to only accept .asl files
            input.accept = ".asl,";
            input.name = "asl";
            // set the input to reject all other files
            input.setAttribute("capture", "capture");
            // Set the input to be hidden
            input.style.display = "none";
            // Set the input to be a file input
            input.type = "file";
            // Add an event listener to the input
            input.addEventListener("change", function (event) {
                // Get the file
                const file = event.target.files[0];
                // Create a new file reader
                const reader = new FileReader();
                // Add an event listener to the reader
                reader.addEventListener("load", function (event) {
                    // Get the text from the file
                    const text = event.target.result;
                    // Set the editor to the text
                    editor.value = text;
                });
                // Read the file
                reader.readAsText(file);
            });
            // Click the input
            input.click();

            // refresh the line numbers
            refreshLineNum();
        }
    });
});

// on tab, add 4 spaces to input
document.addEventListener("keydown", function (event) {
    if (event.key === "Tab") {
        event.preventDefault();
        // Get the editor
        const editor = document.getElementById("editorText");
        // Get the cursor position
        const cursorPos = editor.selectionStart;
        // Get the text before the cursor
        const textBeforeCursor = editor.value.substring(
            0,
            cursorPos
        );
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
        // ask the user if they want to save the file
        const save = confirm("Do you want to save the file?");
        // if the user wants to save the file, save it
        if (save) {
            // Get the text from the editor
            const text = editor.value;
            // Create a new file
            const file = new Blob([text], { type: "text/plain" });
            // Create a new URL for the file
            const url = URL.createObjectURL(file);
            // Create a new link
            const link = document.createElement("a");
            // Set the link to the file
            link.href = url;
            // Set the link to download the file
            link.download = "file.asl";
            // Click the link
            link.click();
        }
        // Get the editor
        const editor = document.getElementById("editorText");
        // Set the editor to be empty
        editor.value = "";
        // refresh the line numbers
        refreshLineNum();
    }
});