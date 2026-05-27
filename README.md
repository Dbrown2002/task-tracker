# Task Tracker CLI

> **Repository:** [github.com/Dbrown2002/task-tracker](https://github.com/Dbrown2002/task-tracker)
> **Project:** [roadmap.sh/projects/task-tracker](https://roadmap.sh/projects/task-tracker)

A command-line task manager that stores tasks locally in `tasks.json`.

## Requirements

- Python 3.6+

## Setup

Clone or download the project, then run commands from the project folder.

**Windows** — use the included `task-cli.bat` wrapper:

```
task-cli <command> [args]
```

**Any platform** — call Python directly:

```
python main.py <command> [args]
```

---

## Commands

### Add a task

```
task-cli add "<description>"
```

```
task-cli add "Buy groceries"
# Task added successfully (ID: 1)
```

### Update a task

```
task-cli update <id> "<description>" <status>
```

```
task-cli update 1 "Buy groceries and cook dinner" in-progress
```

Valid statuses: `todo`, `in-progress`, `done`

### Delete a task

```
task-cli delete <id>
```

```
task-cli delete 1
```

### Mark a task as in progress

```
task-cli mark-in-progress <id>
```

```
task-cli mark-in-progress 1
```

### Mark a task as done

```
task-cli mark-done <id>
```

```
task-cli mark-done 1
```

### List tasks

```
task-cli list                # all tasks
task-cli list todo           # only todo
task-cli list in-progress    # only in-progress
task-cli list done           # only done
```

---

## Task Storage

Tasks are saved to `tasks.json` in the project folder. Each task has:

| Field         | Description                      |
| ------------- | -------------------------------- |
| `id`          | Auto-incremented integer         |
| `description` | Task text                        |
| `status`      | `todo`, `in-progress`, or `done` |
| `createdAt`   | ISO timestamp set on creation    |
| `updatedAt`   | ISO timestamp set on last update |
