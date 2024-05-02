
import os
import shutil
from typing import List, Tuple

def sort_files(directory: str, sort_by_date: bool = False) -> None:
    """
    Sorts files in the given directory by file type or creation date.

    :param directory: Path to the directory to sort files in.
    :param sort_by_date: If True, sort files by creation date, otherwise sort by file type.
    """
    # Get all possible file extensions
    extensions = {
        'video': ['mp4', 'mov', 'avi', 'mkv', 'wmv', '3gp', '3g2', 'mpg', 'mpeg', 'm4v', 'h264', 'flv', 'rm', 'swf', 'vob'],
        'data': ['sql', 'sqlite', 'sqlite3', 'csv', 'dat', 'db', 'log', 'mdb', 'sav', 'tar', 'xml'],
        'audio': ['mp3', 'wav', 'ogg', 'flac', 'aif', 'mid', 'midi', 'mpa', 'wma', 'wpl', 'cda'],
        'image': ['jpg', 'png', 'bmp', 'ai', 'psd', 'ico', 'jpeg', 'ps', 'svg', 'tif', 'tiff'],
        'archive': ['zip', 'rar', '7z', 'z', 'gz', 'rpm', 'arj', 'pkg', 'deb'],
        'text': ['pdf', 'txt', 'doc', 'docx', 'rtf', 'tex', 'wpd', 'odt'],
        '3d': ['stl', 'obj', 'fbx', 'dae', '3ds', 'iges', 'step'],
        'presentation': ['pptx', 'ppt', 'pps', 'key', 'odp'],
        'spreadsheet': ['xlsx', 'xls', 'xlsm', 'ods'],
        'font': ['otf', 'ttf', 'fon', 'fnt'],
        'gif': ['gif'],
        'exe': ['exe'],
        'bat': ['bat'],
        'apk': ['apk']
    }

    # Create directories for each file type
    for file_type in extensions.keys():
        os.makedirs(os.path.join(directory, file_type), exist_ok=True)

    # Get all files in the directory
    files = []
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        if os.path.isfile(file_path):
            # Get file extension and creation date
            file_ext = os.path.splitext(file_name)[1][1:].lower()
            creation_date = os.path.getctime(file_path) if sort_by_date else None
            # Add file to the list
            files.append((file_path, file_ext, creation_date))

    # Sort files by creation date or file type
    if sort_by_date:
        sorted_files = sorted(files, key=lambda x: x[2])
    else:
        sorted_files = sorted(files, key=lambda x: x[1])

    # Move sorted files to corresponding directories
    for file_path, file_ext, _ in sorted_files:
        for file_type, exts in extensions.items():
            if file_ext in exts:
                new_dir = os.path.join(directory, file_type)
                shutil.move(file_path, new_dir)




