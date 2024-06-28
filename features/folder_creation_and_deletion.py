import os
import shutil
from utils.Speaker import speak

dir_path = os.path.expanduser('~/Desktop')

def make_dir(key = 'new_folder'):
    
    try:
       
        os.makedirs(dir_path+'/'+key,exist_ok=False)
        speak("Folder created")
        print(f'Folder at {dir_path}/{key} created..')
    
    except OSError as e:
        print(f"{e}")

 
 
 
        
def rem_dir(key):
    
    try:
        shutil.rmtree(dir_path+'/'+key)
        speak("Folder removed")
        print(f'Folder at {dir_path}/{key} removed.')
    except OSError as e:
        print(f'Failed to remove directory: {e}')


def make_file(key = 'new_file'):
    
    os.makedirs(os.path.dirname(dir_path+'/'+key), exist_ok=True)

    try:
        # Attempt to create the file
        with open(dir_path+'/'+key, 'x'):  # 'x' mode creates a new file; fails if the file already exists
            speak("file created")
            print(f"File created successfully at {dir_path}/{key}")
    except FileExistsError:
        print(f"File {dir_path}/{key} already exists. Skipping creation.")
    except FileNotFoundError:
        print(f"Directory for {dir_path}/{key} does not exist.")
    except PermissionError:
        print(f"Permission denied to create {dir_path}/{key}.")
    except Exception as e:
        print(f"An error occurred: {e}")

def rem_file(key):
        
    try:
        os.remove(dir_path+'/'+key)
        speak("file removed")
        print(f'File {dir_path}/{key} removed..')
    except FileNotFoundError:
        print(f'File {dir_path}/{key} not found')

rem_dir('vikram')
make_file('mytext')
rem_file('mytext')
make_dir('vikram')