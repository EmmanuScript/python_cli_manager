"""Storage module for task persistence"""
import json
import os
from pathlib import Path
import pickle  # INCONSISTENCY: Tests use json, storage defaults to pickle


class TaskStorage:
    """Handle task persistence"""
    
    def __init__(self, filepath="tasks.dat"):
        self.filepath = filepath
        self.tasks = {}
    
    def save(self, tasks):
        """Save tasks to file - uses pickle by default"""
        # TODO: Add error handling for file write failures
        try:
            with open(self.filepath, 'wb') as f:
                pickle.dump(tasks, f)
        except IOError:
            # ISSUE: Silent failure - no logging
            pass
    
    def load(self):
        """Load tasks from file"""
        # TODO: Handle file not found gracefully
        if not os.path.exists(self.filepath):
            return {}
        
        with open(self.filepath, 'rb') as f:
            return pickle.load(f)
    
    def save_json(self, tasks, filepath=None):
        """Save tasks as JSON - method exists but not used in main app"""
        if filepath is None:
            filepath = self.filepath.replace('.dat', '.json')
        
        with open(filepath, 'w') as f:
            json.dump(tasks, f, indent=2, default=str)
    
    def add_task(self, task):
        """Add task to storage"""
        # TODO: Validate task object
        self.tasks[task.id] = task
    
    def delete_task(self, task_id):
        """Delete task - NO VERIFICATION if task exists"""
        del self.tasks[task_id]
