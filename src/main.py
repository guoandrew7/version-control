from datetime import datetime

with open('version.md', 'w') as file:
    file.write(str(datetime.now()))