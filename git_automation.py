import os
import subprocess

class GitAutomation:
    def __init__(self, repo_path="."):
        self.repo_path = repo_path
        os.chdir(self.repo_path)

    def run_command(self, command):
        try:
            result = subprocess.run(command, shell=True, check=True,
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Қате орын алды: {e.stderr}")

    def initialize_repo(self):
        if not os.path.exists(".git"):
            print("Git репозиторий табылмады. Инициализация жасалуда...")
            self.run_command("git init")

    def create_gitignore(self):
        if not os.path.exists(".gitignore"):
            print(".gitignore файлы табылмады. Жасалуда...")
            with open(".gitignore", "w") as f:
                f.write("# Python\n__pycache__/\n*.pyc\n.env\n")

    def add_changes(self):
        self.run_command("git add .")

    def commit_changes(self, message):
        self.run_command(f'git commit -m "{message}"')

    def push_changes(self):
        self.run_command("git push origin main")

    def automate(self):
        self.initialize_repo()
        self.create_gitignore()
        self.add_changes()
        commit_msg = input("Commit хабарламасын енгізіңіз: ")
        self.commit_changes(commit_msg)
        self.push_changes()

if __name__ == "__main__":
    git_bot = GitAutomation()
    git_bot.automate()
