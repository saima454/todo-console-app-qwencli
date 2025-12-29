"""
Main application file for the Console Todo App.
Implements the menu-driven interface and handles user interactions.
"""
from typing import Optional
import sys
from task_manager import TaskManager
from utils.validation import validate_task_title, validate_task_description
from config import MENU_OPTIONS



def display_menu():
    """
    Show the main menu options to the user.
    Displays numbered options for all 5 Basic Level features plus Exit.
    """
    print("\n" + "="*40)
    print("         CONSOLE TODO APP")
    print("="*40)
    
    for option_num, option_desc in MENU_OPTIONS.items():
        print(f"{option_num}. {option_desc}")
    
    print("="*40)


def get_user_choice() -> Optional[int]:
    """
    Prompt user for menu selection and validate input.
    
    Returns:
        int: A valid menu option number (1-6), or None if user enters invalid input
    """
    try:
        choice = input("\nSelect an option (1-6): ").strip()
        
        if not choice:
            print("Please enter a number between 1 and 6.")
            return None
        
        choice_int = int(choice)
        
        if 1 <= choice_int <= 6:
            return choice_int
        else:
            print("Invalid choice. Please select a number between 1 and 6.")
            return None
            
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 6.")
        return None


def handle_add_task(task_manager_instance):
    """
    Handle the add task workflow.
    Prompts user for task title and description, creates new task via TaskManager,
    and displays confirmation or error message.
    """
    print("\n--- Add New Task ---")

    # Get title from user
    title = input("Enter task title (required): ").strip()

    # Validate title
    is_valid, error_msg = validate_task_title(title)
    if not is_valid:
        print(f"Error: {error_msg}")
        return

    # Get description from user (optional)
    description = input("Enter task description (optional, press Enter to skip): ").strip()

    # Validate description if provided
    if description:
        is_valid, error_msg = validate_task_description(description)
        if not is_valid:
            print(f"Error: {error_msg}")
            return

    # Add task to manager
    try:
        task_id = task_manager_instance.add_task(title, description)
        print(f"Task added successfully with ID: {task_id}")
    except ValueError as e:
        print(f"Error adding task: {e}")


def handle_view_tasks(task_manager_instance):
    """
    Display all tasks to the user with proper formatting.
    Shows all tasks with ID, title, description, and completion status ([ ] or [x]).
    Shows appropriate message if no tasks exist.
    """
    print("\n--- View All Tasks ---")

    tasks = task_manager_instance.get_all_tasks()

    if not tasks:
        print("No tasks found. Your todo list is empty.")
        return

    print(f"Found {len(tasks)} task(s):")
    print("-" * 60)

    for task in tasks:
        status = "[x]" if task.completed else "[ ]"
        print(f"{task.id}. {status} {task.title}")
        if task.description:
            print(f"    Description: {task.description}")
        print()  # Empty line for better readability


def handle_update_task(task_manager_instance):
    """
    Handle the update task workflow.
    Prompts user for task ID and new details, validates inputs, and updates via TaskManager.
    Displays confirmation or error message.
    """
    print("\n--- Update Task ---")

    # Check if there are any tasks
    tasks = task_manager_instance.get_all_tasks()
    if not tasks:
        print("No tasks available to update. Please add some tasks first.")
        return

    # Display all tasks for reference
    print("Current tasks:")
    for task in tasks:
        status = "[x]" if task.completed else "[ ]"
        print(f"  {task.id}. {status} {task.title}")

    # Get task ID from user
    task_id_input = input("\nEnter the task ID to update: ").strip()

    # Validate task ID input
    try:
        task_id = int(task_id_input)
    except ValueError:
        print("Error: Task ID must be a number.")
        return

    # Validate that the task exists
    task = task_manager_instance.get_task_by_id(task_id)
    if task is None:
        print(f"Error: Task with ID {task_id} does not exist.")
        return

    print(f"Current task details:")
    print(f"  Title: {task.title}")
    print(f"  Description: {task.description if task.description else '(No description)'}")

    # Get new title from user (or keep current if empty input)
    new_title = input(f"\nEnter new title (current: '{task.title}', press Enter to keep current): ").strip()
    if not new_title:
        new_title = task.title  # Keep current title if user presses Enter

    # Get new description from user (or keep current if empty input)
    new_description = input(f"Enter new description (current: '{task.description if task.description else '(No description)'}', press Enter to keep current): ").strip()
    if not new_description and task.description:  # Only keep current if there was one
        new_description = task.description
    elif not new_description and not task.description:  # If both are empty, keep as empty
        new_description = ""

    # Validate the new title if it's different
    if new_title != task.title:
        is_valid, error_msg = validate_task_title(new_title)
        if not is_valid:
            print(f"Error: {error_msg}")
            return

    # Validate the new description if it's different
    if new_description != task.description:
        is_valid, error_msg = validate_task_description(new_description)
        if not is_valid:
            print(f"Error: {error_msg}")
            return

    # Update the task
    try:
        success = task_manager_instance.update_task(task_id, new_title, new_description)

        if success:
            updated_task = task_manager_instance.get_task_by_id(task_id)
            print(f"Task updated successfully!")
            print(f"New details:")
            print(f"  ID: {updated_task.id}")
            print(f"  Title: {updated_task.title}")
            print(f"  Description: {updated_task.description if updated_task.description else '(No description)'}")
            print(f"  Status: {'[x] Complete' if updated_task.completed else '[ ] Incomplete'}")
        else:
            print("Error: Could not update task.")
    except ValueError as e:
        print(f"Error updating task: {e}")


def handle_mark_task(task_manager_instance):
    """
    Handle the mark task as complete/incomplete workflow.
    Prompts user for task ID, validates the ID exists, and toggles completion status via TaskManager.
    Displays confirmation or error message.
    """
    print("\n--- Mark Task as Complete/Incomplete ---")

    # Check if there are any tasks
    tasks = task_manager_instance.get_all_tasks()
    if not tasks:
        print("No tasks available to mark. Please add some tasks first.")
        return

    # Display all tasks for reference
    print("Current tasks:")
    for task in tasks:
        status = "[x]" if task.completed else "[ ]"
        print(f"  {task.id}. {status} {task.title}")

    # Get task ID from user
    task_id_input = input("\nEnter the task ID to toggle completion status: ").strip()

    # Validate task ID input
    try:
        task_id = int(task_id_input)
    except ValueError:
        print("Error: Task ID must be a number.")
        return

    # Validate that the task exists
    task = task_manager_instance.get_task_by_id(task_id)
    if task is None:
        print(f"Error: Task with ID {task_id} does not exist.")
        return

    # Toggle the completion status
    success = task_manager_instance.toggle_task_completion(task_id)

    if success:
        # Get the updated task to show the new status
        updated_task = task_manager_instance.get_task_by_id(task_id)
        new_status = "[x]" if updated_task.completed else "[ ]"
        print(f"Task '{updated_task.title}' marked as {'complete' if updated_task.completed else 'incomplete'}.")
        print(f"New status: {updated_task.id}. {new_status} {updated_task.title}")
    else:
        print("Error: Could not toggle task completion status.")


def handle_delete_task(task_manager_instance):
    """
    Handle the delete task workflow.
    Prompts user for task ID, validates the ID exists, and removes via TaskManager.
    Displays confirmation or error message.
    """
    print("\n--- Delete Task ---")

    # Check if there are any tasks
    tasks = task_manager_instance.get_all_tasks()
    if not tasks:
        print("No tasks available to delete. Please add some tasks first.")
        return

    # Display all tasks for reference
    print("Current tasks:")
    for task in tasks:
        status = "[x]" if task.completed else "[ ]"
        print(f"  {task.id}. {status} {task.title}")

    # Get task ID from user
    task_id_input = input("\nEnter the task ID to delete: ").strip()

    # Validate task ID input
    try:
        task_id = int(task_id_input)
    except ValueError:
        print("Error: Task ID must be a number.")
        return

    # Validate that the task exists
    task = task_manager_instance.get_task_by_id(task_id)
    if task is None:
        print(f"Error: Task with ID {task_id} does not exist.")
        return

    # Confirm deletion
    confirm = input(f"Are you sure you want to delete task '{task.title}'? (y/N): ").strip().lower()
    if confirm not in ['y', 'yes']:
        print("Task deletion cancelled.")
        return

    # Delete the task
    success = task_manager_instance.delete_task(task_id)

    if success:
        print(f"Task '{task.title}' (ID: {task_id}) deleted successfully.")
    else:
        print("Error: Could not delete task.")


def handle_exit():
    """
    Implement graceful exit functionality for menu option 6.
    """
    print("\nThank you for using the Console Todo App. Goodbye!")
    import sys
    sys.exit(0)


def main():
    """
    Main application loop with menu-driven interface.
    """
    task_manager_instance = TaskManager()

    print("Welcome to the Console Todo App!")

    while True:
        try:
            display_menu()
            choice = get_user_choice()

            if choice is None:
                continue  # Invalid input, show menu again

            if choice == 1:
                handle_add_task(task_manager_instance)
            elif choice == 2:
                handle_view_tasks(task_manager_instance)
            elif choice == 3:
                handle_update_task(task_manager_instance)
            elif choice == 4:
                handle_delete_task(task_manager_instance)
            elif choice == 5:
                handle_mark_task(task_manager_instance)
            elif choice == 6:
                handle_exit()

            # Pause to let user see the result before showing menu again
            input("\nPress Enter to continue...")

        except KeyboardInterrupt:
            print("\n\nOperation cancelled by user. Exiting...")
            handle_exit()
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}")
            print("Please try again or restart the application.")
            input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()