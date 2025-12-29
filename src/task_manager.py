"""
TaskManager class for the Console Todo App.
Handles in-memory storage and operations for Task objects.
"""
from typing import List, Optional
from models.task import Task


class TaskManager:
    """
    Manages in-memory storage of Task objects with CRUD operations.
    
    Responsibilities:
    - Store tasks in memory
    - Provide CRUD operations for tasks
    - Generate unique IDs for new tasks
    - Validate task data before operations
    """
    
    def __init__(self):
        """Initialize the TaskManager with an empty task list and ID counter."""
        self.tasks: List[Task] = []
        self._next_id = 1
    
    def add_task(self, title: str, description: str = "") -> int:
        """
        Add a new task to the in-memory storage.
        
        Args:
            title (str): The task title (required, non-empty)
            description (str): The task description (optional)
            
        Returns:
            int: The ID of the newly created task
        """
        # Validate inputs
        if not title or not title.strip():
            raise ValueError("Title cannot be empty")
        
        if len(title) > 200:
            raise ValueError("Title must not exceed 200 characters")
        
        if len(description) > 1000:
            raise ValueError("Description must not exceed 1000 characters")
        
        # Create new task with auto-incrementing ID
        new_task = Task(
            id=self._next_id,
            title=title.strip(),
            description=description.strip(),
            completed=False
        )
        
        # Add task to storage
        self.tasks.append(new_task)
        
        # Increment ID for next task
        self._next_id += 1
        
        return new_task.id
    
    def get_all_tasks(self) -> List[Task]:
        """
        Retrieve all tasks from storage.
        
        Returns:
            List[Task]: A list of all tasks (may be empty if no tasks exist)
        """
        return self.tasks.copy()  # Return a copy to prevent external modification
    
    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """
        Retrieve a specific task by its ID.
        
        Args:
            task_id (int): The ID of the task to retrieve (must be a positive integer)
            
        Returns:
            Optional[Task]: The task if found, None if no task with the given ID exists
        """
        if not isinstance(task_id, int) or task_id <= 0:
            return None
        
        for task in self.tasks:
            if task.id == task_id:
                return task
        
        return None
    
    def update_task(self, task_id: int, title: str = None, description: str = None) -> bool:
        """
        Update the title and/or description of an existing task.
        
        Args:
            task_id (int): The ID of the task to update (must be a positive integer)
            title (str, optional): New title for the task (if provided, must be non-empty)
            description (str, optional): New description for the task
            
        Returns:
            bool: True if the task was successfully updated, False if the task ID doesn't exist
        """
        # Find the task to update
        task = self.get_task_by_id(task_id)
        if task is None:
            return False
        
        # Validate and update title if provided
        if title is not None:
            if not title.strip():
                raise ValueError("Title cannot be empty")
            
            if len(title) > 200:
                raise ValueError("Title must not exceed 200 characters")
            
            task.title = title.strip()
        
        # Update description if provided
        if description is not None:
            if len(description) > 1000:
                raise ValueError("Description must not exceed 1000 characters")
            
            task.description = description.strip()
        
        return True
    
    def delete_task(self, task_id: int) -> bool:
        """
        Remove a task from storage.
        
        Args:
            task_id (int): The ID of the task to remove (must be a positive integer)
            
        Returns:
            bool: True if the task was successfully deleted, False if the task ID doesn't exist
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            return False
        
        self.tasks.remove(task)
        return True
    
    def toggle_task_completion(self, task_id: int) -> bool:
        """
        Toggle the completion status of a task.
        
        Args:
            task_id (int): The ID of the task to toggle (must be a positive integer)
            
        Returns:
            bool: True if the task status was successfully toggled, False if the task ID doesn't exist
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            return False
        
        task.completed = not task.completed
        return True
    
    def get_next_id(self) -> int:
        """
        Get the next available ID without incrementing the counter.
        
        Returns:
            int: The next available ID
        """
        return self._next_id