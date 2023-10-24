import os
import json

import argparse


class ProjectManager:
    def __init__(self, data_dir='projects/'):
        self.data_dir = data_dir
        self.projects = []
        self.load_projects()

    def load_projects(self):
        for filename in os.listdir(self.data_dir):
            if filename.endswith('.json'):
                with open(os.path.join(self.data_dir, filename), 'r') as file:
                    project_data = json.load(file)
                    self.projects.append(project_data)

    def save_project(self, project):
        filename = f"{project['name'].replace(' ', '_')}.json"
        with open(os.path.join(self.data_dir, filename), 'w') as file:
            json.dump(project, file)

    def list_projects(self, show_completed=False):
        for project in self.projects:
            if show_completed or project['status'] != 'completed':
                print(f"Name: {project['name']}, Priority: {project['priority']}, Status: {project['status']}")

    def add_project(self):
        name = input("请输入项目名称: ")
        priority = input("请输入优先级 (High/Medium/Low): ")
        status = input("请输入状态 (In Progress/Completed): ")
        category = input("请输入分类: ")
        tags = input("请输入标签，用逗号分隔: ").split(',')

        project = {
            "name": name,
            "priority": priority,
            "status": status,
            "category": category,
            "tags": [tag.strip() for tag in tags]
        }

        self.save_project(project)
        self.projects.append(project)

def main():
    parser = argparse.ArgumentParser(description="Project Manager CLI")
    parser.add_argument('command', choices=['list', 'add'], help="Command to perform")
    parser.add_argument('--show-completed', action='store_true', help="Show completed projects")

    args = parser.parse_args()

    manager = ProjectManager()

    if args.command == 'list':
        manager.list_projects(show_completed=args.show_completed)
    elif args.command == 'add':
        manager.add_project()

if __name__ == "__main__":
    main()
