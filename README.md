# Directory Copier

**Directory Copier** is a user-friendly GUI tool built using Python and Tkinter that simplifies the process of copying files or entire directories. The tool includes features such as selective file extension filtering and detailed logging for every operation. 

⚠ **Note:** The compression feature is planned but not implemented yet.

## Features

- Copy individual files based on specific extensions.
- Copy entire directories (without compression for now).
- Real-time success/error status displayed at the bottom of the screen.
- Access to detailed log files for debugging and tracking operations.
- Intuitive graphical interface for easy navigation and use.

## Prerequisites

- Python 3.7 or higher
- Required Python libraries:
  - `tkinter` (comes pre-installed with Python)
  - `Pillow`
  - `shutil` (built-in)
  
To install additional dependencies, run:
```bash
pip install pillow
```

## How to Use
- Clone the repository
```bash
git clone https://github.com/yourusername/directory-copier.git
cd directory-copier
```

- Run the script:
```bash
python user_input.py
```

## How to Use the GUI

Use the GUI to:
- Select source and destination directories.
- Choose whether to copy specific file types or entire directories.
- **Compression options are not available yet.**
- Click **Start Copy** to begin the process.
- View logs (if available) after the operation by clicking the **View Log File** link.

---

## Screenshots

### Main Interface
![Main Interface](images/screenshot1.png)

### Copying Files with Specific Extensions
![Copying Files with Specific Extensions](images/screenshot2.png)

### Log File View Option
![Log File View Option](images/screenshot3.png)

---

## Folder Structure

```plaintext
directory-copier/
│
├── directory_copier.py      # Main application code
├── copy_files.py            # Helper functions for file operations
├── log/                     # Directory containing log files
├── screenshots/             # Folder for screenshots (used in README)
└── README.md                # Project documentation
```


