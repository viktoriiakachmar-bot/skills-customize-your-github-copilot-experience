# 📘 Assignment: Study Planner CLI

## 🎯 Objective

Build a Python command-line study planner that helps students organize assignments, track deadlines, and stay on top of upcoming work.

## 📝 Tasks

### 🛠️ Create the Study Task Model

#### Description
Design a simple data model for a study task and make sure each task includes the information students need to manage their workload.

#### Requirements
Completed program should:

- Define a task with a title, subject, due date, priority level, and completion status.
- Use a class or data structure to represent each study item.
- Include a way to mark a task as complete or update its priority.
- Show a clear summary for each task.
- Example:
  ```python
  title = "Complete Chemistry review"
  subject = "Science"
  due_date = "2026-11-05"
  priority = "high"
  ```

### 🛠️ Build the Planner Features

#### Description
Create the main CLI workflow so a student can add, view, update, and save their study tasks.

#### Requirements
Completed program should:

- Allow a student to add a new task.
- Display all tasks in a readable list, sorted by due date or priority.
- Let the user mark a task as complete.
- Save the planner data to a JSON file so the list persists between runs.
- Print a helpful message when there are no tasks or when a task is not found.
- Example menu:
  ```text
  1. Add task
  2. View tasks
  3. Mark task complete
  4. Save and exit
  ```

### 🛠️ Add a Smart Summary

#### Description
Extend the planner with a simple summary feature so students can quickly see what matters most this week.

#### Requirements
Completed program should:

- Count how many tasks are complete and incomplete.
- Highlight upcoming deadlines or high-priority tasks.
- Display a short summary before the program exits.
- Example output:
  ```text
  Total tasks: 5
  Completed: 2
  High priority tasks: 1
  ```
