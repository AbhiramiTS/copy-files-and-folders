import os
import shutil
from validate_dir import create_dest_dir
from log_config import get_logger

logger = get_logger()

def copy_entire_directory(src, dest,compress):
    for item in os.listdir(src):
        src_item = os.path.join(src, item)
        dest_item = os.path.join(dest, item)
        
        if "__MACOSX" in src_item or src_item.startswith("._"):
            logger.info(f"Ignoring items starting with '.' or '_'")
            continue
        
        if os.path.isdir(src_item):
            if not os.path.exists(dest_item):
                create_dest_dir(dest_item)
            copy_entire_directory(src_item, dest_item, compress)
        else:
            try:
                shutil.copy2(src_item, dest_item)  
                logger.info(f"Copied: {src_item} -> {dest_item}")
            except PermissionError as e:
                logger.error(f"PermissionError: {e}. Skipping {dest_item}.")
            except Exception as e:
                logger.error(f"An unexpected error occurred: {e}. Skipping {dest_item}.")
    
