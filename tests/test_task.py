"""Tests for task module"""
import unittest
from task import Task, TaskStatus, Priority
from datetime import datetime


class TestTask(unittest.TestCase):
    """Test Task class"""
    
    def setUp(self):
        self.task = Task(
            title="Test Task",
            description="A test task",
            priority=Priority.HIGH
        )
    
    def test_task_creation(self):
        """Test task can be created"""
        self.assertEqual(self.task.title, "Test Task")
        self.assertEqual(self.task.priority, Priority.HIGH)
        self.assertEqual(self.task.status, TaskStatus.TODO)
    
    def test_status_transitions(self):
        """Test valid status transitions"""
        # NOTE: This test expects validation, but cli.py's update_status() doesn't validate!
        self.task.update_status(TaskStatus.IN_PROGRESS)
        self.assertEqual(self.task.status, TaskStatus.IN_PROGRESS)
        
        self.task.update_status(TaskStatus.DONE)
        self.assertEqual(self.task.status, TaskStatus.DONE)
    
    def test_task_serialization(self):
        """Test task can be serialized to dict"""
        task_dict = self.task.to_dict()
        self.assertIn("title", task_dict)
        self.assertIn("status", task_dict)
        self.assertEqual(task_dict["status"], "todo")


if __name__ == "__main__":
    unittest.main()
