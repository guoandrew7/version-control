from datetime import datetime 
from zoneinfo import ZoneInfo

with open('version.md', 'w') as file:
    file.write(str(datetime.now(ZoneInfo("America/Los_Angeles")))[0:-6])
