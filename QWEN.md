# QWEN Prompt Templates for Console Todo App

This file contains prompt templates and instructions for using Qwen to generate code for the Console Todo App project.

## General Guidelines

- All code must be generated using Python standard library only (no external dependencies)
- Follow PEP 8 standards for Python code
- Use dataclasses for data models where appropriate
- Implement modular design with separate concerns (data model, storage operations, UI)
- Include proper error handling and input validation
- Write clear comments and docstrings

## Prompt Templates

### Task Data Model
```
Create a Python dataclass for a Task entity with the following attributes:
- id: int (unique, auto-increment starting from 1)
- title: str (required, non-empty, max 200 chars)
- description: str (optional, can be empty, max 1000 chars)
- completed: bool (default: False)

Include proper validation and string representation.
```

### TaskManager Class
```
Create a TaskManager class that handles in-memory storage of Task objects with these methods:
- add_task(title, description="") - adds a new task with auto-incrementing ID, returns the ID
- get_all_tasks() - returns all tasks
- get_task_by_id(task_id) - returns a specific task or None
- update_task(task_id, title=None, description=None) - updates a task, returns True/False
- delete_task(task_id) - deletes a task, returns True/False
- toggle_task_completion(task_id) - toggles completion status, returns True/False

Use a list for in-memory storage and implement proper validation.
```

### Input Validation Functions
```
Create validation functions for the todo app:
- validate_task_title(title) - checks if title is non-empty and within length limits
- validate_task_id(task_id, task_manager) - checks if task ID exists
- validate_menu_choice(choice) - checks if menu choice is valid
```

### Main Application Loop
```
Create a main application loop with a menu-driven interface that includes:
- Option 1: Add task
- Option 2: View tasks
- Option 3: Update task
- Option 4: Delete task
- Option 5: Mark task complete/incomplete
- Option 6: Exit

Implement proper input handling and error messages.
```

### Menu Display Function
```
Create a function that displays the main menu options clearly to the user.
```

### Add Task Handler
```
Create a function that handles adding a new task by prompting the user for title and description, validating inputs, and adding to the task manager.
```

### View Tasks Handler
```
Create a function that displays all tasks with proper formatting showing ID, title, description, and completion status ([ ] or [x]).
```

### Update Task Handler
```
Create a function that handles updating a task by prompting for task ID and new details, validating inputs, and updating via the task manager.
```

### Delete Task Handler
```
Create a function that handles deleting a task by prompting for task ID, validating the ID exists, and deleting via the task manager.
```

### Mark Task Handler
```
Create a function that handles toggling task completion status by prompting for task ID, validating the ID exists, and updating via the task manager.
```