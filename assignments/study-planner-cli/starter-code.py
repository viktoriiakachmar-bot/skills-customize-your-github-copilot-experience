import json
from dataclasses import dataclass, asdict


@dataclass
class StudyTask:
    title: str
    subject: str
    due_date: str
    priority: str = "medium"
    completed: bool = False

    def to_dict(self):
        return asdict(self)


class StudyPlanner:
    def __init__(self, file_path="study_tasks.json"):
        self.file_path = file_path
        self.tasks = self.load_tasks()

    def load_tasks(self):
        # TODO: open the JSON file if it exists and return a list of tasks
        return []

    def save_tasks(self):
        # TODO: write the current tasks to the JSON file
        pass

    def add_task(self, title, subject, due_date, priority="medium"):
        # TODO: create a StudyTask and append it to the list
        pass

    def list_tasks(self):
        # TODO: print each task with a readable summary
        pass

    def mark_complete(self, task_index):
        # TODO: mark the selected task as complete
        pass

    def summary(self):
        # TODO: return a summary of total, completed, and high-priority tasks
        return {}


def main():
    planner = StudyPlanner()

    while True:
        print("\n1. Add task")
        print("2. View tasks")
        print("3. Mark task complete")
        print("4. Show summary")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            # TODO: gather task details and call add_task
            pass
        elif choice == "2":
            # TODO: call list_tasks
            pass
        elif choice == "3":
            # TODO: ask the user which task to complete and call mark_complete
            pass
        elif choice == "4":
            # TODO: display the planner summary
            pass
        elif choice == "5":
            planner.save_tasks()
            print("Good luck with your studies!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
