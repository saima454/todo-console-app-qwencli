"""
Validation functions for the Console Todo App.
These functions validate user inputs and return appropriate error messages.
"""


def validate_task_title(title):
    """
    Validates that the task title is non-empty and within length limits.
    
    Args:
        title (str): The task title to validate
        
    Returns:
        tuple: (is_valid: bool, error_message: str)
    """
    if not isinstance(title, str):
        return False, "Title must be a string"
    
    if not title.strip():
        return False, "Title cannot be empty"
    
    if len(title) > 200:
        return False, "Title must not exceed 200 characters"
    
    return True, ""


def validate_task_description(description):
    """
    Validates that the task description is within length limits.
    
    Args:
        description (str): The task description to validate
        
    Returns:
        tuple: (is_valid: bool, error_message: str)
    """
    if not isinstance(description, str):
        return False, "Description must be a string"
    
    if len(description) > 1000:
        return False, "Description must not exceed 1000 characters"
    
    return True, ""


def validate_task_id(task_id, task_manager):
    """
    Validates that the task ID exists in the task manager.
    
    Args:
        task_id (int): The task ID to validate
        task_manager: The TaskManager instance to check against
        
    Returns:
        tuple: (is_valid: bool, error_message: str)
    """
    if not isinstance(task_id, int) or task_id <= 0:
        return False, "Task ID must be a positive integer"
    
    task = task_manager.get_task_by_id(task_id)
    if task is None:
        return False, f"Task with ID {task_id} does not exist"
    
    return True, ""


def validate_menu_choice(choice):
    """
    Validates that the menu choice is a valid option (1-6).
    
    Args:
        choice (str or int): The menu choice to validate
        
    Returns:
        tuple: (is_valid: bool, error_message: str, choice_int: int)
    """
    try:
        choice_int = int(choice)
        if 1 <= choice_int <= 6:
            return True, "", choice_int
        else:
            return False, "Menu choice must be between 1 and 6", choice_int
    except ValueError:
        return False, "Menu choice must be a number", None


def validate_positive_integer(value_str, field_name="Value"):
    """
    Validates that a string represents a positive integer.
    
    Args:
        value_str (str): The string to validate
        field_name (str): The name of the field for error messages
        
    Returns:
        tuple: (is_valid: bool, error_message: str, value_int: int)
    """
    try:
        value_int = int(value_str)
        if value_int > 0:
            return True, "", value_int
        else:
            return False, f"{field_name} must be a positive integer", value_int
    except ValueError:
        return False, f"{field_name} must be a number", None