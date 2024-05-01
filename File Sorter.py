
import os

# set the main path to the directory where you want to sort files
main_path = 'C:\\Test'

# create a new directory for sorted files
os.mkdir(main_path + '\\sorted')

# define a dictionary of file extensions and their corresponding file types
extensions = {
    'video': ['mp4', 'mov', 'avi', 'mkv', 'wmv', '3gp', '3g2', 'mpg', 'mpeg', 'm4v',
              'h264', 'flv', 'rm', 'swf', 'vob'],
    'data': ['sql', 'sqlite', 'sqlite3', 'csv', 'dat', 'db', 'log', 'mdb', 'sav',
             'tar', 'xml'],
    'audio': ['mp3', 'wav', 'ogg', 'flac', 'aif', 'mid', 'midi', 'mpa', 'wma', 'wpl',
              'cda'],
    'image': ['jpg', 'png', 'bmp', 'ai', 'psd', 'ico', 'jpeg', 'ps', 'svg', 'tif',
              'tiff'],
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

# define a function to create new directories for each file type
def create_folders_from_ist(folder_path, folder_names):
    # iterate through each folder name
    for folder in folder_names:
        # create a new directory for the file type if it doesn't already exist
        if not os.path.exists(f'{folder_path}\\{folder}'):
            os.mkdir(f'{folder_path}\\{folder}')

# define a function to get a list of all subdirectories in a directory
def get_subfolder_paths(folder_path) -> list:
    # use os.scandir to get a list of all subdirectories
    subfolder_paths = [f.path for f in os.scandir(folder_path) if f.is_dir()]
    # return the list of subdirectories
    return subfolder_paths

# define a function to get a list of all files in a directory
def get_file_paths(folder_path) -> list:
    # use os.scandir to get a list of all files
    file_paths = [f.path for f in os.scandir(folder_path) if not f.is_dir()]
    # return the list of files
    return file_paths

# define a function to sort files into their corresponding directories
def sort_files(folder_path):
    # get a list of all files in the directory
    file_paths = get_file_paths(folder_path)
    # get a list of all file extensions and their corresponding file types
    ext_list = list(extensions.items())
    # iterate through each file
    for file_path in file_paths:
        # get the file extension
        extension = file_path.split('.')[-1]
        # get the file name
        file_name = file_path.split('\\')[-1]
        # iterate through each file type
        for dict_key_int in range(len(ext_list)):
            # check if the file extension matches the current file type
            if extension in ext_list[dict_key_int][1]:
                # print a message indicating that the file is being moved
                print(f'Moving {file_name} in {ext_list[dict_key_int][0]} folder\n')
                # move the file to the corresponding directory
                os.rename(file_path, f'{main_path}\\{ext_list[dict_key_int][0]}\\{file_name}')

# define a function to delete empty directories
def remove_empty_folders(folder_path):
    # get a list of all subdirectories in the directory
    subfolder_paths = get_subfolder_paths(folder_path)
    # iterate through each subdirectory
    for p in subfolder_paths:
        # check if the subdirectory is empty
        if not os.listdir(p):
            # print a message indicating that the empty directory is being deleted
            print('Deleting empty folder', p.split('\\')[-1], '\n')
            # delete the empty directory
            os.rmdir(p)

# check if the script is being run directly (not being imported as a module)
if __name__ == "__main__":
    # create new directories for each file type
    create_folders_from_ist(main_path, extensions)
    # sort files into their corresponding directories
    sort_files(main_path)
    # delete empty directories
    remove_empty_folders(main_path)




