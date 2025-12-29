# Data Model: Console Todo App

## Task Entity

### Attributes
- **id**: int
  - Unique auto-incrementing integer starting from 1
  - Required field
  - Primary identifier for the task
- **title**: str
  - Required field
  - Non-empty string representing the task title
  - Maximum length: 200 characters (practical limit for console display)
- **description**: str
  - Optional field
  - Can be empty string
  - Maximum length: 1000 characters (practical limit for console display)
- **completed**: bool
  - Default value: False
  - Represents the completion status of the task

### Validation Rules
- id must be a positive integer
- title must be a non-empty string
- title must not exceed 200 characters
- description, if provided, must not exceed 1000 characters
- completed must be a boolean value

### State Transitions
- A task can transition from `completed=False` to `completed=True` (mark as complete)
- A task can transition from `completed=True` to `completed=False` (mark as incomplete)

## TaskManager Entity

### Responsibilities
- Store tasks in memory
- Provide CRUD operations for tasks
- Generate unique IDs for new tasks
- Validate task data before operations

### Operations
- **Create Task**: Add a new task with auto-generated ID
- **Read Tasks**: Retrieve all tasks or a specific task by ID
- **Update Task**: Modify an existing task's title or description
- **Delete Task**: Remove a task by ID
- **Toggle Completion**: Change the completion status of a task

### Validation Rules
- No duplicate IDs allowed
- Task with non-existent ID cannot be updated/deleted/toggled
- Title must not be empty when creating or updating a task