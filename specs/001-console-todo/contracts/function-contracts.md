# Function Contracts: Console Todo App

## TaskManager Class Interface

### add_task(title: str, description: str = "") -> int
**Purpose**: Add a new task to the in-memory storage
**Preconditions**: 
- title is a non-empty string
- description is a string (can be empty)
**Postconditions**:
- A new task is created with a unique auto-incrementing ID
- The task has completed=False by default
- Returns the ID of the newly created task
**Side Effects**: Modifies the internal task storage

### get_all_tasks() -> List[Task]
**Purpose**: Retrieve all tasks from storage
**Preconditions**: None
**Postconditions**:
- Returns a list of all tasks
- The list may be empty if no tasks exist
**Side Effects**: None

### get_task_by_id(task_id: int) -> Optional[Task]
**Purpose**: Retrieve a specific task by its ID
**Preconditions**: task_id is a positive integer
**Postconditions**:
- Returns the task if found
- Returns None if no task with the given ID exists
**Side Effects**: None

### update_task(task_id: int, title: str = None, description: str = None) -> bool
**Purpose**: Update the title and/or description of an existing task
**Preconditions**: 
- task_id is a positive integer
- If provided, title is a non-empty string
**Postconditions**:
- Returns True if the task was successfully updated
- Returns False if the task ID doesn't exist
- Updates only the fields that are provided
**Side Effects**: Modifies the specified task in storage

### delete_task(task_id: int) -> bool
**Purpose**: Remove a task from storage
**Preconditions**: task_id is a positive integer
**Postconditions**:
- Returns True if the task was successfully deleted
- Returns False if the task ID doesn't exist
- The task is removed from storage
**Side Effects**: Modifies the internal task storage

### toggle_task_completion(task_id: int) -> bool
**Purpose**: Toggle the completion status of a task
**Preconditions**: task_id is a positive integer
**Postconditions**:
- Returns True if the task status was successfully toggled
- Returns False if the task ID doesn't exist
- Changes the completed status from True to False or False to True
**Side Effects**: Modifies the completion status of the specified task

## CLI Interface Specifications

### display_menu() -> None
**Purpose**: Show the main menu options to the user
**Preconditions**: None
**Postconditions**: 
- Displays numbered options for all 5 Basic Level features plus Exit
- Options are clearly labeled
**Side Effects**: Outputs to console

### get_user_choice() -> int
**Purpose**: Prompt user for menu selection and validate input
**Preconditions**: None
**Postconditions**:
- Returns a valid menu option number (1-6)
- Handles invalid input gracefully with error message
**Side Effects**: Reads input from console

### handle_add_task() -> None
**Purpose**: Handle the add task workflow
**Preconditions**: None
**Postconditions**:
- Prompts user for task title and description
- Creates new task via TaskManager
- Displays confirmation or error message
**Side Effects**: Adds task to storage, outputs to console

### handle_view_tasks() -> None
**Purpose**: Display all tasks to the user
**Preconditions**: None
**Postconditions**:
- Shows all tasks with ID, title, description, and completion status
- Shows appropriate message if no tasks exist
**Side Effects**: Outputs to console

### handle_update_task() -> None
**Purpose**: Handle the update task workflow
**Preconditions**: None
**Postconditions**:
- Prompts user for task ID and new details
- Updates task via TaskManager
- Displays confirmation or error message
**Side Effects**: Modifies task in storage, outputs to console

### handle_delete_task() -> None
**Purpose**: Handle the delete task workflow
**Preconditions**: None
**Postconditions**:
- Prompts user for task ID
- Deletes task via TaskManager
- Displays confirmation or error message
**Side Effects**: Removes task from storage, outputs to console

### handle_mark_task() -> None
**Purpose**: Handle the mark task as complete/incomplete workflow
**Preconditions**: None
**Postconditions**:
- Prompts user for task ID
- Toggles completion status via TaskManager
- Displays confirmation or error message
**Side Effects**: Modifies task in storage, outputs to console