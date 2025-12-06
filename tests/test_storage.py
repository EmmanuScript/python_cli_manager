"""Tests for storage module"""
import unittest
import json
import os
from storage import TaskStorage
from task import Task, TaskStatus, Priority


class TestTaskStorage(unittest.TestCase):
    """Test TaskStorage class"""
    
    def setUp(self):
        self.storage = TaskStorage("test_tasks.dat")
    
    def tearDown(self):
        if os.path.exists("test_tasks.dat"):
            os.remove("test_tasks.dat")
        if os.path.exists("test_tasks.json"):
            os.remove("test_tasks.json")
    
    def test_save_and_load_pickle(self):
        """Test save and load with pickle"""
        task = Task(title="Test", priority=Priority.MEDIUM)
        task.id = 1
        tasks = {1: task}
        
        self.storage.save(tasks)
        loaded = self.storage.load()
        
        self.assertIsNotNone(loaded)
        self.assertEqual(len(loaded), 1)
    
    def test_save_json(self):
        """Test JSON export - but note CLI doesn't use this"""
        task = Task(title="Test", priority=Priority.MEDIUM)
        task.id = 1
        tasks = {1: task}
        
        self.storage.save_json(tasks, "test_tasks.json")
        
        with open("test_tasks.json", 'r') as f:
            data = json.load(f)
        
        self.assertIsNotNone(data)


if __name__ == "__main__":
    unittest.main()
