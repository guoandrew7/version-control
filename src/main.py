from datetime import datetime
import os

def write_version():
    # Define the path to the version.md file
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    version_file = os.path.join(repo_root, "version.md")
    
    # Get the current date and time in the required format
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Write to version.md
    with open(version_file, "w") as f:
        f.write(f"{now}\n")
