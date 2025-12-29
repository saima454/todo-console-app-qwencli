from dataclasses import dataclass


@dataclass
class Task:
    """
    Represents a single todo item with the following attributes:
    - id: int (unique, auto-increment starting from 1)
    - title: str (required, non-empty, max 200 chars)
    - description: str (optional, can be empty, max 1000 chars)
    - completed: bool (default: False)
    """
    id: int
    title: str
    description: str = ""
    completed: bool = False

    def __post_init__(self):
        """Validate the task attributes after initialization."""
        if not isinstance(self.id, int) or self.id <= 0:
            raise ValueError("ID must be a positive integer")
        
        if not isinstance(self.title, str) or not self.title.strip():
            raise ValueError("Title must be a non-empty string")
        
        if len(self.title) > 200:
            raise ValueError("Title must not exceed 200 characters")
        
        if not isinstance(self.description, str):
            raise ValueError("Description must be a string")
        
        if len(self.description) > 1000:
            raise ValueError("Description must not exceed 1000 characters")
        
        if not isinstance(self.completed, bool):
            raise ValueError("Completed must be a boolean value")
    
    def __str__(self):
        """Return a string representation of the task for display."""
        status = "[x]" if self.completed else "[ ]"
        return f"{self.id}. {status} {self.title} - {self.description if self.description else '(No description)'}"