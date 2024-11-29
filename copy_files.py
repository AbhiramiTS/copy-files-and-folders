import os
import shutil
import validate_dir
from copy_dir import copy_entire_directory
from log_config import get_logger

# source_dir = input("Enter the Source Directory").strip()
# dest_dir = input("Enter the Destination Directory").strip()

# source_dir = r"{}".format(source_dir)
# dest_dir = r"{}".format(dest_dir)

# copy_type = input("Do you want to copy only files or the whole directory? (Enter 'files' or 'directory'): ").strip().lower()

# if copy_type == 'files':
#     extensions = tuple(set("." + ext for ext in input("Enter the extensions separated by comma: ").split(',')))


logger = get_logger()


def copy_files(source_dir, dest_dir, extensions):
    
    source_dir_exist = validate_dir.validate_dir(source_dir)
    if not source_dir_exist:
        logger.error(f"Source Directory does not exists. Invalid path: {source_dir}")
        return False
    
    for file_name in os.listdir(source_dir):
        
        src_file = os.path.join(source_dir, file_name)
        dest_file = os.path.join(dest_dir, file_name)

        try:
            if os.path.isfile(src_file) and file_name.lower().endswith(extensions):            
                shutil.copyfile(src_file, dest_file)
                logger.info(f"Copied: {src_file} -> {dest_file}")
        except PermissionError as e:
            logger.error(f"PermissionError: {e}. Skipping {dest_file}.")
        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}. Skipping {dest_file}.")
    logger.info(f"All files have been copied!.")
    return True


def copy_dirs(source_dir, dest_dir, compress):
    
    source_dir_exist = validate_dir.validate_dir(source_dir)
    if not source_dir_exist:
        logger.error(f"Source Directory does not exists. Invalid path: {source_dir}")
        return False
    
    if not validate_dir.validate_dir(dest_dir):
        if not validate_dir.create_dest_dir(dest_dir):
            logger.info(f"Error creating destination folder. Exiting.")
            exit(1)
    logger.info(f"Copying the whole directory.")
    copy_entire_directory(source_dir, dest_dir, compress)
    logger.info(f"Copied entire directory: {source_dir} -> {dest_dir}")
    return True


# source_dir = r'C:\Users\My Account\Documents\BackUpTest'
# dest_dir = r"D:\Backup Images"

# C:\Users\My Account\Downloads\QA_Wolf_Take_Home





        
    
    
