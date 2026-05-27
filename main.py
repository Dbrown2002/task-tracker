import sys
import json
import os
from datetime import datetime
from task import Task

TASKS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tasks.json")


def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        return [Task.from_dict(d) for d in json.load(f)]


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump([t.to_dict() for t in tasks], f, indent=2)


def next_id(tasks):
    return max((t.id for t in tasks), default=0) + 1


def cmd_add(tasks, description):
    task = Task(next_id(tasks), description)
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {task.id})")


def cmd_update(tasks, id, description, status):
    for t in tasks:
        if t.id == id:
            t.description = description
            t.updated_at = datetime.now().isoformat()
            t.status = status
            save_tasks(tasks)
            print(f"Task {id} updated successfully")
            return
    print(f"Error: Task {id} not found")


def cmd_delete(tasks, id):
    for i, t in enumerate(tasks):
        if t.id == id:
            tasks.pop(i)
            save_tasks(tasks)
            print(f"Task {id} deleted successfully")
            return
    print(f"Error: Task {id} not found")


def cmd_mark(tasks, id, status):
    for t in tasks:
        if t.id == id:
            t.status = status
            t.updated_at = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {id} marked as {status}")
            return
    print(f"Error: Task {id} not found")


def cmd_list(tasks, status=None):
    filtered = [t for t in tasks if status is None or t.status == status]
    if not filtered:
        print("No tasks found")
        return
    for t in filtered:
        updated = f"  Updated: {t.updated_at}" if t.updated_at else ""
        print(f"[{t.id}] ({t.status}) {t.description}  Created: {t.created_at}{updated}")


def usage():
    print("Usage:")
    print("  task-cli add <description>")
    print("  task-cli update <id> <description> <status>")
    print("  task-cli delete <id>")
    print("  task-cli mark-in-progress <id>")
    print("  task-cli mark-done <id>")
    print("  task-cli list [done|todo|in-progress]")


def main():
    args = sys.argv[1:]
    if not args:
        usage()
        return

    tasks = load_tasks()
    cmd = args[0]

    if cmd == "add" and len(args) == 2:
        cmd_add(tasks, args[1])
    elif cmd == "update" and len(args) == 4:
        cmd_update(tasks, int(args[1]), args[2], args[3])
    elif cmd == "delete" and len(args) == 2:
        cmd_delete(tasks, int(args[1]))
    elif cmd == "mark-in-progress" and len(args) == 2:
        cmd_mark(tasks, int(args[1]), "in-progress")
    elif cmd == "mark-done" and len(args) == 2:
        cmd_mark(tasks, int(args[1]), "done")
    elif cmd == "list":
        status_map = {"done": "done", "todo": "todo", "in-progress": "in-progress"}
        if len(args) == 1:
            cmd_list(tasks)
        elif len(args) == 2 and args[1] in status_map:
            cmd_list(tasks, status_map[args[1]])
        else:
            print(f"Unknown status '{args[1] if len(args) > 1 else ''}'. Use: todo, done, in-progress")
    else:
        print(f"Unknown command: {cmd}")
        usage()


if __name__ == "__main__":
    main()
