# Quickstart Guide: Console Todo App

## Setup

### Prerequisites
- Python 3.13+ installed on your system
- UV package manager (for virtual environment management, though no additional packages will be installed)

### Installation Steps
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. Create and activate a virtual environment using UV:
   ```bash
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Verify Python version:
   ```bash
   python --version
   ```
   Ensure you're using Python 3.13+ as required by the constitution.

## Running the Application

1. Navigate to the source directory:
   ```bash
   cd src/
   ```

2. Run the application:
   ```bash
   python main.py
   ```

## Using the Application

Once the application starts, you'll see a menu with the following options:

1. **Add task**: Prompts for a title and optional description, then adds the task to your list with a unique ID
2. **View tasks**: Displays all tasks with their ID, title, description, and completion status ([ ] or [x])
3. **Update task**: Prompts for a task ID and allows you to modify the title and/or description
4. **Delete task**: Prompts for a task ID and removes the task from your list
5. **Mark as complete/incomplete**: Prompts for a task ID and toggles its completion status
6. **Exit**: Gracefully exits the application

### Example Usage Flow
1. Select "Add task" to create your first task
2. Enter a title (required) and description (optional)
3. Select "View tasks" to see your task list
4. Use other menu options to manage your tasks
5. Select "Exit" when finished

## Troubleshooting

- If you get an error about Python version, ensure you're using Python 3.13+
- If the application crashes, check that you're entering valid inputs (e.g., numeric IDs when prompted)
- For empty list errors, the application should handle these gracefully with appropriate messages

## Verification

After running the application, verify that:
- All 5 Basic Level features work correctly
- Tasks are properly stored in memory during the session
- Tasks are lost when the application exits (confirming in-memory storage)
- Error handling works for invalid inputs and non-existent task IDs
- The interface is user-friendly with clear prompts and formatted output