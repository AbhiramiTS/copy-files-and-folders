import logging
import os
from datetime import datetime

# Log directory
log_dir = "C://Users//My Account//Downloads//Automation//logs"

# Ensure the log directory exists
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Log file name based on the current date
current_date = datetime.now().strftime("%Y-%m-%d")
log_file = os.path.join(log_dir, f"directory_copier_{current_date}.log")

# Create a logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Create a file handler to write logs to the file
file_handler = logging.FileHandler(log_file)
file_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

# Add the file handler to the logger
logger.addHandler(file_handler)

# Optionally, you can also add a console handler to log to the console
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
logger.addHandler(console_handler)

# Function to get the logger (so other files can use it)
def get_logger():
    return logger

def get_latest_log_file():
    if not os.path.exists(log_dir):
        return None  
    
    log_files = [os.path.join(log_dir, f) for f in os.listdir(log_dir) if f.endswith('.log')]
    if not log_files:
        return None  
    
    latest_log_file = max(log_files, key=os.path.getmtime)
    return latest_log_file 
