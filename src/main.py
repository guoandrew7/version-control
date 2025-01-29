from datetime import datetime

with open('version.md', 'w') as file:
    # Write data to the file
    file.write(str(datetime.now()))