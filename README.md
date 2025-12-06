# Task Manager CLI

A lightweight command-line task management application written in Python.

## Overview

Task Manager CLI is a simple but growing tool for managing tasks and to-do items from the terminal. It provides basic CRUD operations, task filtering, and data persistence.

**Version:** 0.1.0  
**Status:** Early Beta

## Quick Start

```bash
# Install
python setup.py install

# Basic usage
task-manager add "My first task" --desc "Do something important"
task-manager list
task-manager update 0 done
```

## Features

### Implemented ✓

- **Add tasks** with title, description, priority, and assignment
- **List tasks** with optional filtering by status and priority
- **Update task status** (todo, in_progress, done, blocked)
- **Task persistence** to disk
- **Basic CLI interface** with argparse

### Partially Implemented ⚠️

- **Task filtering**: Works for status and priority, but no search by keyword
- **Export functionality**: Parameter for format selection exists but not implemented

### Not Yet Implemented ✗

The following features are documented in the code but not yet implemented:

1. **Task IDs**: Unique ID generation for tasks (currently uses memory address)
2. **Tag system**: Tag filtering and management mentioned in code
3. **Task sorting**: Sort options (by date, priority, assignee) in list command
4. **Error handling**: Validation for file operations, task boundaries, input validation
5. **User roles**: Task assignment with role-based access control
6. **Recurring tasks**: Repeat task scheduling
7. **Notifications**: Alert system for due dates and task updates
8. **Database backend**: Currently uses pickle file format; SQL support planned
9. **Multi-user support**: Single-user only; concurrent access not handled
10. **Task dependencies**: Ability to mark tasks as blocking other tasks
11. **CSV export**: CSV format export mentioned in CLI but format always uses pickle
12. **Undo/redo**: Change history and reversal
13. **Performance optimization**: Indexing and search optimization
14. **API layer**: REST API for task operations (CLI-only currently)
15. **Configuration file**: Uses hardcoded settings; config file loading not implemented

## Project Structure

```
task_manager/
├── src/
│   ├── __init__.py       # Package initialization
│   ├── task.py           # Task model and status enums
│   ├── storage.py        # Data persistence layer
│   ├── cli.py            # Command-line interface
│   └── logger.py         # (TODO: Add logging module)
├── tests/
│   ├── test_task.py      # Task unit tests
│   ├── test_storage.py   # Storage unit tests
│   └── test_cli.py       # (TODO: CLI integration tests)
├── config/
│   └── settings.py       # Configuration management
├── requirements.txt      # Dependencies
├── setup.py             # Package setup
└── README.md            # This file
```

## Commands

### Add Task

```bash
task-manager add <title> [--desc <description>] [--priority <low|medium|high>] [--assigned <user>]
```

**Example:**

```bash
task-manager add "Fix login bug" --desc "Users report 404 error" --priority high --assigned john
```

### List Tasks

```bash
task-manager list [--status <status>] [--priority <priority>]
```

**Filters:**

- `--status`: todo, in_progress, done, blocked
- `--priority`: low, medium, high

**Example:**

```bash
task-manager list --status in_progress --priority high
```

### Update Status

```bash
task-manager update <index> <status>
```

**Example:**

```bash
task-manager update 0 done
```

### Export Tasks

```bash
task-manager export [--format <json|csv>]
```

**Note:** Currently saves in pickle format regardless of --format parameter.

## Known Issues

1. **Silent failures**: File I/O errors are caught but not logged
2. **No ID generation**: Tasks don't have stable unique IDs
3. **Index-based updates**: Update command uses task list index, which changes when filtering
4. **Storage format mismatch**: Tests expect JSON serialization but CLI uses pickle
5. **No input validation**: No checks on title length, due dates, or priority values
6. **Inconsistent filtering patterns**: Status filter uses string comparison, priority filter uses enum
7. **Memory leak risk**: Tasks stored indefinitely without cleanup
8. **No bounds checking**: Update command crashes on invalid index

## Data Storage

Tasks are persisted to `tasks.dat` (pickle format) by default.

**Alternative storage methods exist but are not integrated:**

- `save_json()` method in TaskStorage class
- Development vs Production configurations defined but not used

## Status Transitions

Valid task status values:

- `todo` - Task not started (default)
- `in_progress` - Currently being worked on
- `done` - Task completed
- `blocked` - Task blocked by dependency

**Note:** No validation of valid state transitions in CLI. Use with caution!

## Configuration

Configuration files are defined in `config/settings.py` but not currently loaded from disk.

Environment variables:

- `TASK_MANAGER_ENV`: Set to "production" for production mode
- `TASK_STORAGE_FILE`: Override storage file path (production only)

## Testing

```bash
# Run all tests
python -m pytest tests/

# Run specific test file
python -m pytest tests/test_task.py

# Run with coverage
python -m pytest --cov=src tests/
```

**Test coverage areas:**

- Task model creation and status changes
- Storage save/load operations
- Serialization to dictionary format

## Contributing

This is an early-stage project. Areas needing work:

- Error handling and validation
- Feature implementation (see "Not Yet Implemented" section)
- Integration tests
- Documentation
- Performance optimization

## License

MIT

## Next Steps / Roadmap

- [ ] Implement stable task ID generation
- [ ] Add comprehensive error handling
- [ ] Implement tag-based filtering
- [ ] Add task sorting options
- [ ] Build REST API endpoint
- [ ] Add user authentication
- [ ] Migrate to SQLite backend
- [ ] Implement recurring tasks
- [ ] Add notification system
- [ ] Complete test coverage

---

**Last Updated:** December 2024
