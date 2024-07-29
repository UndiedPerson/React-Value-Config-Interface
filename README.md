# Servo Configurator

A web application for configuring servo settings. Built with React and TypeScript on the frontend and Node.js with Express on the backend.

## Project Structure

- **Frontend:** Located in the `frontend` directory.
- **Backend:** Located in the `backend` directory.

## Installation

### Prerequisites

Ensure you have [Node.js](https://nodejs.org/) and [Yarn](https://yarnpkg.com/) installed on your system.

### Backend

1. **Navigate to the Backend Directory**

   cd backend

2. **Install Backend Dependencies**

    yarn install

3. **Start the Backend Server**

    yarn start

This will start the server on port 5000. The backend handles configuration file saving and loading.

### Frontend

1. **Navigate to the Frontend Directory**

    cd frontend

2. **Install Frontend Dependencies**

    yarn install

3. **Start the Frontend Development Server**

    yarn start

This will start the React development server, which will open the application in your default web browser.


# Usage
# Access the Application

Open your web browser and go to http://localhost:3000 (or the port specified by your React development server).

# Interact with the Form

Input Fields: Enter values directly. The form only accepts user input without scroll options.
Save Button: Click to save the configuration. The status will update to reflect the save operation.
Status Message: Shows the result of the save operation.
# Configuration File
Location: The configuration file is saved in the Config directory within the backend folder.
Format: The configuration is stored in JSON format.
# CSS Styling
The frontend is styled to ensure a clean and centered layout with a focus on usability. The .window-box class ensures that the form is centered and covers the full viewport.

# Troubleshooting
Error Saving Config: Ensure that the backend server is running and that you have write permissions to the Config directory.
No Configuration Loaded: Ensure the backend server is running and correctly handles the /load-config endpoint.
# Contributing
Feel free to fork the repository and submit pull requests. Ensure that your changes are well-tested and adhere to the project’s coding standards.

# License
Specify the license under which the project is distributed.
