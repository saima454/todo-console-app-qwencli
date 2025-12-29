"""
Configuration constants for the Console Todo App.
"""

# Task-related constants
MAX_TITLE_LENGTH = 200
MAX_DESCRIPTION_LENGTH = 1000

# Menu-related constants
MENU_OPTIONS = {
    1: "Add task",
    2: "View tasks", 
    3: "Update task",
    4: "Delete task",
    5: "Mark as complete/incomplete",
    6: "Exit"
}

# Display-related constants
COMPLETED_INDICATOR = "[x]"
INCOMPLETE_INDICATOR = "[ ]"

# Error messages
ERROR_MESSAGES = {
    "invalid_task_id": "Task ID not found",
    "invalid_menu_choice": "Invalid menu choice. Please select 1-6.",
    "empty_title": "Title cannot be empty",
    "invalid_input": "Invalid input. Please try again."
}