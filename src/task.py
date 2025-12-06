"""Task model and operations"""
from datetime import datetime
from enum import Enum
import json


class TaskStatus(Enum):
    """Task status enumeration"""
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"
    BLOCKED = "blocked"


class Priority(Enum):
    """Priority levels for tasks"""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class Task:
    """Task object with metadata"""
    
    def __init__(self, title, description="", priority=Priority.MEDIUM, 
                 status=TaskStatus.TODO, assigned_to=None, due_date=None):
        self.id = None  # TODO: Generate unique ID
        self.title = title
        self.description = description
        self.priority = priority if isinstance(priority, Priority) else Priority[priority.upper()]
        self.status = status if isinstance(status, TaskStatus) else TaskStatus[status.upper()]
        self.assigned_to = assigned_to
        self.due_date = due_date
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.tags = []  # TODO: Implement tag filtering
    
    def update_status(self, new_status):
        """Update task status - NO VALIDATION FOR TRANSITIONS"""
        # NOTE: In test_task.py, we validate transitions, but this method doesn't
        if isinstance(new_status, str):
            new_status = TaskStatus[new_status.upper()]
        self.status = new_status
        self.updated_at = datetime.now()
    
    def to_dict(self):
        """Convert task to dictionary"""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "priority": self.priority.value,
            "status": self.status.value,
            "assigned_to": self.assigned_to,
            "due_date": self.due_date,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "tags": self.tags
        }
    
    def __repr__(self):
        return f"Task(id={self.id}, title={self.title}, status={self.status.value})"
