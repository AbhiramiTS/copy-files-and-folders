import os
import subprocess
from log_config import get_logger

logger = get_logger()


def validate_dir(current_dir):
    if os.path.exists(current_dir):
        if os.path.isdir(current_dir):
            logger.info(f"{current_dir} is a valid directory.")
            return True
    return False
        

def create_dest_dir(dst_dir):
    if not os.path.exists(dst_dir):
        try:
            os.makedirs(dst_dir)
            logger.info(f"Created destination directory: {dst_dir}")
            username = os.getenv('USERNAME')  # Get the current username
            quoted_dest_dir = f'"{dst_dir}"'  # Ensure destination path is quoted
            quoted_username = f'"{username}"'  # Ensure username is quoted

            command = f'icacls {quoted_dest_dir} /grant {quoted_username}:F /T'

            subprocess.run(command, shell=True, check=True)
            logger.info(f"Full permissions granted to {dst_dir}.")
        except Exception as e:
            logger.error(f"Error creating directory: {e}")
            return False
    else:
        logger.error(f"Destination directory already exists: {dst_dir}")
    
    return True




    
        
    