"""Command-line interface for task manager"""
import argparse
import sys
from task import Task, TaskStatus, Priority
from storage import TaskStorage


class TaskManagerCLI:
    """CLI interface for task management"""
    
    def __init__(self, storage_file="tasks.dat"):
        self.storage = TaskStorage(storage_file)
        self.tasks = self.storage.load() if isinstance(self.storage.load(), dict) else {}
    
    def add_task(self, title, description="", priority="medium", assigned_to=None):
        """Add a new task"""
        task = Task(
            title=title,
            description=description,
            priority=priority,
            assigned_to=assigned_to
        )
        # ISSUE: No task ID generation - tasks get None as ID
        self.tasks[id(task)] = task
        self.storage.add_task(task)
        print(f"✓ Task added: {title}")
    
    def list_tasks(self, filter_status=None, filter_priority=None):
        """List all tasks with optional filtering"""
        # TODO: Implement sorting options (by date, priority, etc.)
        
        tasks_to_show = self.tasks.values()
        
        if filter_status:
            # INCONSISTENCY: Different filtering patterns
            tasks_to_show = [t for t in tasks_to_show if t.status.value == filter_status]
        
        if filter_priority:
            # Different pattern than status filter - uses priority enum
            tasks_to_show = [t for t in tasks_to_show if t.priority == Priority[filter_priority.upper()]]
        
        if not tasks_to_show:
            print("No tasks found.")
            return
        
        for task in tasks_to_show:
            self._print_task(task)
    
    def update_status(self, task_index, new_status):
        """Update task status by index"""
        # UNSAFE: No bounds checking
        task_list = list(self.tasks.values())
        task_list[task_index].update_status(new_status)
        print(f"✓ Task status updated to {new_status}")
    
    def _print_task(self, task):
        """Print task in formatted way"""
        status_symbols = {
            TaskStatus.TODO: "☐",
            TaskStatus.IN_PROGRESS: "◐",
            TaskStatus.DONE: "☑",
            TaskStatus.BLOCKED: "⊘"
        }
        symbol = status_symbols.get(task.status, "?")
        print(f"{symbol} [{task.priority.value}] {task.title} - {task.description[:30]}")
    
    def export_tasks(self, format="json"):
        """Export tasks - format parameter ignored, always uses pickle"""
        # TODO: Implement actual format selection
        self.storage.save(self.tasks)
        print(f"✓ Tasks saved to {self.storage.filepath}")


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(description="Task Manager CLI")
    subparsers = parser.add_subparsers(dest="command", help="Commands")
    
    # Add task
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("title", help="Task title")
    add_parser.add_argument("--desc", help="Task description")
    add_parser.add_argument("--priority", choices=["low", "medium", "high"], default="medium")
    add_parser.add_argument("--assigned", help="Assign to user")
    
    # List tasks
    list_parser = subparsers.add_parser("list", help="List tasks")
    list_parser.add_argument("--status", choices=["todo", "in_progress", "done", "blocked"])
    list_parser.add_argument("--priority", choices=["low", "medium", "high"])
    
    # Update status
    update_parser = subparsers.add_parser("update", help="Update task status")
    update_parser.add_argument("index", type=int, help="Task index")
    update_parser.add_argument("status", choices=["todo", "in_progress", "done", "blocked"])
    
    # Export
    export_parser = subparsers.add_parser("export", help="Export tasks")
    export_parser.add_argument("--format", choices=["json", "csv"], default="json")
    
    args = parser.parse_args()
    cli = TaskManagerCLI()
    
    if args.command == "add":
        cli.add_task(
            title=args.title,
            description=args.desc or "",
            priority=args.priority,
            assigned_to=args.assigned
        )
    elif args.command == "list":
        cli.list_tasks(filter_status=args.status, filter_priority=args.priority)
    elif args.command == "update":
        cli.update_status(args.index, args.status)
    elif args.command == "export":
        cli.export_tasks(format=args.format)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
