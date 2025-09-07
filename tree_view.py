import os

EXCLUDE = {"venv", "__pycache__", ".git", ".idea", ".vscode"}

def print_tree(startpath, prefix=""):
    for item in sorted(os.listdir(startpath)):
        if item in EXCLUDE or item.startswith("."):
            continue
        path = os.path.join(startpath, item)
        if os.path.isdir(path):
            print(f"{prefix}|-- {item}/")
            print_tree(path, prefix + "|   ")
        else:
            print(f"{prefix}|-- {item}")

print("Project Folder Structure:\n")
print("Blood-Donor-Platform/")
print_tree(".")
