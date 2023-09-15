///////////////////////////////////////////////////////////////////////////////////
// Description:
// This file is responsible for rendering the React.js components to the HTML file.
////////////////////////////////////////////////////////////////////////////////////


// Import the necessary modules.
// React.js is imported so we can use it.
// import React from 'react'

function MyButton() { // THIS links to the function below
    return (
        <button>
            I'm a button
        </button>
    );
}

// Export the MyButton component.
export default function MyApp() {
    return (
      <div>
        <h1>Welcome to my app</h1>
        <MyButton /> {/* THIS links to the function above */}
      </div>
    );
  }
  